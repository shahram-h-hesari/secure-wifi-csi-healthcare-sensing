"""
preprocessing.py

Signal preprocessing utilities for synthetic CSI-like time-series data.

This module includes simple smoothing and normalization functions used in the
WiFi CSI fall detection research prototype.

IMPORTANT:
This repository currently uses synthetic CSI-like time-series data for
demonstration purposes. It does not use real patient data, real clinical data,
or validated WiFi CSI measurements. Results are intended only to demonstrate
the research workflow and should not be interpreted as clinical or real-world
fall detection performance.

Part of the wifi-csi-fall-detection research prototype.

Author: Shahram H. Hesari
PhD Student, Electrical and Computer Engineering
Portland State University
"""

import numpy as np
from scipy.ndimage import uniform_filter1d


def smooth_signal(signal, window_size=5):
    """
    Smooth a one-dimensional signal using a simple moving average filter.

    This reduces short-term noise by averaging each sample with its nearby
    neighbors inside a sliding window.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.
    window_size : int, default=5
        Number of samples in the moving-average window.
        Larger values produce smoother signals but may reduce sharp transient
        features.

    Returns
    -------
    smoothed : numpy.ndarray
        Smoothed one-dimensional signal with the same length as the input.

    Notes
    -----
    This function is intended for synthetic CSI-like demonstration data only.
    It is not a clinically validated preprocessing method.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")
    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")
    if window_size < 1:
        raise ValueError("window_size must be at least 1.")

    return uniform_filter1d(signal, size=window_size)


def normalize_csi(signal):
    """
    Normalize a CSI-like signal to zero mean and unit standard deviation.

    This is a standard z-score normalization. It shifts the signal to have
    mean zero and scales it so that the standard deviation equals one.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.

    Returns
    -------
    normalized : numpy.ndarray
        Normalized signal. If the standard deviation is zero, only mean
        subtraction is applied.

    Notes
    -----
    This function is intended for synthetic CSI-like demonstration data only.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")
    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    std = np.std(signal)
    if std == 0.0:
        return signal - np.mean(signal)
    return (signal - np.mean(signal)) / std


# Alias so notebook imports still work with older name
normalize_signal = normalize_csi


def remove_mean(signal):
    """
    Remove the mean (DC offset) from a one-dimensional signal.

    This centers the signal around zero without scaling.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.

    Returns
    -------
    centered : numpy.ndarray
        Mean-subtracted signal.

    Notes
    -----
    This function is intended for synthetic CSI-like demonstration data only.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")
    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    return signal - np.mean(signal)


def preprocess_signal(signal, window_size=7, normalize=True):
    """
    Apply a full preprocessing pipeline to a single synthetic CSI-like signal.

    Steps applied:
      1. Smooth using a moving-average filter.
      2. Optionally normalize to zero mean and unit standard deviation.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.
    window_size : int, default=7
        Size of the smoothing window.
    normalize : bool, default=True
        Whether to apply z-score normalization after smoothing.

    Returns
    -------
    processed : numpy.ndarray
        Preprocessed one-dimensional signal.

    Notes
    -----
    This function is intended for synthetic CSI-like demonstration data only.
    """
    processed = smooth_signal(signal, window_size=window_size)
    if normalize:
        processed = normalize_csi(processed)
    return processed


def preprocess_dataset(X, window_size=7, normalize=True):
    """
    Apply preprocessing to every signal in a dataset array.

    Parameters
    ----------
    X : numpy.ndarray of shape (n_samples, signal_length)
        Array of synthetic CSI-like signals.
    window_size : int, default=7
        Size of the smoothing window applied to each signal.
    normalize : bool, default=True
        Whether to apply z-score normalization to each signal.

    Returns
    -------
    X_processed : numpy.ndarray of shape (n_samples, signal_length)
        Preprocessed signal array.

    Notes
    -----
    This function is intended for synthetic CSI-like demonstration data only.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X must be a 2D array of shape (n_samples, signal_length).")

    return np.array([
        preprocess_signal(row, window_size=window_size, normalize=normalize)
        for row in X
    ])
