"""
simulate_csi.py

Functions to generate synthetic CSI-like time-series signals.

NOTE: All data produced here is SYNTHETIC and SIMULATED.
It does not represent real WiFi channel measurements,
patient data, or clinical recordings.

Part of the wifi-csi-fall-detection research prototype.
"""

import numpy as np


def generate_normal_signal(n_samples=200, n_subcarriers=30, seed=None):
    """
    Generate a synthetic CSI-like signal representing normal activity.

    Simulates a relatively stable channel with low-amplitude,
    slow variation -- representing a person at rest or walking normally.

    Parameters
    ----------
    n_samples : int
        Number of time steps (default: 200)
    n_subcarriers : int
        Number of OFDM-like subcarrier channels (default: 30)
    seed : int or None
        Random seed for reproducibility

    Returns
    -------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Synthetic CSI amplitude array
    """
    rng = np.random.default_rng(seed)

    # Base signal: slow sinusoidal variation + small Gaussian noise
    t = np.linspace(0, 4 * np.pi, n_samples)
    base = 0.5 * np.sin(t) + 1.0  # Slow oscillation around 1.0

    # Expand across subcarriers with small per-subcarrier variation
    signal = np.outer(base, np.ones(n_subcarriers))
    signal += rng.normal(loc=0.0, scale=0.05, size=signal.shape)

    return signal


def generate_fall_signal(n_samples=200, n_subcarriers=30, fall_start=80, seed=None):
    """
    Generate a synthetic CSI-like signal representing a fall-like event.

    Simulates a normal-looking signal that transitions into a
    high-amplitude, high-variance burst (representing the fall)
    followed by a low-activity resting state.

    Parameters
    ----------
    n_samples : int
        Number of time steps (default: 200)
    n_subcarriers : int
        Number of OFDM-like subcarrier channels (default: 30)
    fall_start : int
        Time index where the fall-like burst begins (default: 80)
    seed : int or None
        Random seed for reproducibility

    Returns
    -------
    signal : np.ndarray of shape (n_samples, n_subcarriers)
        Synthetic CSI amplitude array with embedded fall-like event
    """
    rng = np.random.default_rng(seed)

    t = np.linspace(0, 4 * np.pi, n_samples)
    base = 0.5 * np.sin(t) + 1.0  # Normal pre-fall baseline

    signal = np.outer(base, np.ones(n_subcarriers))
    signal += rng.normal(loc=0.0, scale=0.05, size=signal.shape)

    # Inject fall-like burst: high amplitude spike over ~20 samples
    fall_end = min(fall_start + 20, n_samples)
    burst = rng.normal(loc=3.5, scale=0.6, size=(fall_end - fall_start, n_subcarriers))
    signal[fall_start:fall_end, :] = burst

    # Post-fall: low amplitude (person on ground)
    if fall_end < n_samples:
        post_fall = rng.normal(loc=0.2, scale=0.05, size=(n_samples - fall_end, n_subcarriers))
        signal[fall_end:, :] = post_fall

    return signal


def generate_dataset(n_normal=50, n_fall=50, n_samples=200, n_subcarriers=30, seed=42):
    """
    Generate a labeled synthetic dataset with normal and fall-like samples.

    Parameters
    ----------
    n_normal : int
        Number of normal activity samples (default: 50)
    n_fall : int
        Number of fall-like event samples (default: 50)
    n_samples : int
        Length of each time-series sample (default: 200)
    n_subcarriers : int
        Number of simulated subcarrier channels (default: 30)
    seed : int
        Base random seed for reproducibility

    Returns
    -------
    X : list of np.ndarray
        List of signal arrays, each of shape (n_samples, n_subcarriers)
    y : list of int
        Labels: 0 = normal activity, 1 = fall-like event
    """
    X = []
    y = []

    for i in range(n_normal):
        sig = generate_normal_signal(
            n_samples=n_samples, n_subcarriers=n_subcarriers, seed=seed + i
        )
        X.append(sig)
        y.append(0)  # Label: normal

    for i in range(n_fall):
        sig = generate_fall_signal(
            n_samples=n_samples, n_subcarriers=n_subcarriers, seed=seed + 100 + i
        )
        X.append(sig)
        y.append(1)  # Label: fall

    return X, y
