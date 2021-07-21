LaSVM Implementation
====================

LaSVM implementation written in Python/Cython following sklearn classifier API.


The code was extracted and adapted from py2 to py3 from https://github.com/scikit-learn-contrib/lightning (checkpoint 6594fd8).


Code example:

```python
import random

import numpy as np
from lasvm import LaSVM
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

random.seed(42)

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=42)

n_increments = 10
ids = list(range(len(X_train)))
random.shuffle(ids)
increment_groups = np.array_split(ids, n_increments)

scaler = StandardScaler()
scaler.fit(X_train[increment_groups[0]])

X_test_scaled = scaler.transform(X_test)

svm = LaSVM(random_state=42, warm_start=True, verbose=False)

previous_ids = []

for i, increment_ids in enumerate(increment_groups):
    increment_ids = list(np.ravel(increment_ids))
    
    X_increment = X_train[previous_ids + increment_ids]
    y_increment = y_train[previous_ids + increment_ids]
    
    previous_ids.extend(increment_ids)
    
    X_increment_scaled = scaler.transform(X_increment)
    svm.fit(X_increment_scaled, y_increment)
    score = f1_score(y_test, svm.predict(X_test_scaled))
    
    print("Iteration {}: score {:.2f}, chunk size {}".format(i, score, len(X_increment)))

```



Dependencies
============

TODO: Check minimum dependency requirements (These requirements are from the original py2 implementation)

The required dependencies to build the software are Python >= 3, numpy>=1.17.0 cython>=0.29, and a working C/C++ compiler.

To run the tests you will also need nose >= 0.10.

Install
=======

First run:

```
python setup.py build_ext -i
```

Then to install in the current python interpreter:

```
python setup.py install
```

Credits
=======
All credits to the original implementation by Mathieu Blondel (mathieu@mblondel.org).

References
==========

Bordes, A., Ertekin, S., Weston, J., Botton, L., & Cristianini, N. (2005). Fast kernel classifiers with online and active learning. Journal of Machine Learning Research, 6(9).