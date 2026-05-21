"""
simulate_csi.py

Synthetic CSI-like signal generation utilities for the WiFi CSI fall detection
research prototype.

This module generates simple one-dimensional time-series signals that loosely
represent CSI-like amplitude behavior for two conceptual classes:

- Class 0: normal activity
- Class 1: fall-like event

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


def generate_normal_signal(length=200, noise_level=0.05, random_state=None):
    """
    Generate a synthetic CSI-like signal representing normal activity.

    Normal activity is modeled as low-amplitude smooth fluctuations with
    small random noise. This represents a simplified, relatively stable
    wireless sensing condition.

    Parameters
    ----------
    length : int, default=200
        Number of time samples in the signal.

    noise_level : float, default=0.05
        Standard deviation of the Gaussian noise added to the signal.

    random_state : int or None, default=None
        Random seed for reproducibility.

    Returns
    -------
    signal : numpy.ndarray of shape (length,)
        One-dimensional synthetic CSI-like amplitude signal.

    Notes
    -----
    This signal is synthetic and is not a real WiFi CSI measurement.
    """
    if length <= 0:
        raise ValueError("length must be a positive integer.")

    if noise_level < 0:
        raise ValueError("noise_level must be non-negative.")

    rng = np.random.default_rng(random_state)
    t = np.linspace(0, 1, length)

    slow_variation = 0.15 * np.sin(2 * np.pi * 3 * t)
    small_motion = 0.05 * np.sin(2 * np.pi * 12 * t)
    noise = noise_level * rng.normal(size=length)

    signal = 1.0 + slow_variation + small_motion + noise

    return signal


def generate_fall_like_signal(length=200, noise_level=0.05, random_state=None):
    """
    Generate a synthetic CSI-like signal representing a fall-like event.

    A fall-like event is modeled as a sudden transient spike followed by
    a short recovery dip. This is a simplified conceptual model of an abrupt
    change in the wireless sensing signal.

    Parameters
    ----------
    length : int, default=200
        Number of time samples in the signal.

    noise_level : float, default=0.05
        Standard deviation of the Gaussian noise added to the signal.

    random_state : int or None, default=None
        Random seed for reproducibility.

    Returns
    -------
    signal : numpy.ndarray of shape (length,)
        One-dimensional synthetic CSI-like amplitude signal.

    Notes
    -----
    This signal is synthetic and is not a real WiFi CSI measurement or a
    validated fall signature.
    """
    if length <= 0:
        raise ValueError("length must be a positive integer.")

    if noise_level < 0:
        raise ValueError("noise_level must be non-negative.")

    rng = np.random.default_rng(random_state)

    signal = generate_normal_signal(
        length=length,
        noise_level=noise_level,
        random_state=random_state
    )

    center = rng.integers(low=int(length * 0.35), high=int(length * 0.70))
    width = rng.integers(low=max(3, int(length * 0.025)), high=max(4, int(length * 0.07)))
    amplitude = rng.uniform(0.8, 1.3)

    sample_index = np.arange(length)
    transient = amplitude * np.exp(
        -0.5 * ((sample_index - center) / width) ** 2
    )

    signal = signal + transient

    recovery_start = min(center + width, length - 1)
    recovery_end = min(center + 3 * width, length)

    if recovery_start < recovery_end:
        signal[recovery_start:recovery_end] -= 0.15

    return signal


def generate_dataset(n_samples_per_class=100, length=200, noise_level=0.05, random_state=42):
    """
    Generate a labeled dataset of synthetic CSI-like signals.

    The dataset contains two classes:

    - Class 0: normal activity
    - Class 1: fall-like event

    Parameters
    ----------
    n_samples_per_class : int, default=100
        Number of synthetic samples to generate for each class.

    length : int, default=200
        Number of time samples in each signal.

    noise_level : float, default=0.05
        Standard deviation of Gaussian noise added to each signal.

    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    X : numpy.ndarray of shape (2 * n_samples_per_class, length)
        Synthetic CSI-like time-series signals.

    y : numpy.ndarray of shape (2 * n_samples_per_class,)
        Class labels.
        0 = normal activity
        1 = fall-like event

    Notes
    -----
    This dataset is synthetic and should be used only to demonstrate the
    signal-processing and machine learning workflow.
    """
    if n_samples_per_class <= 0:
        raise ValueError("n_samples_per_class must be a positive integer.")

    if length <= 0:
        raise ValueError("length must be a positive integer.")

    if noise_level < 0:
        raise ValueError("noise_level must be non-negative.")

    rng = np.random.default_rng(random_state)

    signals = []
    labels = []

    for _ in range(n_samples_per_class):
        seed = rng.integers(0, 1_000_000)
        signals.append(
            generate_normal_signal(
                length=length,
                noise_level=noise_level,
                random_state=seed
            )
        )
        labels.append(0)

    for _ in range(n_samples_per_class):
        seed = rng.integers(0, 1_000_000)
        signals.append(
            generate_fall_like_signal(
                length=length,
                noise_level=noise_level,
                random_state=seed
            )
        )
        labels.append(1)

    X = np.array(signals)
    y = np.array(labels)

    return X, y
