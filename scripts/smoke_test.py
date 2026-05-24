"""
smoke_test.py
=============
Lightweight smoke test for the WiFi CSI Fall Detection Research Prototype.

IMPORTANT NOTE
--------------
This script uses synthetic CSI-like data only.
It does not use real WiFi CSI hardware measurements.
It does not validate clinical fall-detection performance.
It does not validate real-world adversarial defense.
Successful execution of this script is not evidence of clinical validation
or hardware deployment readiness.

Usage
-----
    python scripts/smoke_test.py

Expected output
---------------
    [SMOKE TEST] PASSED - Synthetic pipeline ran without errors.
"""

import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score
)


def print_banner():
    """Print the smoke test disclaimer banner."""
    print("")
    print("=" * 60)
    print("[SMOKE TEST] WiFi CSI Fall Detection Research Prototype")
    print("[SMOKE TEST] Phase 10 - Testing and Verification")
    print("[SMOKE TEST] All data is SYNTHETIC only.")
    print("[SMOKE TEST] This test does NOT validate real CSI,")
    print("[SMOKE TEST] clinical performance, or hardware deployment.")
    print("=" * 60)
    print("")


def generate_synthetic_csi(n_samples=200, n_subcarriers=30,
                            n_packets=100, fall_strength=2.0,
                            noise_std=0.3, random_seed=42):
    """
    Generate synthetic normal and fall-like CSI-like amplitude signals.

    Returns
    -------
    X_normal : np.ndarray, shape (n_samples, n_packets, n_subcarriers)
    X_fall   : np.ndarray, shape (n_samples, n_packets, n_subcarriers)
    """
    rng = np.random.default_rng(random_seed)
    base = rng.normal(loc=0.0, scale=1.0, size=(n_samples, n_packets, n_subcarriers))
    X_normal = base + rng.normal(loc=0.0, scale=noise_std,
                                  size=(n_samples, n_packets, n_subcarriers))
    fall_pulse = np.zeros((n_samples, n_packets, n_subcarriers))
    fall_start = n_packets // 3
    fall_end   = n_packets // 3 + n_packets // 5
    fall_pulse[:, fall_start:fall_end, :] = fall_strength
    X_fall = base + fall_pulse + rng.normal(loc=0.0, scale=noise_std,
                                             size=(n_samples, n_packets, n_subcarriers))
    return X_normal, X_fall


def extract_features(X):
    """
    Extract simple statistical features from a synthetic CSI-like array.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_packets, n_subcarriers)

    Returns
    -------
    features : np.ndarray, shape (n_samples, 7)
        Columns: mean, std, energy, peak-to-peak, max, min, variance
    """
    amp = np.abs(X)  # treat signal magnitude as amplitude proxy
    flat = amp.reshape(amp.shape[0], -1)  # (n_samples, n_packets * n_subcarriers)
    mean     = flat.mean(axis=1)
    std      = flat.std(axis=1)
    energy   = (flat ** 2).mean(axis=1)
    ptp      = flat.max(axis=1) - flat.min(axis=1)
    maximum  = flat.max(axis=1)
    minimum  = flat.min(axis=1)
    variance = flat.var(axis=1)
    return np.column_stack([mean, std, energy, ptp, maximum, minimum, variance])


def run_smoke_test():
    """Run the end-to-end synthetic pipeline smoke test."""
    print_banner()

    # Step 1: Generate synthetic data
    print("[SMOKE TEST] Step 1: Generating synthetic CSI-like data...")
    n_samples = 200
    X_normal, X_fall = generate_synthetic_csi(n_samples=n_samples)
    print(f"  Normal shape : {X_normal.shape}")
    print(f"  Fall shape   : {X_fall.shape}")

    # Step 2: Create labels
    # 0 = normal, 1 = fall
    y = np.array([0] * n_samples + [1] * n_samples)
    X_all = np.vstack([X_normal, X_fall])

    # Step 3: Extract features
    print("[SMOKE TEST] Step 2: Extracting statistical features...")
    features = extract_features(X_all)
    print(f"  Feature matrix shape: {features.shape}")
    assert features.shape == (2 * n_samples, 7), \
        f"Expected (400, 7), got {features.shape}"

    # Step 4: Train/test split
    print("[SMOKE TEST] Step 3: Splitting into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        features, y, test_size=0.25, random_state=42, stratify=y
    )
    print(f"  Train: {X_train.shape[0]} samples | Test: {X_test.shape[0]} samples")

    # Step 5: Train baseline classifier
    print("[SMOKE TEST] Step 4: Training baseline Random Forest classifier...")
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)

    # Step 6: Evaluate
    print("[SMOKE TEST] Step 5: Evaluating on synthetic test set...")
    y_pred = clf.predict(X_test)
    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec  = recall_score(y_test, y_pred, zero_division=0)
    f1   = f1_score(y_test, y_pred, zero_division=0)

    print("")
    print("[SMOKE TEST] Results (SYNTHETIC PROTOTYPE ONLY):")
    print(f"  Accuracy : {acc:.4f}")
    print(f"  Precision: {prec:.4f}")
    print(f"  Recall   : {rec:.4f}")
    print(f"  F1-score : {f1:.4f}")
    print("")
    print("[SMOKE TEST] Note: These metrics are computed from synthetic")
    print("[SMOKE TEST] labels and predictions only. They do not represent")
    print("[SMOKE TEST] clinical outcomes or real-world performance.")
    print("")
    print("=" * 60)
    print("[SMOKE TEST] PASSED - Synthetic pipeline ran without errors.")
    print("=" * 60)
    print("")


if __name__ == "__main__":
    try:
        run_smoke_test()
        sys.exit(0)
    except Exception as e:
        print(f"")
        print(f"[SMOKE TEST] FAILED - Error: {e}")
        sys.exit(1)
