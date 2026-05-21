"""
baseline_model.py

Baseline ML classifier training and evaluation for CSI fall detection.

Uses scikit-learn for beginner-friendly, interpretable baseline models.
Designed to demonstrate the ML workflow on synthetic CSI-like data.

NOTE: Results produced by this module are based on SYNTHETIC data only
and do not represent real-world or clinical fall detection performance.

Part of the wifi-csi-fall-detection research prototype.
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def train_random_forest(X_train, y_train, n_estimators=50, random_state=42):
    """
    Train a Random Forest classifier on the training set.

    Random Forest is an ensemble method that is easy to use and
    provides reasonable baseline results without heavy tuning.

    Parameters
    ----------
    X_train : np.ndarray of shape (n_samples, n_features)
        Feature matrix for training
    y_train : array-like of shape (n_samples,)
        Training labels (0 = normal, 1 = fall)
    n_estimators : int
        Number of trees in the forest (default: 50)
    random_state : int
        Random seed for reproducibility

    Returns
    -------
    model : trained RandomForestClassifier
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    return model


def train_logistic_regression(X_train, y_train, random_state=42, max_iter=1000):
    """
    Train a Logistic Regression classifier on the training set.

    Logistic Regression is a simple linear baseline model that is
    interpretable and fast to train.

    Parameters
    ----------
    X_train : np.ndarray of shape (n_samples, n_features)
        Feature matrix for training
    y_train : array-like of shape (n_samples,)
        Training labels (0 = normal, 1 = fall)
    random_state : int
        Random seed for reproducibility
    max_iter : int
        Maximum iterations for solver convergence (default: 1000)

    Returns
    -------
    model : trained LogisticRegression
    """
    model = LogisticRegression(
        random_state=random_state,
        max_iter=max_iter
    )
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, label_names=None):
    """
    Evaluate a trained classifier on the test set.

    Prints accuracy, classification report, and confusion matrix.

    NOTE: All results reflect SYNTHETIC data only.
    Do not interpret these as real-world or clinical performance metrics.

    Parameters
    ----------
    model : trained scikit-learn classifier
    X_test : np.ndarray of shape (n_samples, n_features)
        Test feature matrix
    y_test : array-like of shape (n_samples,)
        True test labels
    label_names : list of str or None
        Class names for display (default: ['Normal', 'Fall'])

    Returns
    -------
    results : dict
        Dictionary with accuracy, confusion_matrix, and y_pred
    """
    if label_names is None:
        label_names = ['Normal', 'Fall']

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=label_names)

    print("=" * 50)
    print("Evaluation Results (SYNTHETIC DATA ONLY)")
    print("=" * 50)
    print(f"Accuracy: {acc:.4f}")
    print()
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(cm)
    print("=" * 50)
    print("NOTE: These results are from synthetic simulation only.")
    print("They do not represent real-world or clinical performance.")

    results = {
        'accuracy': acc,
        'confusion_matrix': cm,
        'y_pred': y_pred,
    }
    return results


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split feature matrix and labels into train and test sets.

    Parameters
    ----------
    X : np.ndarray of shape (n_samples, n_features)
    y : array-like of shape (n_samples,)
    test_size : float
        Fraction of data for testing (default: 0.2)
    random_state : int
        Random seed

    Returns
    -------
    X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
