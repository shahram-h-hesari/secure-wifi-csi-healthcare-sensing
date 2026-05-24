"""
defenses.py
===========
Simple synthetic CSI defense and robustness-hardening functions.

IMPORTANT NOTE
--------------
All functions in this module operate on synthetic CSI-like data only.
No real WiFi CSI hardware is used. No real physical-layer defense is implemented.
No clinical validation or validated security protection is included.
Results produced by these functions are synthetic prototype outputs intended
for research-methodology demonstration only.

These defenses are simple preprocessing methods. They do not guarantee
robustness against adaptive adversaries or real-world physical-layer attacks.

Label convention
----------------
  0 = normal activity
  1 = fall-like event

Dependencies
------------
  numpy, pandas, scipy.ndimage, sklearn

Author: WiFi CSI Fall Detection Research Prototype
Phase:  7 - Defense Methods and Robustness Hardening
"""

import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d, median_filter
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)


# ---------------------------------------------------------------------------
# Preprocessing defense functions
# ---------------------------------------------------------------------------

def moving_average_defense(X, window_size=5):
    """
    Apply a sliding-window mean filter along the sample axis for each feature.

    This defense smooths the feature distribution by replacing each sample
    value with the mean of a local window. It is intended to reduce the
    effect of high-frequency Gaussian noise perturbations.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Synthetic CSI-like feature matrix (may be clean or perturbed).
    window_size : int, optional (default=5)
        Size of the sliding window. Larger windows produce stronger smoothing
        but may blur genuine signal transitions.

    Returns
    -------
    X_defended : np.ndarray, shape (n_samples, n_features)
        Smoothed feature matrix. Original array is not modified.

    Notes
    -----
    - This is a synthetic prototype defense only.
    - Cannot remove large burst perturbations or structured adversarial
      perturbations.
    - scipy.ndimage.uniform_filter1d is used for efficiency.
    """
    X_defended = np.zeros_like(X, dtype=float)
    for j in range(X.shape[1]):
        X_defended[:, j] = uniform_filter1d(X[:, j].astype(float), size=window_size)
    return X_defended


def median_filter_defense(X, kernel_size=5):
    """
    Apply a median filter along the sample axis for each feature.

    Median filtering is robust to spike-like outliers and burst perturbations.
    It preserves edges better than mean filtering and is less susceptible to
    extreme values introduced by synthetic burst perturbations.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Synthetic CSI-like feature matrix (may be clean or perturbed).
    kernel_size : int, optional (default=5)
        Size of the median filter kernel. Must be a positive odd integer.

    Returns
    -------
    X_defended : np.ndarray, shape (n_samples, n_features)
        Median-filtered feature matrix. Original array is not modified.

    Notes
    -----
    - This is a synthetic prototype defense only.
    - Computationally more expensive than moving_average_defense.
    - scipy.ndimage.median_filter is applied per feature column.
    """
    X_defended = np.zeros_like(X, dtype=float)
    for j in range(X.shape[1]):
        col = X[:, j].astype(float).reshape(-1, 1)
        X_defended[:, j] = median_filter(col, size=(kernel_size, 1)).ravel()
    return X_defended


def clip_outliers(X, lower_percentile=1.0, upper_percentile=99.0):
    """
    Clip feature values to a range defined by percentile thresholds.

    Extreme values introduced by synthetic perturbations (especially burst
    and subcarrier perturbations) can dominate the feature space. Clipping
    limits these extreme values to reduce their effect on the classifier.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Synthetic CSI-like feature matrix (may be clean or perturbed).
    lower_percentile : float, optional (default=1.0)
        Lower bound percentile. Values below this quantile are clipped up.
    upper_percentile : float, optional (default=99.0)
        Upper bound percentile. Values above this quantile are clipped down.

    Returns
    -------
    X_defended : np.ndarray, shape (n_samples, n_features)
        Clipped feature matrix. Original array is not modified.

    Notes
    -----
    - This is a synthetic prototype defense only.
    - Thresholds are computed per feature column from the provided data.
    - May discard genuine extreme values if percentiles are set too tightly.
    """
    X_defended = X.copy().astype(float)
    for j in range(X.shape[1]):
        lo = np.percentile(X_defended[:, j], lower_percentile)
        hi = np.percentile(X_defended[:, j], upper_percentile)
        X_defended[:, j] = np.clip(X_defended[:, j], lo, hi)
    return X_defended


