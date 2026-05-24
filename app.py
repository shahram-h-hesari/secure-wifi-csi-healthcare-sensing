"""
Streamlit Demo Dashboard
WiFi CSI Fall Detection Research Prototype

Important:
This dashboard uses synthetic CSI-like data only. It is for research-prototype
visualization and education. It is not clinical validation, real CSI validation,
hardware deployment, or medical-grade fall-detection performance.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from scipy.ndimage import uniform_filter1d, median_filter
from scipy.fft import rfft, rfftfreq

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="WiFi CSI Fall Detection Demo",
    page_icon="📡",
    layout="wide"
)


# ------------------------------------------------------------
# Synthetic CSI generation
# ------------------------------------------------------------

def generate_normal_activity_csi(
    num_packets=300,
    num_subcarriers=30,
    noise_level=0.05,
    seed=None
):
    """Generate synthetic CSI-like amplitude and phase for normal activity."""
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 1, num_packets)

    amplitude = np.zeros((num_packets, num_subcarriers))
    phase = np.zeros((num_packets, num_subcarriers))

    for sc in range(num_subcarriers):
        base_amp = 1.0 + 0.1 * np.sin(2 * np.pi * (2 + sc * 0.02) * t)
        slow_motion = 0.05 * np.sin(2 * np.pi * (5 + sc * 0.01) * t)
        amplitude[:, sc] = base_amp + slow_motion + noise_level * rng.standard_normal(num_packets)

        base_phase = 0.2 * np.sin(2 * np.pi * (3 + sc * 0.02) * t)
        phase[:, sc] = base_phase + noise_level * rng.standard_normal(num_packets)

    return amplitude, phase


def generate_fall_event_csi(
    num_packets=300,
    num_subcarriers=30,
    noise_level=0.05,
    fall_strength=0.6,
    seed=None
):
    """Generate synthetic CSI-like amplitude and phase with a fall-like disturbance."""
    amplitude, phase = generate_normal_activity_csi(
        num_packets=num_packets,
        num_subcarriers=num_subcarriers,
        noise_level=noise_level,
        seed=seed
    )

    event_center = int(num_packets * 0.55)
    event_width = max(1, int(num_packets * 0.06))
    event_window = np.arange(num_packets)
    disturbance = np.exp(-0.5 * ((event_window - event_center) / event_width) ** 2)

    for sc in range(num_subcarriers):
        scale = fall_strength + 0.2 * np.sin(sc)
        amplitude[:, sc] += scale * disturbance
        phase[:, sc] += 0.5 * scale * disturbance * np.sin(
            2 * np.pi * 10 * event_window / num_packets
        )

    return amplitude, phase


# ------------------------------------------------------------
# Preprocessing and feature extraction
# ------------------------------------------------------------

def remove_mean(signal):
    """Remove the mean from each subcarrier."""
    return signal - np.mean(signal, axis=0, keepdims=True)


def normalize_csi(signal):
    """Normalize each subcarrier to zero mean and unit standard deviation."""
    mean = np.mean(signal, axis=0, keepdims=True)
    std = np.std(signal, axis=0, keepdims=True) + 1e-8
    return (signal - mean) / std


def smooth_signal(signal, window_size=5):
    """Apply moving-average smoothing along the packet/time axis."""
    return uniform_filter1d(signal, size=window_size, axis=0)


def preprocess_signal(signal):
    """Apply the basic preprocessing pipeline."""
    return smooth_signal(normalize_csi(remove_mean(signal)))


def extract_features(amplitude, sampling_rate=100):
    """Extract simple time-domain and frequency-domain features."""
    mean_signal = amplitude.mean(axis=1)

    spectrum = np.abs(rfft(mean_signal))
    freqs = rfftfreq(len(mean_signal), d=1 / sampling_rate)

    if len(spectrum) > 1:
        dominant_index = np.argmax(spectrum[1:]) + 1
        dominant_frequency = freqs[dominant_index]
    else:
        dominant_frequency = 0.0

    return {
        "mean": float(np.mean(mean_signal)),
        "std": float(np.std(mean_signal)),
        "max": float(np.max(mean_signal)),
        "min": float(np.min(mean_signal)),
        "range": float(np.max(mean_signal) - np.min(mean_signal)),
        "energy": float(np.sum(mean_signal ** 2)),
        "peak_to_average": float(np.max(mean_signal) / (np.mean(np.abs(mean_signal)) + 1e-8)),
        "dominant_frequency": float(dominant_frequency),
        "spectral_energy": float(np.sum(spectrum ** 2))
    }


# ------------------------------------------------------------
# Dataset and model
# ------------------------------------------------------------

@st.cache_data
def generate_synthetic_dataset(
    num_samples_per_class=120,
    num_packets=300,
    num_subcarriers=30,
    noise_level=0.05,
    fall_strength=0.6,
    seed=42
):
    """Generate a synthetic feature dataset for normal and fall-like classes."""
    rows = []
    labels = []

    rng = np.random.default_rng(seed)

    for i in range(num_samples_per_class):
        amp, _ = generate_normal_activity_csi(
            num_packets=num_packets,
            num_subcarriers=num_subcarriers,
            noise_level=noise_level,
            seed=int(rng.integers(0, 1_000_000))
        )
        amp_processed = preprocess_signal(amp)
        rows.append(extract_features(amp_processed))
        labels.append(0)

    for i in range(num_samples_per_class):
        amp, _ = generate_fall_event_csi(
            num_packets=num_packets,
            num_subcarriers=num_subcarriers,
            noise_level=noise_level,
            fall_strength=fall_strength,
            seed=int(rng.integers(0, 1_000_000))
        )
        amp_processed = preprocess_signal(amp)
        rows.append(extract_features(amp_processed))
        labels.append(1)

    return pd.DataFrame(rows), np.array(labels)


def train_baseline_model(X, y):
    """Train a simple baseline classifier."""
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = summarize_ml_metrics(y_test, y_pred, "baseline_test_split")
    safety = compute_clinical_safety_metrics(y_test, y_pred)

    return model, metrics, safety


# ------------------------------------------------------------
# Perturbation and defense functions
# ------------------------------------------------------------

def add_random_noise(signal, noise_std=0.25, seed=None):
    """Add Gaussian noise to a CSI-like signal."""
    rng = np.random.default_rng(seed)
    return signal + rng.normal(0, noise_std, size=signal.shape)


def add_burst_perturbation(signal, strength=1.0, center_fraction=0.55, width_fraction=0.04):
    """Add a short time-localized burst perturbation."""
    perturbed = signal.copy()
    num_packets = signal.shape[0]
    center = int(num_packets * center_fraction)
    width = max(1, int(num_packets * width_fraction))
    window = np.arange(num_packets)
    burst = strength * np.exp(-0.5 * ((window - center) / width) ** 2)
    perturbed += burst[:, None]
    return perturbed


def add_subcarrier_perturbation(signal, strength=0.6):
    """Perturb selected subcarriers."""
    perturbed = signal.copy()
    subcarrier_indices = [5, 10, 15, 20]

    for sc in subcarrier_indices:
        if sc < perturbed.shape[1]:
            perturbed[:, sc] += strength * np.sin(
                np.linspace(0, 8 * np.pi, perturbed.shape[0])
            )

    return perturbed


def apply_combined_perturbation(signal, strength=0.6, seed=None):
    """Apply noise, burst, and subcarrier perturbations."""
    perturbed = add_random_noise(signal, noise_std=0.25 * strength, seed=seed)
    perturbed = add_burst_perturbation(perturbed, strength=strength)
    perturbed = add_subcarrier_perturbation(perturbed, strength=0.5 * strength)
    return perturbed


def clip_outliers(signal, lower_percentile=1, upper_percentile=99):
    """Clip extreme values using percentile thresholds."""
    lower = np.percentile(signal, lower_percentile, axis=0, keepdims=True)
    upper = np.percentile(signal, upper_percentile, axis=0, keepdims=True)
    return np.clip(signal, lower, upper)


def robust_normalize(signal):
    """Normalize using median and interquartile range."""
    median = np.median(signal, axis=0, keepdims=True)
    q75 = np.percentile(signal, 75, axis=0, keepdims=True)
    q25 = np.percentile(signal, 25, axis=0, keepdims=True)
    iqr = q75 - q25 + 1e-8
    return (signal - median) / iqr


def apply_defense_pipeline(signal):
    """Apply a simple prototype defense pipeline."""
    defended = clip_outliers(signal)
    defended = median_filter(defended, size=(3, 1))
    defended = uniform_filter1d(defended, size=7, axis=0)
    defended = robust_normalize(defended)
    return defended


# ------------------------------------------------------------
# Metrics
# ------------------------------------------------------------

def summarize_ml_metrics(y_true, predictions, label):
    """Summarize standard ML metrics."""
    return {
        "condition": label,
        "accuracy": accuracy_score(y_true, predictions),
        "precision": precision_score(y_true, predictions, zero_division=0),
        "recall": recall_score(y_true, predictions, zero_division=0),
        "f1_score": f1_score(y_true, predictions, zero_division=0)
    }


def compute_clinical_safety_metrics(y_true, y_pred):
    """Compute simple clinical-safety-aware metrics from binary labels."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    total_falls = np.sum(y_true == 1)
    total_normal = np.sum(y_true == 0)

    missed_falls = np.sum((y_true == 1) & (y_pred == 0))
    false_alarms = np.sum((y_true == 0) & (y_pred == 1))
    detected_falls = np.sum((y_true == 1) & (y_pred == 1))

    missed_fall_rate = missed_falls / total_falls if total_falls > 0 else 0.0
    false_alarm_rate = false_alarms / total_normal if total_normal > 0 else 0.0

    if false_alarm_rate >= 0.30:
        alarm_fatigue_indicator = "High prototype false-alarm burden"
    elif false_alarm_rate >= 0.10:
        alarm_fatigue_indicator = "Moderate prototype false-alarm burden"
    else:
        alarm_fatigue_indicator = "Low prototype false-alarm burden"

    return {
        "total_true_fall_like_events": int(total_falls),
        "total_true_normal_events": int(total_normal),
        "detected_falls": int(detected_falls),
        "missed_falls": int(missed_falls),
        "false_alarms": int(false_alarms),
        "missed_fall_rate": missed_fall_rate,
        "false_alarm_rate": false_alarm_rate,
        "alarm_fatigue_indicator": alarm_fatigue_indicator
    }


