"""
clinical_metrics.py

Clinical-safety-aware evaluation utilities for the WiFi CSI fall detection
research prototype.

This module extends conventional ML metrics with healthcare-relevant safety
metrics including missed fall count, false alarm count, missed fall rate,
false alarm rate, alarm fatigue indicator, simulated detection delay, and
a full clinical-safety summary.

IMPORTANT:
All metrics in this module are computed from synthetic CSI-like prototype
outputs only. This repository does not use real patient data, real clinical
data, or validated WiFi CSI measurements. No clinical validation is claimed.
Metrics are intended only to demonstrate the clinical-safety evaluation
framework.

Part of the wifi-csi-fall-detection research prototype.

Author: Shahram H. Hesari
PhD Student, Electrical and Computer Engineering
Portland State University
"""

import os
import numpy as np
import pandas as pd

# Label constants
LABEL_NORMAL = 0
LABEL_FALL = 1

# Alarm fatigue thresholds (illustrative, not from clinical guidelines)
_FATIGUE_LOW_THRESHOLD = 0.05
_FATIGUE_MODERATE_THRESHOLD = 0.15


def compute_missed_falls(y_true, y_pred):
    """
    Compute the number of missed fall-like events (false negatives).

    A missed fall occurs when the true label is 1 (fall-like event) but
    the model predicts 0 (normal activity).

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels. 1 = fall-like event, 0 = normal activity.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.

    Returns
    -------
    missed_falls : int
        Number of fall-like events that were not detected.

    Notes
    -----
    Computed from synthetic prototype labels only. Not a clinical metric.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return int(np.sum((y_true == LABEL_FALL) & (y_pred == LABEL_NORMAL)))


def compute_false_alarms(y_true, y_pred):
    """
    Compute the number of false alarms (false positives).

    A false alarm occurs when the true label is 0 (normal activity) but
    the model predicts 1 (fall-like event).

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.

    Returns
    -------
    false_alarms : int
        Number of normal events incorrectly predicted as fall-like events.

    Notes
    -----
    Computed from synthetic prototype labels only. Not a clinical metric.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return int(np.sum((y_true == LABEL_NORMAL) & (y_pred == LABEL_FALL)))


def compute_missed_fall_rate(y_true, y_pred):
    """
    Compute the missed fall rate (false negative rate for fall class).

    missed_fall_rate = missed_falls / total_true_fall_events

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.

    Returns
    -------
    rate : float
        Fraction of true fall-like events that were missed.
        Returns 0.0 if there are no true fall-like events.

    Notes
    -----
    Computed from synthetic prototype labels only. Not a clinical metric.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    total_falls = int(np.sum(y_true == LABEL_FALL))
    if total_falls == 0:
        return 0.0
    missed = compute_missed_falls(y_true, y_pred)
    return missed / total_falls


def compute_false_alarm_rate(y_true, y_pred):
    """
    Compute the false alarm rate (false positive rate for normal class).

    false_alarm_rate = false_alarms / total_true_normal_events

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.

    Returns
    -------
    rate : float
        Fraction of true normal events incorrectly flagged as fall-like.
        Returns 0.0 if there are no true normal events.

    Notes
    -----
    Computed from synthetic prototype labels only. Not a clinical metric.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    total_normal = int(np.sum(y_true == LABEL_NORMAL))
    if total_normal == 0:
        return 0.0
    false_alarms = compute_false_alarms(y_true, y_pred)
    return false_alarms / total_normal


def compute_alarm_fatigue_indicator(y_true, y_pred):
    """
    Compute a simple alarm fatigue indicator based on the false alarm rate.

    This is a categorical prototype indicator. High false alarm rates may
    contribute to alarm fatigue in caregivers over time, reducing system
    trustworthiness even when true fall detection is accurate.

    Categories:
      - 'low'      : false_alarm_rate < 0.05
      - 'moderate' : 0.05 <= false_alarm_rate < 0.15
      - 'high'     : false_alarm_rate >= 0.15

    Thresholds are illustrative and are not derived from clinical guidelines.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.

    Returns
    -------
    indicator : str
        One of 'low', 'moderate', or 'high'.

    Notes
    -----
    Computed from synthetic prototype labels only. Not a clinical metric.
    Thresholds are for demonstration purposes only.
    """
    far = compute_false_alarm_rate(y_true, y_pred)
    if far < _FATIGUE_LOW_THRESHOLD:
        return "low"
    elif far < _FATIGUE_MODERATE_THRESHOLD:
        return "moderate"
    else:
        return "high"


