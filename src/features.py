"""
features.py

Time-series feature extraction functions for CSI-like signals.
Extracts simple statistical features from preprocessed signal arrays.

NOTE: Designed for synthetic/simulated data in this research prototype.
Not validated for clinical use.

Part of the wifi-csi-fall-detection research prototype.
Author: Shahram H. Hesari
Portland State University
"""

import numpy as np


def extract_basic_features(signal):
    """
    Extract basic statistical features from a 1D time-series signal.

    These features are simple and easy to understand. They are designed
    to capture basic properties of the signal shape that might differ
    between normal activity and fall-like events.

    Parameters
    ----------
    signal : numpy.ndarray
        1D array representing a preprocessed CSI-like time-series signal.

    Returns
    -------
    features : dict
        Dictionary containing the following features:
        - 'mean'      : average value of the signal
        - 'std'       : standard deviation (spread of values)
        - 'energy'    : sum of squared values (total signal energy)
        - 'ptp_range' : peak-to-peak range (max minus min)
        - 'max_value' : maximum value in the signal
        - 'min_value' : minimum value in the signal
        - 'variance'  : variance (std squared)
    """
    # Mean: average amplitude of the signal
    mean = np.mean(signal)

    # Standard deviation: how much the signal varies around the mean
    std = np.std(signal)

    # Energy: sum of squared values
    # Fall events tend to have higher energy due to the spike
    energy = np.sum(signal ** 2)

    # Peak-to-peak range: difference between max and min
    # Fall events tend to have a larger range due to the spike
    ptp_range = np.ptp(signal)  # ptp = peak-to-peak

    # Maximum value in the signal
    max_value = np.max(signal)

    # Minimum value in the signal
    min_value = np.min(signal)

    # Variance: the square of the standard deviation
    variance = np.var(signal)

    # Pack all features into a dictionary
    features = {
        'mean': mean,
        'std': std,
        'energy': energy,
        'ptp_range': ptp_range,
        'max_value': max_value,
        'min_value': min_value,
        'variance': variance
    }

    return features
