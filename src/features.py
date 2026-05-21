"""
features.py

Time-series feature extraction functions for CSI-like signals.

Extracts simple statistical and signal-level features
from preprocessed CSI amplitude arrays.

NOTE: Designed for synthetic/simulated data in this research prototype.

Part of the wifi-csi-fall-detection research prototype.
"""

import numpy as np
import pandas as pd


def extract_features(signal):
    """
    Extract simple time-series features from a CSI-like signal.

    Features are computed across the entire signal array (flattened),
    capturing basic statistical properties useful for classification.

    Features extracted:
    - mean: Average amplitude value
    - std: Standard deviation (measure of variability)
    - energy: Sum of squared values (total signal energy)
    - peak_to_peak: Range between max and min amplitude
    - max_amplitude: Maximum amplitude value

    Parameters
    ----------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Preprocessed CSI-like amplitude array

    Returns
    -------
    features : dict
        Dictionary of feature name -> feature value
    """
    flat = signal.flatten()  # Flatten to 1D for simple feature extraction

    features = {
        'mean':          np.mean(flat),
        'std':           np.std(flat),
        'energy':        np.sum(flat ** 2),
        'peak_to_peak':  np.max(flat) - np.min(flat),
        'max_amplitude': np.max(flat),
    }

    return features


def extract_features_batch(signals):
    """
    Extract features from a list of signals and return as a DataFrame.

    Parameters
    ----------
    signals : list of np.ndarray
        List of signal arrays, each of shape (n_samples, n_subcarriers)

    Returns
    -------
    df : pd.DataFrame
        DataFrame with one row per signal and one column per feature
    """
    rows = []
    for sig in signals:
        feat = extract_features(sig)
        rows.append(feat)

    df = pd.DataFrame(rows)
    return df
