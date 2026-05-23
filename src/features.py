"""
features.py

Time-series and frequency-domain feature extraction utilities for synthetic
CSI-like signals in the WiFi CSI fall detection research prototype.

This module extracts simple statistical and spectral features from preprocessed
one-dimensional signals. These features are used as inputs to baseline ML models.

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
import pandas as pd


def extract_time_domain_features(signal):
    """
    Extract simple time-domain statistical features from a 1-D signal.

    Features extracted:
      - mean: arithmetic mean
      - std: standard deviation
      - variance: variance
      - energy: sum of squared sample values
      - ptp_range: peak-to-peak range (max - min)
      - max_value: maximum value
      - min_value: minimum value
      - abs_mean: mean of absolute values

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional preprocessed CSI-like signal.

    Returns
    -------
    features : dict
        Dictionary mapping feature name to feature value.

    Notes
    -----
    These features are intentionally simple and interpretable. They are designed
    for synthetic data demonstration only and have not been validated on real
    WiFi CSI measurements.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")
    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    return {
        "mean": float(np.mean(signal)),
        "std": float(np.std(signal)),
        "variance": float(np.var(signal)),
        "energy": float(np.sum(signal ** 2)),
        "ptp_range": float(np.ptp(signal)),
        "max_value": float(np.max(signal)),
        "min_value": float(np.min(signal)),
        "abs_mean": float(np.mean(np.abs(signal))),
    }


# Alias for backward compatibility
extract_basic_features = extract_time_domain_features


def extract_frequency_domain_features(signal, sample_rate=1.0):
    """
    Extract simple frequency-domain features from a 1-D signal.

    Uses the real FFT to compute spectral features:
      - dominant_freq: frequency bin with the highest power (excluding DC)
      - spectral_energy: total power in the spectrum
      - spectral_centroid: power-weighted mean frequency
      - spectral_std: power-weighted standard deviation of frequency

    Parameters
    ----------
    signal : array-like of shape (n_samples,)
        One-dimensional preprocessed CSI-like signal.
    sample_rate : float, default=1.0
        Sampling rate in Hz. Used to scale frequency values.
        For synthetic data, a default of 1.0 is used.

    Returns
    -------
    features : dict
        Dictionary mapping feature name to feature value.

    Notes
    -----
    These frequency features are computed on synthetic CSI-like signals.
    They have not been validated against real hardware WiFi CSI measurements.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("Input signal must be one-dimensional.")
    if signal.size == 0:
        raise ValueError("Input signal must not be empty.")

    n = len(signal)
    fft_vals = np.fft.rfft(signal)
    fft_power = np.abs(fft_vals) ** 2
    freqs = np.fft.rfftfreq(n, d=1.0 / sample_rate)

    # Exclude DC component (index 0) when finding dominant frequency
    if len(fft_power) > 1:
        dominant_idx = np.argmax(fft_power[1:]) + 1
    else:
        dominant_idx = 0

    dominant_freq = float(freqs[dominant_idx])
    spectral_energy = float(np.sum(fft_power))

    total_power = np.sum(fft_power)
    if total_power > 0:
        spectral_centroid = float(np.sum(freqs * fft_power) / total_power)
        spectral_std = float(
            np.sqrt(np.sum(fft_power * (freqs - spectral_centroid) ** 2) / total_power)
        )
    else:
        spectral_centroid = 0.0
        spectral_std = 0.0

    return {
        "dominant_freq": dominant_freq,
        "spectral_energy": spectral_energy,
        "spectral_centroid": spectral_centroid,
        "spectral_std": spectral_std,
    }


def extract_features_from_dataset(X, include_frequency=True, sample_rate=1.0):
    """
    Extract features from every signal in a dataset array.

    Applies both time-domain and optionally frequency-domain feature extraction
    to each signal in X and returns a pandas DataFrame.

    Parameters
    ----------
    X : numpy.ndarray of shape (n_samples, signal_length)
        Array of preprocessed synthetic CSI-like signals.
    include_frequency : bool, default=True
        Whether to include frequency-domain features.
    sample_rate : float, default=1.0
        Sampling rate passed to frequency-domain extraction.

    Returns
    -------
    feature_df : pandas.DataFrame of shape (n_samples, n_features)
        Feature table ready for use with scikit-learn classifiers.

    Notes
    -----
    Features are extracted from synthetic CSI-like signals and are
    intended only to demonstrate the prototype ML workflow.
    """
    X = np.asarray(X, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D array of shape (n_samples, signal_length).")

    rows = []
    for signal in X:
        feats = extract_time_domain_features(signal)
        if include_frequency:
            feats.update(
                extract_frequency_domain_features(signal, sample_rate=sample_rate)
            )
        rows.append(feats)

    return pd.DataFrame(rows)