# ------------------------------------------------------------
# Plot helpers
# ------------------------------------------------------------

def plot_mean_signal(normal_signal, fall_signal, ylabel, title):
    """Plot mean signal across subcarriers."""
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(normal_signal.mean(axis=1), label="Normal activity")
    ax.plot(fall_signal.mean(axis=1), label="Fall-like event")
    ax.set_xlabel("Packet index")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig


def plot_single_subcarrier(normal_signal, fall_signal, subcarrier_index):
    """Plot one subcarrier for normal and fall-like samples."""
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(normal_signal[:, subcarrier_index], label="Normal activity")
    ax.plot(fall_signal[:, subcarrier_index], label="Fall-like event")
    ax.set_xlabel("Packet index")
    ax.set_ylabel("CSI amplitude")
    ax.set_title(f"Example Subcarrier {subcarrier_index}: Normal vs Fall-like Event")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig


def plot_bar_metric(df, metric, title):
    """Plot a metric comparison as a bar chart."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df["condition"], df[metric])
    ax.set_ylabel(metric)
    ax.set_title(title)
    ax.set_ylim(0, 1.05)
    ax.tick_params(axis="x", rotation=15)
    fig.tight_layout()
    return fig


# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------

st.title("WiFi CSI Fall Detection Research Prototype")

st.warning(
    "This dashboard uses synthetic CSI-like data only. It is not clinical validation, "
    "not real CSI validation, not hardware deployment, and not medical-grade fall detection."
)

st.markdown(
    """
