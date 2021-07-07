.. -*- mode: rst -*-

lightning
==========

lightning is an ongoing project to implement and research large-scale
algorithms for kernel-based classification and regression in Python/Cython.

Dependencies
============

The required dependencies to build the software are Python >= 2.6,
setuptools, Numpy >= 1.3, SciPy >= 0.7, scikit-learn (git version), Cython >= 0.15.1
and a working C/C++ compiler.

To run the tests you will also need nose >= 0.10.

Install
=======

First run::

  make cython

Then to install in your home directory, use::

  python setup.py install --home

To install for all users on Unix/Linux::

  python setup.py build
  sudo python setup.py install


