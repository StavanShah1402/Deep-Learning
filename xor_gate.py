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
def OR(x):
    w = [1,1]
    b = -1
    # print(x)
    return perceptron(x,w,b)
def XOR(x):
    w1 = [-1,1]
    b = -1
    print(x)
    z1 = perceptron(x,w1,b)
    print(z1)

    w2 = [1,-1]
    z2 = perceptron(x,w2,b)
    print(z2)

    z = []
    for z1_hat, z2_hat in zip(z1,z2):
        z.append([z1_hat,z2_hat])
    print(z)    
    print(list(zip(z1,z2)))
    return OR(z) 
xor = XOR(x2)
gates['XOR'] = xor
print('XOR', xor)
data = pd.DataFrame(gates)
print(data)

