import numpy as np
import scipy.sparse as sp

from numpy.testing import assert_array_equal, assert_array_almost_equal, \
                          assert_almost_equal
from nose.tools import assert_raises, assert_true, assert_equal

from sklearn.datasets import make_classification
import unittest
from lasvm.lasvm import LaSVM

bin_dense, bin_target = make_classification(n_samples=200, n_features=100,
                                            n_informative=5,
                                            n_classes=2, random_state=0)
bin_sparse = sp.csr_matrix(bin_dense)

mult_dense, mult_target = make_classification(n_samples=300, n_features=100,
                                              n_informative=5,
                                              n_classes=3, random_state=0)
mult_sparse = sp.csr_matrix(mult_dense)


def test_fit_linear_binary():
    for selection, exp in (("cyclic", 1.0),
                           ("active", 1.0),
                           ("loss", 1.0)):
        clf = LaSVM(random_state=0, max_iter=2, kernel="linear",
                    selection=selection)
        clf.fit(bin_dense, bin_target)
        acc = clf.score(bin_dense, bin_target)
        assert_almost_equal(acc, exp)
        print(acc, exp)


def test_fit_rbf_binary():
    for selection in ("cyclic", "active", "loss"):
        clf = LaSVM(random_state=0, max_iter=2, kernel="rbf",
                    selection=selection)
        clf.fit(bin_dense, bin_target)
        acc = clf.score(bin_dense, bin_target)
        assert_almost_equal(acc, 1.0)


def test_fit_rbf_multi():
    clf = LaSVM(kernel="rbf", gamma=0.1, random_state=0)
    clf.fit(mult_dense, mult_target)
    y_pred = clf.predict(mult_dense)
    acc = np.mean(y_pred == mult_target)
    assert_almost_equal(acc, 1.0)


def test_warm_start():
    for selection in ("cyclic", "active", "loss"):
        clf = LaSVM(random_state=0, max_iter=2, kernel="rbf", warm_start=True,
                    selection=selection)
        clf.C = 0.5
        clf.fit(bin_dense, bin_target)
        acc = clf.score(bin_dense, bin_target)
        assert_almost_equal(acc, 1.0, 1)

        clf.C = 0.6
        clf.fit(bin_dense, bin_target)
        acc = clf.score(bin_dense, bin_target)
        assert_almost_equal(acc, 1.0)


def test_n_components():
    clf = LaSVM(random_state=0, max_iter=2, kernel="rbf", finish_step=True,
                termination="n_components", n_components=30)
    clf.fit(bin_dense, bin_target)
    assert_equal(clf.n_nonzero(), 30)


if __name__ == "__main__":
     test_fit_linear_binary()
     test_fit_rbf_multi()
     test_n_components()
