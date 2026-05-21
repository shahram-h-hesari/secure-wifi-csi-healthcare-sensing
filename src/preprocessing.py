"""
preprocessing.py

Signal preprocessing functions for CSI-like time-series data.

Includes smoothing/filtering and normalization utilities.

NOTE: Designed for synthetic/simulated data in this research prototype.
Not validated for clinical use.

Part of the wifi-csi-fall-detection research prototype.
"""

import numpy as np
from scipy.ndimage import uniform_filter1d


def smooth_signal(signal, window_size=5):
    """
    Apply a moving average (uniform) filter to smooth the signal.

    Applies 1D uniform smoothing along the time axis (axis=0),
    independently for each subcarrier channel.

    Parameters
    ----------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Raw CSI-like amplitude array
    window_size : int
        Size of the smoothing window (default: 5)

    Returns
    -------
    smoothed : np.ndarray of shape (n_samples, n_subcarriers)
        Smoothed signal array
    """
    # Apply uniform filter along time axis (axis=0) for each subcarrier
    smoothed = uniform_filter1d(signal, size=window_size, axis=0)
    return smoothed


def normalize_signal(signal):
    """
    Normalize a signal to zero mean and unit variance (z-score normalization).

    Normalization is applied globally across the entire signal array.
    This brings signals to a common scale, which helps with ML training.

    Parameters
    ----------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Input signal array

    Returns
    -------
    normalized : np.ndarray of shape (n_samples, n_subcarriers)
        Normalized signal array (zero mean, unit std)
    """
    mean = np.mean(signal)
    std = np.std(signal)

    # Avoid division by zero for flat signals
    if std < 1e-8:
        return signal - mean

    normalized = (signal - mean) / std
    return normalized


def preprocess_signal(signal, window_size=5):
    """
    Apply full preprocessing pipeline: smoothing followed by normalization.

    Parameters
    ----------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Raw CSI-like amplitude array
    window_size : int
        Smoothing window size (default: 5)

    Returns
    -------
    processed : np.ndarray of shape (n_samples, n_subcarriers)
        Preprocessed signal array
    """
    smoothed = smooth_signal(signal, window_size=window_size)
    processed = normalize_signal(smoothed)
    return processed