This demo visualizes a simplified WiFi CSI fall-detection research workflow:

- Synthetic CSI amplitude and phase generation
- Normal vs fall-like event visualization
- Baseline ML classification
- Clinical-safety-aware metrics
- Synthetic perturbation stress testing
- Simple prototype defense/hardening comparison
"""
)

with st.sidebar:
    st.header("Simulation Controls")

    num_packets = st.slider("Number of packets", 100, 600, 300, step=50)
    num_subcarriers = st.slider("Number of subcarriers", 10, 64, 30, step=2)
    noise_level = st.slider("Noise level", 0.01, 0.20, 0.05, step=0.01)
    fall_strength = st.slider("Fall-like event strength", 0.2, 1.5, 0.6, step=0.1)
    perturbation_strength = st.slider("Perturbation strength", 0.1, 2.0, 0.8, step=0.1)
    subcarrier_index = st.slider(
        "Subcarrier index to visualize",
        0,
        max(0, num_subcarriers - 1),
        min(10, max(0, num_subcarriers - 1))
    )

    run_demo = st.button("Run demo", type="primary")


# Generate example signals
normal_amp, normal_phase = generate_normal_activity_csi(
    num_packets=num_packets,
    num_subcarriers=num_subcarriers,
    noise_level=noise_level,
    seed=1
)

fall_amp, fall_phase = generate_fall_event_csi(
    num_packets=num_packets,
    num_subcarriers=num_subcarriers,
    noise_level=noise_level,
    fall_strength=fall_strength,
    seed=2
)

st.header("1. Synthetic CSI Signal Visualization")

col1, col2 = st.columns(2)

with col1:
    st.pyplot(
        plot_mean_signal(
            normal_amp,
            fall_amp,
            "Mean CSI amplitude",
            "Synthetic CSI Amplitude"
        )
    )

with col2:
    st.pyplot(
        plot_mean_signal(
            normal_phase,
            fall_phase,
            "Mean CSI phase",
            "Synthetic CSI Phase"
        )
    )

st.pyplot(plot_single_subcarrier(normal_amp, fall_amp, subcarrier_index))


st.header("2. Baseline Classifier Demo")

with st.spinner("Training baseline model on synthetic features..."):
    X, y = generate_synthetic_dataset(
        num_samples_per_class=120,
        num_packets=num_packets,
        num_subcarriers=num_subcarriers,
        noise_level=noise_level,
        fall_strength=fall_strength,
        seed=42
    )

    model, baseline_metrics, baseline_safety = train_baseline_model(X, y)

baseline_metrics_df = pd.DataFrame([baseline_metrics])
baseline_safety_df = pd.DataFrame([baseline_safety])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", f"{baseline_metrics['accuracy']:.3f}")
col2.metric("Precision", f"{baseline_metrics['precision']:.3f}")
col3.metric("Recall", f"{baseline_metrics['recall']:.3f}")
col4.metric("F1-score", f"{baseline_metrics['f1_score']:.3f}")

st.caption(
    "These metrics are computed from synthetic CSI-like data only and should not be interpreted as real-world fall-detection performance."
)

st.subheader("Clinical-Safety-Aware Prototype Metrics")
st.dataframe(baseline_safety_df, use_container_width=True)


st.header("3. Synthetic Adversarial Robustness Stress Test")

st.markdown(
    """
