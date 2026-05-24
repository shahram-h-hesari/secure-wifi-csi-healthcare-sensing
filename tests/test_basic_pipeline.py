"""
test_basic_pipeline.py
======================
Basic pytest tests for the WiFi CSI Fall Detection Research Prototype.

IMPORTANT NOTE
--------------
All tests use synthetic CSI-like data only.
Passing these tests does not imply:
  - Clinical validation of fall detection
  - Real WiFi CSI hardware validation
  - Hardware deployment readiness
  - Medical-grade performance

These are simple sanity checks to verify that imports work,
data arrays have expected shapes, feature extraction produces
the expected output structure, and the classifier can fit and
predict on synthetic data.

Run with:
    pytest
    pytest -v

Phase: 10 - Testing and Verification
"""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Helper: generate a tiny synthetic CSI-like dataset
# ---------------------------------------------------------------------------

def make_synthetic_data(n_normal=50, n_fall=50, n_packets=40,
                         n_subcarriers=20, fall_strength=2.0,
                         noise_std=0.3, random_seed=99):
    """
    Generate a small synthetic dataset for testing purposes.

    Returns
    -------
    X : np.ndarray, shape (n_normal + n_fall, n_packets, n_subcarriers)
    y : np.ndarray, shape (n_normal + n_fall,)  -- 0=normal, 1=fall
    """
    rng = np.random.default_rng(random_seed)
    n_total = n_normal + n_fall
    base = rng.normal(loc=0.0, scale=1.0,
                      size=(n_total, n_packets, n_subcarriers))
    # Add a fall pulse to the last n_fall samples
    fall_start = n_packets // 3
    fall_end   = fall_start + n_packets // 5
    base[n_normal:, fall_start:fall_end, :] += fall_strength
    X = base + rng.normal(loc=0.0, scale=noise_std,
                           size=(n_total, n_packets, n_subcarriers))
    y = np.array([0] * n_normal + [1] * n_fall)
    return X, y


def extract_features_simple(X):
    """
    Extract simple statistical features for testing purposes.

    Returns
    -------
    features : np.ndarray, shape (n_samples, 7)
    feature_names : list of str
    """
    amp = np.abs(X)
    flat = amp.reshape(amp.shape[0], -1)
    feature_names = ['mean', 'std', 'energy', 'ptp', 'max', 'min', 'var']
    features = np.column_stack([
        flat.mean(axis=1),
        flat.std(axis=1),
        (flat ** 2).mean(axis=1),
        flat.max(axis=1) - flat.min(axis=1),
        flat.max(axis=1),
        flat.min(axis=1),
        flat.var(axis=1),
    ])
    return features, feature_names


# ---------------------------------------------------------------------------
# Import tests
# ---------------------------------------------------------------------------

class TestImports:
    """Verify that all required packages import without errors."""

    def test_import_numpy(self):
        import numpy
        assert numpy is not None

    def test_import_pandas(self):
        import pandas
        assert pandas is not None

    def test_import_scipy(self):
        import scipy
        assert scipy is not None

    def test_import_scipy_ndimage(self):
        from scipy.ndimage import uniform_filter1d, median_filter
        assert uniform_filter1d is not None
        assert median_filter is not None

    def test_import_sklearn(self):
        import sklearn
        assert sklearn is not None

    def test_import_sklearn_rf(self):
        from sklearn.ensemble import RandomForestClassifier
        assert RandomForestClassifier is not None

    def test_import_sklearn_metrics(self):
        from sklearn.metrics import accuracy_score, precision_score
        assert accuracy_score is not None

    def test_import_matplotlib(self):
        import matplotlib
        assert matplotlib is not None


# ---------------------------------------------------------------------------
# Synthetic data shape tests
# ---------------------------------------------------------------------------

class TestSyntheticDataShapes:
    """Verify that synthetic data arrays have expected dimensions."""

    def test_data_shape(self):
        """Synthetic dataset should have correct number of samples."""
        n_normal, n_fall = 50, 50
        X, y = make_synthetic_data(n_normal=n_normal, n_fall=n_fall,
                                    n_packets=40, n_subcarriers=20)
        assert X.shape == (100, 40, 20), f"Unexpected X shape: {X.shape}"
        assert y.shape == (100,), f"Unexpected y shape: {y.shape}"

    def test_label_counts(self):
        """Label array should have equal normal and fall samples."""
        X, y = make_synthetic_data(n_normal=50, n_fall=50)
        assert np.sum(y == 0) == 50, "Expected 50 normal samples"
        assert np.sum(y == 1) == 50, "Expected 50 fall samples"

    def test_data_is_float(self):
        """Synthetic data should be floating point."""
        X, y = make_synthetic_data()
        assert X.dtype in [np.float32, np.float64], \
            f"Expected float dtype, got {X.dtype}"

    def test_fall_samples_have_higher_amplitude(self):
        """Fall samples should have higher mean amplitude than normal."""
        X, y = make_synthetic_data(fall_strength=3.0)
        mean_normal = np.abs(X[y == 0]).mean()
        mean_fall   = np.abs(X[y == 1]).mean()
        assert mean_fall > mean_normal, \
            "Expected fall samples to have higher mean amplitude than normal"


