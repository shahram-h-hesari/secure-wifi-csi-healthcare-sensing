"""
simulate_csi.py

Functions to generate synthetic CSI-like time-series signals.

NOTE: All data produced here is SYNTHETIC and SIMULATED.
It does not represent real WiFi channel measurements,
patient data, or clinical recordings.

Part of the wifi-csi-fall-detection research prototype.
Author: Shahram H. Hesari
Portland State University
"""

import numpy as np


def generate_normal_signal(length=200, noise_level=0.05, random_state=None):
    """
    Generate a synthetic CSI-like signal representing normal activity.

    Normal activity is modeled as low-amplitude smooth fluctuations
    with small random noise. This simulates a relatively stable
    WiFi channel with minor environmental changes (e.g., slow walking
    or sitting still).

    Parameters
    ----------
    length : int
        Number of time steps in the signal. Default is 200.
    noise_level : float
        Standard deviation of the Gaussian noise added to the signal.
        Default is 0.05.
    random_state : int or None
        Random seed for reproducibility. Default is None.

    Returns
    -------
    signal : numpy.ndarray
        1D array of shape (length,) representing the synthetic signal.
    """
    # Set random seed if provided for reproducibility
    rng = np.random.RandomState(random_state)

    # Create a time axis from 0 to 2*pi
    t = np.linspace(0, 2 * np.pi, length)

    # Normal activity: smooth low-amplitude sine wave with small noise
    # The sine wave simulates slow periodic channel fluctuations
    signal = 0.3 * np.sin(t) + noise_level * rng.randn(length)

    return signal


def generate_fall_like_signal(length=200, noise_level=0.05, random_state=None):
    """
    Generate a synthetic CSI-like signal representing a fall-like event.

    A fall-like event is modeled as a sudden transient spike followed by
    a recovery period. This simulates an abrupt change in the WiFi channel
    caused by a rapid body movement (i.e., a simulated fall).

    Parameters
    ----------
    length : int
        Number of time steps in the signal. Default is 200.
    noise_level : float
        Standard deviation of the Gaussian noise added to the signal.
        Default is 0.05.
    random_state : int or None
        Random seed for reproducibility. Default is None.

    Returns
    -------
    signal : numpy.ndarray
        1D array of shape (length,) representing the synthetic signal.
    """
    # Set random seed if provided for reproducibility
    rng = np.random.RandomState(random_state)

    # Start with a low-amplitude baseline similar to normal activity
    t = np.linspace(0, 2 * np.pi, length)
    signal = 0.3 * np.sin(t) + noise_level * rng.randn(length)

    # Add a transient spike to simulate the fall event
    # The spike occurs at roughly 40% into the signal
    spike_center = int(0.4 * length)
    spike_width = int(0.05 * length)  # spike lasts ~5% of signal length

    # Create a Gaussian-shaped spike with high amplitude
    for i in range(length):
        distance_from_spike = abs(i - spike_center)
        if distance_from_spike < spike_width:
            # The closer to the spike center, the higher the value
            signal[i] += 2.0 * np.exp(-0.5 * (distance_from_spike / (spike_width / 3)) ** 2)

    return signal


def generate_dataset(n_samples_per_class=100, length=200, random_state=42):
    """
    Generate a labeled dataset of synthetic CSI-like signals.

    Creates n_samples_per_class samples for each of two classes:
    - Class 0: normal activity signals
    - Class 1: fall-like event signals

    Parameters
    ----------
    n_samples_per_class : int
        Number of samples to generate per class. Default is 100.
    length : int
        Length of each signal (number of time steps). Default is 200.
    random_state : int
        Random seed for reproducibility. Default is 42.

    Returns
    -------
    X : numpy.ndarray
        Array of shape (2 * n_samples_per_class, length) containing all signals.
    y : numpy.ndarray
        Array of shape (2 * n_samples_per_class,) containing labels (0 or 1).
    """
    X = []  # will hold all signal arrays
    y = []  # will hold all labels

    # Generate normal activity signals (class 0)
    for i in range(n_samples_per_class):
        # Use a different random seed for each sample
        seed = random_state + i
        signal = generate_normal_signal(length=length, noise_level=0.05, random_state=seed)
        X.append(signal)
        y.append(0)  # class 0 = normal activity

    # Generate fall-like event signals (class 1)
    for i in range(n_samples_per_class):
        # Use a different random seed for each sample
        seed = random_state + n_samples_per_class + i
        signal = generate_fall_like_signal(length=length, noise_level=0.05, random_state=seed)
        X.append(signal)
        y.append(1)  # class 1 = fall-like event

    # Convert to numpy arrays
    X = np.array(X)
    y = np.array(y)

    return X, y
