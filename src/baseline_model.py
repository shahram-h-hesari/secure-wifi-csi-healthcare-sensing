"""
baseline_model.py

Baseline ML classifier training and evaluation for CSI fall detection.
Uses scikit-learn for beginner-friendly, interpretable baseline models.
Designed to demonstrate the ML workflow on synthetic CSI-like data.

NOTE: Results produced by this module are based on SYNTHETIC data only
and do not represent real-world or clinical fall detection performance.

Part of the wifi-csi-fall-detection research prototype.
Author: Shahram H. Hesari
Portland State University
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def train_baseline_classifier(X_train, y_train):
    """
    Train a simple baseline Random Forest classifier.

    Random Forest is a beginner-friendly ensemble method that is
    easy to use and interpret. It is used here as a starting point
    for the baseline ML workflow.

    NOTE: This classifier is trained on synthetic data only.
    Results should not be interpreted as clinical performance.

    Parameters
    ----------
    X_train : numpy.ndarray
        2D array of shape (n_samples, n_features) containing
        the feature vectors for training.
    y_train : numpy.ndarray
        1D array of shape (n_samples,) containing the class labels
        for training (0 = normal activity, 1 = fall-like event).

    Returns
    -------
    model : RandomForestClassifier
        Trained scikit-learn Random Forest classifier object.
    """
    # Create a Random Forest classifier
    # n_estimators=50: use 50 decision trees (enough for this small dataset)
    # random_state=42: set seed for reproducibility
    model = RandomForestClassifier(n_estimators=50, random_state=42)

    # Train the model on the training data
    model.fit(X_train, y_train)

    return model


def evaluate_classifier(model, X_test, y_test):
    """
    Evaluate a trained classifier on test data.

    Computes accuracy score and confusion matrix.

    NOTE: These metrics are based on synthetic test data only.
    High accuracy here does not imply real-world fall detection capability.

    Parameters
    ----------
    model : scikit-learn classifier
        A trained classifier object with a predict() method.
    X_test : numpy.ndarray
        2D array of shape (n_samples, n_features) containing
        the feature vectors for testing.
    y_test : numpy.ndarray
        1D array of shape (n_samples,) containing the true class labels
        for the test set.

    Returns
    -------
    accuracy : float
        Fraction of correctly classified test samples (between 0 and 1).
    cm : numpy.ndarray
        Confusion matrix of shape (n_classes, n_classes).
        Rows represent true classes, columns represent predicted classes.
    """
    # Generate predictions on the test data
    y_pred = model.predict(X_test)

    # Compute accuracy: fraction of correct predictions
    accuracy = accuracy_score(y_test, y_pred)

    # Compute confusion matrix
    # cm[0,0] = true normal classified as normal (true negative)
    # cm[0,1] = true normal classified as fall (false positive)
    # cm[1,0] = true fall classified as normal (false negative / missed fall)
    # cm[1,1] = true fall classified as fall (true positive)
    cm = confusion_matrix(y_test, y_pred)

    return accuracy, cm
