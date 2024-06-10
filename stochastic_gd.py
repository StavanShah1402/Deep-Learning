# -*- coding: utf-8 -*-
"""Stochastic_GD

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6VVM-CVAbroPYam9qYw4V5QxgsJVeLR
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def sigmoid(Y_in):
    return 1 / (1 + np.exp(-Y_in))
def find_Yhat(X, w, b):
    if type(X) in [type([1]), type((1,2))]:
        Y_in = np.dot(X, w) + b
    else:
        Y_in = X * w + b

    return sigmoid(Y_in)
def delta_w(X, Y_true, Y_pred):
  return -2 * (Y_true - Y_pred) * Y_pred * (1 - Y_pred) * X
def delta_b(Y_true, Y_pred):
  return -2 * (Y_true - Y_pred) * Y_pred * (1 - Y_pred)


X = [0.5, 2.5]
Y = [0.2, 0.9]
n_epochs = 300
df = pd.DataFrame([(x, y) for x, y in zip(X, Y)], columns = ['X', 'Y'])
df.head()

def stochastic_gradient_descent(X, Y, noofepochs = 300):
    w = -2; alpha = 1; b = -2;

    # LIST FOR ALL EPOCHS
    error_mega_list = []
    weights_mega_list = []
    bias_mega_list = []
        
    for i in range(noofepochs):
        # LIST FOR EACH EPOCH
        error_list = []

        for x, y in zip(X, Y):
            Y_hat = find_Yhat(x, w, b)
            error_list.append((y - Y_hat) ** 2)

            dw = delta_w(x, y, Y_hat)
            db = delta_b(y, Y_hat)
        
            w += (-alpha * dw)
            b += (-alpha * db)
        
        error_mega_list.append(error_list)
        weights_mega_list.append(w)
        bias_mega_list.append(b)
        
    return error_mega_list, weights_mega_list, bias_mega_list
errors_sgd, weights_sgd, biases_sgd = stochastic_gradient_descent(X, Y, n_epochs)
plt.title("WEIGHT VS EPOCHS")
epoch_range = [i for i in range(n_epochs)]
weight_range = [w for w in weights_sgd]
plt.plot(epoch_range, weight_range)
plt.xlabel('EPOCHS ')
plt.ylabel('WEIGHT')
plt.show()

