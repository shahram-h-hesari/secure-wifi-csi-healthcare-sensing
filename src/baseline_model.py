"""
baseline_model.py

Baseline machine learning utilities for the WiFi CSI fall detection
research prototype.

This module trains and evaluates a simple scikit-learn classifier using
features extracted from synthetic CSI-like time-series signals.

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

import os
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


def train_baseline_classifier(
    X_train,
    y_train,
    n_estimators=100,
    random_state=42
):
    """
    Train a Random Forest baseline classifier on the feature training set.

    Random Forest is used here as a beginner-friendly baseline model for
    demonstrating a binary classification workflow on synthetic data.
    It is not an optimized or clinically validated fall detection model.

    Parameters
    ----------
    X_train : array-like of shape (n_train_samples, n_features)
        Training feature matrix.
    y_train : array-like of shape (n_train_samples,)
        Training labels. 0 = normal activity, 1 = fall-like event.
    n_estimators : int, default=100
        Number of decision trees in the Random Forest.
    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    model : sklearn.ensemble.RandomForestClassifier
        Fitted classifier.

    Notes
    -----
    This model is trained on synthetic CSI-like data only.
    Its performance metrics should not be interpreted as real-world
    fall detection accuracy.
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    return model


def evaluate_classifier(model, X_test, y_test, class_names=None):
    """
    Evaluate a trained classifier on the test feature set.

    Computes accuracy, precision, recall, F1-score, and confusion matrix.
    All reported metrics are based on synthetic CSI-like test data.

    Parameters
    ----------
    model : fitted scikit-learn classifier
        Trained baseline classifier.
    X_test : array-like of shape (n_test_samples, n_features)
        Test feature matrix.
    y_test : array-like of shape (n_test_samples,)
        True test labels.
    class_names : list of str or None, default=None
        Class names for the classification report.
        If None, defaults to ["normal_activity", "fall_like_event"].

    Returns
    -------
    results : dict
        Dictionary with keys:
          - accuracy: float
          - precision: float (macro average)
          - recall: float (macro average)
          - f1_score: float (macro average)
          - confusion_matrix: numpy.ndarray
          - classification_report: str
          - y_pred: numpy.ndarray of predicted labels

    Notes
    -----
    All metrics are computed on synthetic CSI-like test data.
    They do not represent real-world fall detection performance.
    """
    if class_names is None:
        class_names = ["normal_activity", "fall_like_event"]

    y_pred = model.predict(X_test)

    results = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, average="macro", zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, average="macro", zero_division=0)),
        "f1_score": float(f1_score(y_test, y_pred, average="macro", zero_division=0)),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(
            y_test, y_pred, target_names=class_names, zero_division=0
        ),
        "y_pred": y_pred,
    }

    return results


def save_results_summary(
    results,
    output_path="results/baseline_metrics.json",
    note="Synthetic prototype metrics only. Not real-world fall detection performance."
):
    """
    Save baseline classifier metrics to a JSON file.

    Parameters
    ----------
    results : dict
        Results dictionary from evaluate_classifier(), containing
        accuracy, precision, recall, and f1_score.
    output_path : str, default="results/baseline_metrics.json"
        Path where the JSON summary file will be saved.
    note : str
        Disclaimer note to embed in the saved file.

    Returns
    -------
    None

    Notes
    -----
    Saved metrics are based on synthetic CSI-like data only.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    summary = {
        "note": note,
        "accuracy": results["accuracy"],
        "precision_macro": results["precision"],
        "recall_macro": results["recall"],
        "f1_macro": results["f1_score"],
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Results summary saved to {output_path}")
