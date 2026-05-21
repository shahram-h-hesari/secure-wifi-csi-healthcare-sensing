"""
features.py

Basic time-series feature extraction utilities for synthetic CSI-like signals.

This module extracts simple statistical features from preprocessed one-dimensional
signals. These features are used as inputs to beginner-friendly baseline machine
learning models.

IMPORTANT:
This repository currently uses synthetic CSI-like time-series data for demonstration
purposes. It does not use real patient data, real clinical data, or validated WiFi
CSI measurements. Results are intended only to demonstrate the research workflow
and should not be interpreted as clinical or real-world fall detection performance.

Part of the wifi-csi-fall-detection research prototype.

Author: Shahram H. Hesari
PhD Candidate, Electrical and Computer Engineering
Portland State University
"""

import numpy as np


def extract_basic_features(signal):
    """
    Extract basic statistical features from a one-dimensional time-series signal.

    These features are intentionally simple and interpretable. They are designed
    to demonstrate a baseline feature-extraction workflow for synthetic CSI-like
    signals.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional preprocessed CSI-like time-series signal.

    Returns
    -------
    features : dict
        Dictionary containing basic time-series features:

        - mean : average signal value
        - std : standard deviation of the signal
        - energy : sum of squared signal values
        - ptp_range : peak-to-peak range, computed as max - min
        - max_value : maximum signal value
        - min_value : minimum signal value
        - variance : variance of the signal

    Notes
    -----
    These features are extracted from synthetic data only. They are not validated
    clinical biomarkers and should not be interpreted as real-world fall detection
    features.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")

    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    features = {
        "mean": np.mean(signal),
        "std": np.std(signal),
        "energy": np.sum(signal ** 2),
        "ptp_range": np.ptp(signal),
        "max_value": np.max(signal),
        "min_value": np.min(signal),
        "variance": np.var(signal),
    }

    return features
