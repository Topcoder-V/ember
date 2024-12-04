# 代码有问题 误差太大

import numpy as np

# 使用 NumPy 数组代替列表
X = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1]
])

Y = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 1],
    [0, 0, 0]
])

# 初始化权重
w1 = np.zeros((3, 3))
w2 = np.zeros((3, 3))
w3 = np.zeros((3, 3))

# Sigmoid 函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def d_sigmoid(x):
    return x * (1 - x)

# 学习率
yita = 0.4

# 训练轮数
epochs = 50000
for p in range(epochs):
    C = 0
    for k in range(len(X)):
        y_hat = Y[k]
        a0 = x = X[k]

        # 第一层
        z1 = np.dot(w1[1:, 1:], x[1:])
        a1 = sigmoid(z1)

        # 第二层
        z2 = np.dot(w2[1:, 1:], a1)
        a2 = sigmoid(z2)

        # 第三层
        z3 = np.dot(w3[1:, 1:], a2)
        a3 = sigmoid(z3)

        C += np.sum((a3 - y_hat[1:])**2)

        # 反向传播
        e3 = 2 * (a3 - y_hat[1:])
        e2 = np.dot(e3, w3[1:, 1:]) * d_sigmoid(a2)
        e1 = np.dot(e2, w2[1:, 1:]) * d_sigmoid(a1)

        # 更新权重
        w1[1:, 1:] -= yita * np.outer(e1, a0[1:])
        w2[1:, 1:] -= yita * np.outer(e2, a1)
        w3[1:, 1:] -= yita * np.outer(e3, a2)

    if p % 5000 == 0:
        print('Total Cost: ', C)

# 应用神经网络
x = np.array([0, 1, 0])

z1 = np.dot(w1[1:, 1:], x[1:])
a1 = sigmoid(z1)

z2 = np.dot(w2[1:, 1:], a1)
a2 = sigmoid(z2)

z3 = np.dot(w3[1:, 1:], a2)
a3 = sigmoid(z3)

print(a3)
C = np.sum((a3 - 1)**2)
print('Loss = ', C)