def compute_detection_delay_summary(delay_values):
    """
    Summarize simulated detection delay values for correctly detected falls.

    In this prototype, detection delay values are simulated or estimated
    from synthetic data. No real hardware timestamps are used.

    Parameters
    ----------
    delay_values : array-like of shape (n_detected_falls,)
        Simulated delay values (e.g., in samples or time units) for each
        correctly detected fall-like event.

    Returns
    -------
    summary : dict
        Dictionary with keys:
          - count: number of detected falls with delay data
          - mean_delay: mean detection delay
          - median_delay: median detection delay
          - min_delay: minimum detection delay
          - max_delay: maximum detection delay
          - std_delay: standard deviation of detection delay

    Notes
    -----
    Delay values are simulated from synthetic data. Not based on real
    hardware measurements or clinical timing.
    """
    delay_values = np.asarray(delay_values, dtype=float)
    if delay_values.size == 0:
        return {
            "count": 0,
            "mean_delay": None,
            "median_delay": None,
            "min_delay": None,
            "max_delay": None,
            "std_delay": None,
        }
    return {
        "count": int(delay_values.size),
        "mean_delay": float(np.mean(delay_values)),
        "median_delay": float(np.median(delay_values)),
        "min_delay": float(np.min(delay_values)),
        "max_delay": float(np.max(delay_values)),
        "std_delay": float(np.std(delay_values)),
    }


def summarize_clinical_safety_metrics(
    y_true,
    y_pred,
    delay_values=None,
    random_state=42
):
    """
    Compute and summarize all clinical-safety-aware metrics in one call.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True class labels. 1 = fall-like event, 0 = normal activity.
    y_pred : array-like of shape (n_samples,)
        Predicted class labels.
    delay_values : array-like or None, default=None
        Optional array of simulated detection delay values for correctly
        detected fall-like events. If None, delay values are simulated
        from a uniform distribution for demonstration purposes.
    random_state : int, default=42
        Random seed for delay simulation when delay_values is None.

    Returns
    -------
    summary : dict
        Dictionary containing:
          - total_samples: total number of test samples
          - total_true_falls: number of true fall-like events
          - total_true_normal: number of true normal events
          - missed_falls: count of undetected falls
          - false_alarms: count of false fall detections
          - missed_fall_rate: fraction of falls missed
          - false_alarm_rate: fraction of normal events misclassified
          - alarm_fatigue_indicator: 'low', 'moderate', or 'high'
          - delay_summary: detection delay statistics dict
          - note: disclaimer string

    Notes
    -----
    All metrics are computed from synthetic CSI-like prototype data.
    No clinical validation is claimed.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Compute counts
    total_true_falls = int(np.sum(y_true == LABEL_FALL))
    total_true_normal = int(np.sum(y_true == LABEL_NORMAL))
    true_positives = int(np.sum((y_true == LABEL_FALL) & (y_pred == LABEL_FALL)))

    # Simulate detection delay if not provided
    if delay_values is None:
        rng = np.random.default_rng(random_state)
        if true_positives > 0:
            delay_values = rng.uniform(low=1.0, high=15.0, size=true_positives)
        else:
            delay_values = np.array([])

    missed = compute_missed_falls(y_true, y_pred)
    false_alm = compute_false_alarms(y_true, y_pred)
    mfr = compute_missed_fall_rate(y_true, y_pred)
    far = compute_false_alarm_rate(y_true, y_pred)
    fatigue = compute_alarm_fatigue_indicator(y_true, y_pred)
    delay_summary = compute_detection_delay_summary(delay_values)

    return {
        "note": (
            "SYNTHETIC PROTOTYPE METRICS ONLY. "
            "Not clinical validation. Not real-world fall detection performance."
        ),
        "total_samples": int(y_true.size),
        "total_true_falls": total_true_falls,
        "total_true_normal": total_true_normal,
        "missed_falls": missed,
        "false_alarms": false_alm,
        "missed_fall_rate": round(mfr, 4),
        "false_alarm_rate": round(far, 4),
        "alarm_fatigue_indicator": fatigue,
        "delay_summary": delay_summary,
    }
