# numpy实现的XOR门

import numpy as np
# dot 用于计算两个数组的点积。
# 如果第一个参数是二维数组，第二个参数是一维数组，它将执行矩阵和向量的乘法。
# 如果两个参数都是二维数组，它将执行矩阵乘法。
from numpy import random, dot, exp

# 输入层
x = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])

# 输出层(标签)
y_ = np.array([[0, 1, 1, 0], [0, 1, 1, 0]])

# 随机初始化参数
W1 = np.array([[1, 2],
               [3, 4.0]])
W2 = np.array([[1, 2],
               [3, 4.0]])
W3 = np.array([[1, 2],
               [3, 4.0]])

"""
# 这个矩阵是通过将一个 2x2 的随机矩阵乘以 2 得到的
W1 = 2*random.random((2, 2))
W2 = 2*random.random((2, 2))
W3 = 2*random.random((2, 2))
"""

yita = 0.1  # 学习率

# 激活函数(Sigmoid)及其导数
def sigmoid(z):
    return 1/(1+exp(-z))

def d_sigmoid(a):
    return a*(1-a)

# 训练过程
epochs = 50000

for i in range(epochs):
    # 正向计算
    z1 = dot(W1, x)
    a1 = sigmoid(z1)
    z2 = dot(W2, a1)
    a2 = sigmoid(z2)
    z3 = dot(W3, a2)
    y = a3 = sigmoid(z3)

    # 代价(损失)函数 np.square 是 NumPy 库中的一个函数，用于计算输入数组中每个元素的平方。
    C = np.mean(np.square(y - y_)) # sum
    if i % 5000 == 0:
        print("Cost:", C)

    # 反向传播
    dL_a3 = 2 * (y - y_)
    dL_z3 = dL_a3 * d_sigmoid(a3)
    dL_W3 = dot(dL_z3, a2.T)
    dL_z2 = dot(W3.T, dL_z3) * d_sigmoid(a2)
    dL_W2 = dot(dL_z2, a1.T)
    dL_z1 = dot(W2.T, dL_z2) * d_sigmoid(a1)
    dL_W1 = dot(dL_z1, x.T)

    # 梯度下降
    W3 -= yita*dL_W3
    W2 -= yita*dL_W2
    W1 -= yita*dL_W1



