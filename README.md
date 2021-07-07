LaSVM Implementation
====================


Code adapted from py2 to py3 from https://github.com/scikit-learn-contrib/lightning (checkpoint 6594fd8bdfba3cc808b3852cf380125e7e9df03e). The code not corresponding to LaSVM was removed. It is written in Python/Cython.

All credits to the original implementation by Mathieu Blondel (mathieu@mblondel.org).

Dependencies
============

TODO: Check minimum dependency requirements (These requirements are from the original py2 implementation)

The required dependencies to build the software are Python >= 3,
setuptools, Numpy >= 1.3, SciPy >= 0.7, scikit-learn (git version), Cython >= 0.15.1
and a working C/C++ compiler.

To run the tests you will also need nose >= 0.10.

Install
=======

First run:

```
make
```

Then to install in the current python interpreter:

```
python setup.py install
```