def robust_normalize(X, epsilon=1e-8):
    """
    Normalize features using median and interquartile range (IQR).

    Standard z-score normalization (mean/std) is sensitive to outliers.
    Robust normalization uses the median and IQR as location and scale
    estimates, reducing the influence of extreme perturbation values on
    the normalization.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Synthetic CSI-like feature matrix (may be clean or perturbed).
    epsilon : float, optional (default=1e-8)
        Small constant added to the IQR denominator to avoid division by zero.

    Returns
    -------
    X_normalized : np.ndarray, shape (n_samples, n_features)
        Robustly normalized feature matrix. Original array is not modified.

    Notes
    -----
    - This is a synthetic prototype defense only.
    - Does not remove perturbations; only reduces their relative scale.
    - Statistics are computed per feature column from the provided data.
    """
    X_normalized = X.copy().astype(float)
    for j in range(X.shape[1]):
        col = X_normalized[:, j]
        median_val = np.median(col)
        q75, q25 = np.percentile(col, [75, 25])
        iqr = q75 - q25
        X_normalized[:, j] = (col - median_val) / (iqr + epsilon)
    return X_normalized


# ---------------------------------------------------------------------------
# Perturbation-aware augmentation
# ---------------------------------------------------------------------------

def augment_with_perturbations(X_train, y_train, noise_std=0.3, random_seed=42):
    """
    Create a perturbation-augmented training dataset by combining clean and
    noisy synthetic samples.

    This function provides a simple prototype of perturbation-aware training
    (analogous to adversarial training). A copy of the training data is
    perturbed with Gaussian noise and appended to the clean training set.
    The combined dataset can be used to train a classifier that is more
    robust to low-level noise perturbations.

    Parameters
    ----------
    X_train : np.ndarray, shape (n_samples, n_features)
        Clean synthetic CSI-like training feature matrix.
    y_train : np.ndarray, shape (n_samples,)
        Training labels (0 = normal, 1 = fall).
    noise_std : float, optional (default=0.3)
        Standard deviation of the Gaussian noise added to perturbed copies.
    random_seed : int, optional (default=42)
        Random seed for reproducibility.

    Returns
    -------
    X_augmented : np.ndarray, shape (2 * n_samples, n_features)
        Augmented feature matrix (clean + perturbed copies).
    y_augmented : np.ndarray, shape (2 * n_samples,)
        Augmented labels (original labels repeated for perturbed copies).

    Notes
    -----
    - This is a synthetic prototype of perturbation-aware training only.
    - Full adversarial training (e.g., PGD-based) is not implemented.
    - Labels are preserved: perturbed copies retain the same class label
      as their clean originals, which is appropriate for this synthetic
      noise model.
    """
    rng = np.random.default_rng(random_seed)
    noise = rng.normal(loc=0.0, scale=noise_std, size=X_train.shape)
    X_perturbed = X_train + noise
    X_augmented = np.vstack([X_train, X_perturbed])
    y_augmented = np.concatenate([y_train, y_train])
    return X_augmented, y_augmented


# ---------------------------------------------------------------------------
# Comparison utility
# ---------------------------------------------------------------------------

def compare_defended_vs_undefended(y_true, y_pred_clean, y_pred_perturbed, y_pred_defended):
    """
    Compare ML and clinical-safety-aware metrics for three conditions:
    clean, perturbed (undefended), and defended-perturbed.

    Safety-aware metrics assume:
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
        Classifier predictions on perturbed (undefended) synthetic test data.
    y_pred_defended : array-like of int
        Classifier predictions on defended (preprocessed perturbed) test data.

    Returns
    -------
    summary : dict
        Dictionary with keys 'clean', 'perturbed', 'defended', each containing
        a sub-dict with 'ml_metrics' and 'safety_metrics'.

    Notes
    -----
    All metrics are computed from synthetic labels and predictions only.
    Results do not represent clinical outcomes or validated performance.
    """
    y_true = np.array(y_true)

    def _ml(y_t, y_p):
        return {
            'accuracy':  round(accuracy_score(y_t, y_p), 4),
            'precision': round(precision_score(y_t, y_p, zero_division=0), 4),
            'recall':    round(recall_score(y_t, y_p, zero_division=0), 4),
            'f1_score':  round(f1_score(y_t, y_p, zero_division=0), 4),
        }

    def _safety(y_t, y_p):
        cm = confusion_matrix(y_t, y_p, labels=[0, 1])
        tn, fp, fn, tp = cm.ravel()
        n_falls   = int(tp + fn)
        n_normals = int(tn + fp)
        mfr = round(fn / n_falls,   4) if n_falls   > 0 else 0.0
        far = round(fp / n_normals, 4) if n_normals > 0 else 0.0
        afi = 'HIGH' if far > 0.2 else ('MODERATE' if far > 0.05 else 'LOW')
        return {
            'missed_falls':            int(fn),
            'false_alarms':            int(fp),
            'missed_fall_rate':        mfr,
            'false_alarm_rate':        far,
            'alarm_fatigue_indicator': afi,
        }

    results = {}
    for label, y_p in [('clean', y_pred_clean),
                       ('perturbed', y_pred_perturbed),
                       ('defended', y_pred_defended)]:
        yp = np.array(y_p)
        results[label] = {
            'ml_metrics':     _ml(y_true, yp),
            'safety_metrics': _safety(y_true, yp),
        }
    return results
