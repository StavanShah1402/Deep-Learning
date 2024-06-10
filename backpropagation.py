# -*- coding: utf-8 -*-
"""backpropagation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6VVM-CVAbroPYam9qYw4V5QxgsJVeLR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

d = load_iris()
X = d.data
df = pd.DataFrame(X)
df.shape

df.columns = ['X1', 'X2', 'X3', 'X4']
df.head()

Y = d.target
Y = pd.get_dummies(Y).values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

X_train.shape

def activation(_in):
    return 1 / (1 + np.exp(-_in))
def error(y, y_pred):
    return np.mean((y - y_pred)**2)

def accuracy(y, y_pred):
    acc = 0
    for i in range(len(y)):
        if np.argmax(y[i]) == np.argmax(y_pred[i]):
            acc += 1
    
    return acc / len(y)

def backpropogation(X_train, Y_train, alpha = 1, n_epochs = 300):
    v = np.random.normal(size = (4,2))
    w = np.random.normal(size = (2,3))
    err = []
    acc = []
    for _ in range(n_epochs):
        # FORWARD PASS
        Z_in = np.dot(X_train, v)
        Z_hat = activation(Z_in)

        Y_in = np.dot(Z_hat, w)
        Y_pred = activation(Y_in)

        err.append(error(Y_train, Y_pred))
        acc.append(accuracy(Y_train, Y_pred))

        # BACKWARD PASS
        dy = -2 * (Y_train - Y_pred) * Y_pred * (1 - Y_pred)
        dw = np.dot(np.transpose(Z_hat), dy)
        w += (-alpha * dw)

        dz = -2 * np.dot(dy, np.transpose(w)) * Z_hat * (1 - Z_hat)
        dv = np.dot(np.transpose(X_train), dz)
        v += (-alpha * dv)

    return v, w, err, acc

n = 300
v, w, errors, acc = backpropogation(X_train, Y_train, 1, n)

print(f"AT START, ERROR = {round(errors[0],3)} AND ACCURACY = {100*round(acc[0],3)}")
print(f"AT END, ERROR = {round(errors[-1],3)} AND ACCURACY = {100*round(acc[-1],3)}")

plt.figure(figsize=(10,7))
plt.plot(list(range(n)), errors)
plt.title("ERRORS VS EPOCHS")
plt.show()

plt.figure(figsize=(10,7))
plt.plot(list(range(n)), acc)
plt.title("ACCURACY VS EPOCHS")
plt.show()

def backpropagation_test(X_test, y_test, weights):
    v = weights[0]
    w = weights[1]
    
    Zin = np.dot(X_test, v)
    z_hat = activation(Zin)

    Yin = np.dot(z_hat, w)
    y_hat = activation(Yin)
    
    errors = error(y_test, y_hat)
    acc = accuracy(y_test, y_hat)
    print(f"ERROR = {round(errors,3)} AND ACCURACY = {100*round(acc,3)}")

backpropagation_test(X_test, Y_test, [v, w])