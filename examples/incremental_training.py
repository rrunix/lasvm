import random

import numpy as np
from lasvm.lasvm import LaSVM
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
