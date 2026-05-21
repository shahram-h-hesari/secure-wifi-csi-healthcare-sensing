"""
preprocessing.py

Signal preprocessing functions for CSI-like time-series data.
Includes smoothing/filtering and normalization utilities.

NOTE: Designed for synthetic/simulated data in this research prototype.
Not validated for clinical use.

Part of the wifi-csi-fall-detection research prototype.
Author: Shahram H. Hesari
Portland State University
"""

import numpy as np


def smooth_signal(signal, window_size=5):
    """
    Smooth a signal using a simple moving average filter.

    This reduces short-term noise in the signal by averaging
    each point with its neighbors within a sliding window.

    Parameters
    ----------
    signal : numpy.ndarray
        1D array representing the input signal.
    window_size : int
        Number of points to include in each averaging window.
        Larger values produce smoother signals but may reduce
        sharp feature visibility. Default is 5.

    Returns
    -------
    smoothed : numpy.ndarray
        1D array of the same length as the input signal,
        with edge values handled using 'same' convolution mode.
    """
    # Create a uniform averaging kernel (all weights equal to 1/window_size)
    kernel = np.ones(window_size) / window_size

    # Apply convolution to compute moving average
    # 'same' mode ensures output has the same length as input
    smoothed = np.convolve(signal, kernel, mode='same')

    return smoothed


def normalize_signal(signal):
    """
    Normalize a signal to the range [0, 1] using min-max scaling.

    This scales the signal so that the minimum value becomes 0
    and the maximum value becomes 1. This is useful for comparing
    signals with different amplitude ranges.

    Parameters
    ----------
    signal : numpy.ndarray
        1D array representing the input signal.

    Returns
    -------
    normalized : numpy.ndarray
        1D array of the same length, scaled to [0, 1].
        If the signal has zero range (all values equal),
        returns an array of zeros to avoid division by zero.
    """
    signal_min = np.min(signal)
    signal_max = np.max(signal)
    signal_range = signal_max - signal_min

    # Avoid division by zero if the signal is constant
    if signal_range == 0:
        return np.zeros_like(signal)

    # Apply min-max normalization
    normalized = (signal - signal_min) / signal_range

    return normalized
