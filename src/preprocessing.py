"""
preprocessing.py

Signal preprocessing utilities for synthetic CSI-like time-series data.

This module includes simple smoothing and normalization functions used in the
WiFi CSI fall detection research prototype.

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

    if not isinstance(window_size, int):
        raise TypeError("window_size must be an integer.")

    if window_size < 1:
        raise ValueError("window_size must be at least 1.")

    if window_size > signal.size:
        raise ValueError("window_size must not be larger than the signal length.")

    kernel = np.ones(window_size) / window_size
    smoothed = np.convolve(signal, kernel, mode="same")

    return smoothed


def normalize_signal(signal):
    """
    Normalize a one-dimensional signal using z-score normalization.

    The output signal has approximately zero mean and unit standard deviation.
    This is useful for comparing signals with different amplitude scales.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.

    Returns
    -------
    normalized : numpy.ndarray
        Z-score-normalized signal.

    Notes
    -----
    If the signal has zero standard deviation, this function returns a
    zero-centered signal to avoid division by zero.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")

    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    mean = np.mean(signal)
    std = np.std(signal)

    if std == 0:
        return signal - mean

    normalized = (signal - mean) / std

    return normalized


def min_max_scale_signal(signal):
    """
    Scale a one-dimensional signal to the range [0, 1].

    This function is provided as an alternative to z-score normalization.

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional input signal.

    Returns
    -------
    scaled : numpy.ndarray
        Signal scaled to the range [0, 1].

    Notes
    -----
    If the signal has zero range, this function returns an array of zeros.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")

    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    signal_min = np.min(signal)
    signal_max = np.max(signal)
    signal_range = signal_max - signal_min

    if signal_range == 0:
        return np.zeros_like(signal)

    scaled = (signal - signal_min) / signal_range

    return scaled
