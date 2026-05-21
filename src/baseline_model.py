"""
baseline_model.py

Baseline machine learning utilities for the WiFi CSI fall detection research prototype.

This module trains and evaluates a simple scikit-learn classifier using features
extracted from synthetic CSI-like time-series signals.

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

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def train_baseline_classifier(X_train, y_train, n_estimators=50, random_state=42):
    """
    Train a simple baseline Random Forest classifier.

    Random Forest is used here as a beginner-friendly baseline model for
    demonstrating a basic machine learning workflow on synthetic CSI-like data.

    Parameters
    ----------
    X_train : array-like of shape (n_samples, n_features)
        Feature vectors used for training.

    y_train : array-like of shape (n_samples,)
        Training labels.
        Class 0 = normal activity
        Class 1 = fall-like event

    n_estimators : int, default=50
        Number of trees in the Random Forest.

    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    model : RandomForestClassifier
        Trained scikit-learn Random Forest classifier.
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model


def evaluate_classifier(model, X_test, y_test, target_names=None):
    """
    Evaluate a trained classifier on synthetic test data.

    This function computes accuracy, confusion matrix, and a text classification
    report. These metrics are useful for demonstrating the workflow, but they
    should not be interpreted as real-world or clinical fall detection results.

    Parameters
    ----------
    model : scikit-learn classifier
        A trained classifier object with a predict() method.

    X_test : array-like of shape (n_samples, n_features)
        Feature vectors used for testing.

    y_test : array-like of shape (n_samples,)
        True labels for the test set.
        Class 0 = normal activity
        Class 1 = fall-like event

    target_names : list of str, optional
        Human-readable class names for the classification report.

    Returns
    -------
    results : dict
        Dictionary containing:
        - accuracy : float
        - confusion_matrix : numpy.ndarray
        - classification_report : str
        - y_pred : array-like
    """
    if target_names is None:
        target_names = ["normal activity", "fall-like event"]

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(
        y_test,
        y_pred,
        target_names=target_names
    )

    results = {
        "accuracy": accuracy,
        "confusion_matrix": cm,
        "classification_report": report,
        "y_pred": y_pred,
    }

    return results