This section compares clean synthetic CSI-like samples with perturbed synthetic samples.
The perturbations are synthetic stress tests only and are not real physical-layer attacks.
"""
)

def build_eval_sets(num_samples_per_class=60):
    """Build clean, perturbed, and defended synthetic evaluation sets."""
    rng = np.random.default_rng(123)

    clean_rows = []
    perturbed_rows = []
    defended_rows = []
    labels = []

    for class_label in [0, 1]:
        for sample_idx in range(num_samples_per_class):
            if class_label == 0:
                amp, _ = generate_normal_activity_csi(
                    num_packets=num_packets,
                    num_subcarriers=num_subcarriers,
                    noise_level=noise_level,
                    seed=int(rng.integers(0, 1_000_000))
                )
            else:
                amp, _ = generate_fall_event_csi(
                    num_packets=num_packets,
                    num_subcarriers=num_subcarriers,
                    noise_level=noise_level,
                    fall_strength=fall_strength,
                    seed=int(rng.integers(0, 1_000_000))
                )

            clean_signal = preprocess_signal(amp)
            perturbed_signal = apply_combined_perturbation(
                clean_signal,
                strength=perturbation_strength,
                seed=int(rng.integers(0, 1_000_000))
            )
            defended_signal = apply_defense_pipeline(perturbed_signal)

            clean_rows.append(extract_features(clean_signal))
            perturbed_rows.append(extract_features(perturbed_signal))
            defended_rows.append(extract_features(defended_signal))
            labels.append(class_label)

    return (
        pd.DataFrame(clean_rows),
        pd.DataFrame(perturbed_rows),
        pd.DataFrame(defended_rows),
        np.array(labels)
    )


X_clean, X_perturbed, X_defended, y_eval = build_eval_sets()

clean_pred = model.predict(X_clean)
perturbed_pred = model.predict(X_perturbed)
defended_pred = model.predict(X_defended)

clean_ml = summarize_ml_metrics(y_eval, clean_pred, "clean_synthetic")
perturbed_ml = summarize_ml_metrics(y_eval, perturbed_pred, "perturbed_synthetic")
defended_ml = summarize_ml_metrics(y_eval, defended_pred, "defended_synthetic")

robustness_df = pd.DataFrame([clean_ml, perturbed_ml, defended_ml])

st.subheader("Clean vs Perturbed vs Defended ML Metrics")
st.dataframe(robustness_df, use_container_width=True)

st.pyplot(plot_bar_metric(robustness_df, "f1_score", "F1-score Comparison"))


st.header("4. Safety Impact of Perturbation and Defense")

clean_safety = compute_clinical_safety_metrics(y_eval, clean_pred)
perturbed_safety = compute_clinical_safety_metrics(y_eval, perturbed_pred)
defended_safety = compute_clinical_safety_metrics(y_eval, defended_pred)

safety_comparison_df = pd.DataFrame([
    dict(clean_safety, condition="clean_synthetic"),
    dict(perturbed_safety, condition="perturbed_synthetic"),
    dict(defended_safety, condition="defended_synthetic")
])

st.dataframe(safety_comparison_df, use_container_width=True)

st.markdown(
    """
### Interpretation

This dashboard demonstrates how a WiFi CSI sensing pipeline can be evaluated using:

- Standard ML metrics, such as accuracy, precision, recall, and F1-score
- Clinical-safety-aware metrics, such as missed falls and false alarms
- Synthetic robustness stress tests
- Simple prototype defense methods

The current version is a research prototype using synthetic data only.
"""
)


st.header("5. Limitations and Next Steps")

st.markdown(
    """
### Current limitations

- Uses synthetic CSI-like data only
- Does not use real WiFi CSI measurements
- Does not use clinical or patient data
- Does not include hardware deployment
- Does not claim medical-grade fall detection
- Does not claim validated security protection
- Synthetic perturbations are not real physical-layer attacks

### Future extensions

- Add real CSI datasets when available
- Add hardware data collection
- Add stronger adversarial robustness experiments
- Add perturbation-aware training
- Add clinical-safety-aware evaluation on real datasets
- Add dashboard screenshots to the GitHub README
"""
)
