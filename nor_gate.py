# -*- coding: utf-8 -*-
"""NOR_gate

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6VVM-CVAbroPYam9qYw4V5QxgsJVeLR
"""

import numpy as np
import pandas as pd
x1 = [0,1]
x2 = [[0,0],[0,1],[1,0],[1,1]]
gates = {}
gates['X'] = x2
def activation(y_hat):
    if(y_hat>=0):
        return 1
    else:
        return 0
def perceptron(x,w,b):
    y = []
    for x_hat in x:
        xw = np.dot(x_hat,w) + b
        y.append(activation(xw))
    return y
def NOT(x):
    w = [-1]
    b = 0
    # print(x)
    return perceptron(x,w,b)
def NOR(x):
    w = [1,1]
    b = -1
    # print(x)
    return NOT(perceptron(x,w,b))
nor = NOR(x2)
gates['NOR'] = nor
print('NOR', nor)

data = pd.DataFrame(gates)
print(data)

