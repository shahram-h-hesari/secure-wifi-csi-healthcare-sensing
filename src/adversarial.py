"""
adversarial.py
==============
Synthetic CSI perturbation functions for adversarial robustness stress testing.

IMPORTANT NOTE
--------------
All functions in this module operate on synthetic CSI-like data only.
No real WiFi CSI hardware is used. No real physical-layer attack is implemented.
No clinical validation is included. Results produced by these functions are
synthetic prototype outputs intended for research-methodology demonstration only.

Label convention
----------------
  0 = normal activity
  1 = fall-like event

Dependencies
------------
  numpy, pandas, sklearn

Author: WiFi CSI Fall Detection Research Prototype
Phase:  6 - Adversarial Robustness Stress Testing
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)


# ---------------------------------------------------------------------------
# Perturbation functions
# ---------------------------------------------------------------------------

def add_random_noise(X, noise_std=0.5, random_seed=42):
    """
    Add Gaussian random noise to all features of a synthetic CSI-like dataset.

    This function models low-level background interference or hardware noise
    by adding independent Gaussian noise to every feature dimension.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Clean synthetic CSI-like feature matrix.
    noise_std : float, optional (default=0.5)
        Standard deviation of the Gaussian noise.
        Larger values produce stronger perturbations.
    random_seed : int, optional (default=42)
        Random seed for reproducibility.

    Returns
    -------
    X_perturbed : np.ndarray, shape (n_samples, n_features)
        Perturbed feature matrix. Original array is not modified.

    Notes
    -----
    This is a synthetic perturbation only. It does not replicate
    real WiFi channel noise or hardware-level interference.
    """
    rng = np.random.default_rng(random_seed)
    noise = rng.normal(loc=0.0, scale=noise_std, size=X.shape)
    return X + noise


def add_burst_perturbation(X, burst_magnitude=2.0, burst_fraction=0.1, random_seed=42):
    """
    Add a time-localized burst disturbance to a random subset of samples.

    This function simulates a sudden interference-like event affecting a short
    window of samples, such as a co-channel transmitter activating briefly.
    The burst is applied uniformly across all feature dimensions of the
    affected samples.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Clean synthetic CSI-like feature matrix.
    burst_magnitude : float, optional (default=2.0)
        Magnitude of the additive burst perturbation.
    burst_fraction : float in (0, 1], optional (default=0.1)
        Fraction of samples to affect with the burst.
    random_seed : int, optional (default=42)
        Random seed for reproducibility.

    Returns
    -------
    X_perturbed : np.ndarray, shape (n_samples, n_features)
        Perturbed feature matrix. Original array is not modified.

    Notes
    -----
    This is a synthetic perturbation only. It does not replicate a real
    RF burst, jammer, or hardware interference event.
    """
    rng = np.random.default_rng(random_seed)
    X_perturbed = X.copy()
    n_samples = X.shape[0]
    n_burst = max(1, int(n_samples * burst_fraction))
    burst_indices = rng.choice(n_samples, size=n_burst, replace=False)
    X_perturbed[burst_indices, :] += burst_magnitude
    return X_perturbed


def add_subcarrier_perturbation(X, subcarrier_indices=None, perturbation_scale=1.5, random_seed=42):
    """
    Add perturbation to selected feature dimensions (simulating subcarrier-level effects).

    Real WiFi CSI measurements are resolved per subcarrier. This function
    simulates selective subcarrier degradation by perturbing only a specified
    subset of feature dimensions (e.g., mean amplitude features corresponding
    to specific subcarrier groups).

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Clean synthetic CSI-like feature matrix.
    subcarrier_indices : list of int or None, optional (default=None)
        Feature indices to perturb. If None, the first half of features is used.
    perturbation_scale : float, optional (default=1.5)
        Standard deviation of the Gaussian perturbation applied to target features.
    random_seed : int, optional (default=42)
        Random seed for reproducibility.

    Returns
    -------
    X_perturbed : np.ndarray, shape (n_samples, n_features)
        Perturbed feature matrix. Original array is not modified.

    Notes
    -----
    Perturbation is applied at the extracted feature level, not at the true
    RF subcarrier level. This is a simplified synthetic stress test only.
    """
    rng = np.random.default_rng(random_seed)
    X_perturbed = X.copy()
    n_features = X.shape[1]
    if subcarrier_indices is None:
        subcarrier_indices = list(range(n_features // 2))
    noise = rng.normal(loc=0.0, scale=perturbation_scale, size=(X.shape[0], len(subcarrier_indices)))
    X_perturbed[:, subcarrier_indices] += noise
    return X_perturbed


# ---------------------------------------------------------------------------
# Dataset-level perturbation helper
# ---------------------------------------------------------------------------

def generate_perturbed_dataset(X, perturbation_type='random_noise', random_seed=42, **kwargs):
    """
    Apply a named perturbation to a synthetic CSI-like feature matrix.

    This is a convenience wrapper that selects and applies one of the three
    supported perturbation types by name.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Clean synthetic CSI-like feature matrix.
    perturbation_type : str, optional (default='random_noise')
        One of: 'random_noise', 'burst_perturbation', 'subcarrier_perturbation'.
    random_seed : int, optional (default=42)
        Random seed passed to the perturbation function.
    **kwargs
        Additional keyword arguments passed to the selected perturbation function.

    Returns
    -------
    X_perturbed : np.ndarray, shape (n_samples, n_features)
        Perturbed feature matrix.

    Raises
    ------
    ValueError
        If `perturbation_type` is not one of the supported types.

    Notes
    -----
    All perturbations are synthetic. Results are prototype outputs only.
    """
    supported = ['random_noise', 'burst_perturbation', 'subcarrier_perturbation']
    if perturbation_type not in supported:
        raise ValueError(
            f"Unknown perturbation_type '{perturbation_type}'. "
            f"Choose one of: {supported}"
        )
    if perturbation_type == 'random_noise':
        return add_random_noise(X, random_seed=random_seed, **kwargs)
    elif perturbation_type == 'burst_perturbation':
        return add_burst_perturbation(X, random_seed=random_seed, **kwargs)
    elif perturbation_type == 'subcarrier_perturbation':
        return add_subcarrier_perturbation(X, random_seed=random_seed, **kwargs)


# ---------------------------------------------------------------------------
# Comparison metrics
# ---------------------------------------------------------------------------

def compare_clean_vs_perturbed_metrics(y_true, y_pred_clean, y_pred_perturbed, label_names=None):
    """
    Compare ML performance metrics and safety-aware metrics for clean vs
    perturbed synthetic classifier predictions.

    Safety-aware metrics are computed assuming:
      - Label 1 = fall-like event (positive class)
      - Label 0 = normal activity (negative class)

    Missed falls = fall events predicted as normal (false negatives).
    False alarms = normal events predicted as fall (false positives).

    Parameters
    ----------
    y_true : array-like of int
        Ground-truth labels (0 = normal, 1 = fall).
    y_pred_clean : array-like of int
        Classifier predictions on clean synthetic test data.
    y_pred_perturbed : array-like of int
        Classifier predictions on perturbed synthetic test data.
    label_names : list of str or None, optional
        Human-readable names for classes [class_0, class_1].
        Defaults to ['normal', 'fall'].

    Returns
    -------
    summary : dict
        Dictionary containing:
          - 'clean_ml'     : dict with accuracy, precision, recall, f1
          - 'perturbed_ml' : dict with accuracy, precision, recall, f1
          - 'clean_safety' : dict with missed_falls, false_alarms, rates
          - 'perturbed_safety' : dict with missed_falls, false_alarms, rates
          - 'degradation'  : dict with metric deltas (perturbed - clean)

    Notes
    -----
    All metrics are computed from synthetic labels and predictions only.
    These results do not represent clinical outcomes or validated performance.
    """
    if label_names is None:
        label_names = ['normal', 'fall']

    y_true = np.array(y_true)
    y_pred_clean = np.array(y_pred_clean)
    y_pred_perturbed = np.array(y_pred_perturbed)

    def _ml_metrics(y_t, y_p):
        return {
            'accuracy':  round(accuracy_score(y_t, y_p), 4),
            'precision': round(precision_score(y_t, y_p, zero_division=0), 4),
            'recall':    round(recall_score(y_t, y_p, zero_division=0), 4),
            'f1_score':  round(f1_score(y_t, y_p, zero_division=0), 4),
        }

    def _safety_metrics(y_t, y_p):
        cm = confusion_matrix(y_t, y_p, labels=[0, 1])
        tn, fp, fn, tp = cm.ravel()
        n_falls = int(tp + fn)
        n_normals = int(tn + fp)
        missed_falls  = int(fn)
        false_alarms  = int(fp)
        missed_fall_rate  = round(fn / n_falls,   4) if n_falls   > 0 else 0.0
        false_alarm_rate  = round(fp / n_normals, 4) if n_normals > 0 else 0.0
        alarm_fatigue_indicator = 'HIGH' if false_alarm_rate > 0.2 else (
                                  'MODERATE' if false_alarm_rate > 0.05 else 'LOW')
        return {
            'missed_falls':              missed_falls,
            'false_alarms':              false_alarms,
            'missed_fall_rate':          missed_fall_rate,
            'false_alarm_rate':          false_alarm_rate,
            'alarm_fatigue_indicator':   alarm_fatigue_indicator,
        }

    clean_ml      = _ml_metrics(y_true, y_pred_clean)
    perturbed_ml  = _ml_metrics(y_true, y_pred_perturbed)
    clean_safety     = _safety_metrics(y_true, y_pred_clean)
    perturbed_safety = _safety_metrics(y_true, y_pred_perturbed)

    degradation = {
        'accuracy_delta':          round(perturbed_ml['accuracy']  - clean_ml['accuracy'],  4),
        'precision_delta':         round(perturbed_ml['precision'] - clean_ml['precision'], 4),
        'recall_delta':            round(perturbed_ml['recall']    - clean_ml['recall'],    4),
        'f1_score_delta':          round(perturbed_ml['f1_score']  - clean_ml['f1_score'],  4),
        'missed_falls_delta':      perturbed_safety['missed_falls']     - clean_safety['missed_falls'],
        'false_alarms_delta':      perturbed_safety['false_alarms']     - clean_safety['false_alarms'],
        'missed_fall_rate_delta':  round(perturbed_safety['missed_fall_rate'] - clean_safety['missed_fall_rate'], 4),
        'false_alarm_rate_delta':  round(perturbed_safety['false_alarm_rate'] - clean_safety['false_alarm_rate'], 4),
    }

    return {
        'clean_ml':         clean_ml,
        'perturbed_ml':     perturbed_ml,
        'clean_safety':     clean_safety,
        'perturbed_safety': perturbed_safety,
        'degradation':      degradation,
    }