# ---------------------------------------------------------------------------
# Feature extraction tests
# ---------------------------------------------------------------------------

class TestFeatureExtraction:
    """Verify that feature extraction returns correct structure."""

    def test_feature_shape(self):
        """Feature matrix should have shape (n_samples, 7)."""
        X, y = make_synthetic_data(n_normal=30, n_fall=30)
        features, names = extract_features_simple(X)
        assert features.shape == (60, 7), \
            f"Expected (60, 7), got {features.shape}"

    def test_feature_names(self):
        """Feature names should match expected list."""
        X, y = make_synthetic_data()
        _, names = extract_features_simple(X)
        expected = ['mean', 'std', 'energy', 'ptp', 'max', 'min', 'var']
        assert names == expected, f"Unexpected feature names: {names}"

    def test_features_are_finite(self):
        """All feature values should be finite (no NaN or Inf)."""
        X, y = make_synthetic_data()
        features, _ = extract_features_simple(X)
        assert np.all(np.isfinite(features)), \
            "Feature matrix contains NaN or Inf values"

    def test_energy_positive(self):
        """Energy feature (column 2) should be positive for all samples."""
        X, y = make_synthetic_data()
        features, _ = extract_features_simple(X)
        assert np.all(features[:, 2] >= 0), \
            "Energy feature should be non-negative"


# ---------------------------------------------------------------------------
# Classifier sanity tests
# ---------------------------------------------------------------------------

class TestBaselineClassifier:
    """Verify that a small classifier can fit and predict on synthetic data."""

    def test_classifier_fits_without_error(self):
        """RandomForestClassifier should fit on synthetic features."""
        from sklearn.ensemble import RandomForestClassifier
        X, y = make_synthetic_data(n_normal=60, n_fall=60)
        features, _ = extract_features_simple(X)
        clf = RandomForestClassifier(n_estimators=10, random_state=0)
        clf.fit(features, y)  # Should not raise

    def test_classifier_predicts_correct_shape(self):
        """Predictions should have same length as test set."""
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        X, y = make_synthetic_data(n_normal=60, n_fall=60)
        features, _ = extract_features_simple(X)
        X_tr, X_te, y_tr, y_te = train_test_split(
            features, y, test_size=0.25, random_state=0
        )
        clf = RandomForestClassifier(n_estimators=10, random_state=0)
        clf.fit(X_tr, y_tr)
        y_pred = clf.predict(X_te)
        assert y_pred.shape == y_te.shape, \
            f"Prediction shape {y_pred.shape} != label shape {y_te.shape}"

    def test_predictions_are_binary(self):
        """All predictions should be 0 or 1."""
        from sklearn.ensemble import RandomForestClassifier
        X, y = make_synthetic_data(n_normal=60, n_fall=60)
        features, _ = extract_features_simple(X)
        clf = RandomForestClassifier(n_estimators=10, random_state=0)
        clf.fit(features, y)
        y_pred = clf.predict(features)
        unique_preds = set(y_pred.tolist())
        assert unique_preds.issubset({0, 1}), \
            f"Unexpected prediction values: {unique_preds}"

    def test_accuracy_above_random_chance(self):
        """
        On well-separated synthetic data, accuracy should exceed 0.5.

        NOTE: This is a synthetic sanity check only. It does not validate
        real WiFi CSI performance or clinical fall-detection accuracy.
        """
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score
        X, y = make_synthetic_data(n_normal=100, n_fall=100,
                                    fall_strength=3.0)
        features, _ = extract_features_simple(X)
        X_tr, X_te, y_tr, y_te = train_test_split(
            features, y, test_size=0.3, random_state=42, stratify=y
        )
        clf = RandomForestClassifier(n_estimators=20, random_state=42)
        clf.fit(X_tr, y_tr)
        acc = accuracy_score(y_te, clf.predict(X_te))
        assert acc > 0.5, \
            f"Expected accuracy > 0.5 on synthetic data, got {acc:.4f}"
