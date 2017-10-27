import pytest
import numpy as np

from sklearn.datasets import make_regression

from cartesian import Symbolic
from cartesian.sklearn_api import _ensure_1d


@pytest.mark.parametrize("n_out", [1, 2])
def test_Symbolic_fit(n_out):
    x, y = make_regression(n_features=2, n_informative=1, n_targets=n_out)
    est = Symbolic(max_nfev=1, lambda_=1).fit(x, y)
    yhat = est.predict(x)
    assert yhat.shape == y.shape


def test_Symbolic_joblib():
    x, y = make_regression(n_features=2, n_informative=1, n_targets=1)
    yhat = Symbolic(n_jobs=-1, max_nfev=1, lambda_=1).fit(x, y).predict(x)
    assert yhat.shape == y.shape


def test__ensure_1d():
    assert _ensure_1d(1, 1) == np.ones(1)
    assert _ensure_1d(np.ones(1), 1) == np.ones(1)
