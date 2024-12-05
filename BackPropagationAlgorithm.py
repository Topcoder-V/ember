# 反向传播算法Back Propagation Algorithm

import math
import numpy as np


# 下标0均不用
# 输入层
X = [[0, 0, 0],
     [0, 0, 1],
     [0, 1, 0],
     [0, 1, 1]
    ]

# 输出层
Y = [[0, 0, 0],
     [0, 1, 1],
     [0, 1, 1],
     [0, 0, 0]
    ]

# 第一层
w1 = [[0, 0 ,0],
      [0, 1 ,2],
      [0, 3, 4]
     ]
z1 = [0, 1, 1]
a1 = [0, 1, 1]
e1 = [0, 1, 1]

# 第二层
w2 = [[0, 0 ,0],
      [0 ,1 ,2],
      [0, 3, 4]
     ]
z2 = [0, 1, 1]
a2 = [0, 1, 1]
e2 = [0, 1, 1]

# 第三层
w3 = [[0, 0 ,0],
      [0 ,1 ,2],
      [0, 3, 4]
     ]
z3 = [0, 1, 1]
y = a3 = [0, 1, 1]
e3 = [0, 1, 1]

# Sigmoid函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# def sigmoid(x):
#     return 1 / (1 + math.exp(-x))

def d_sigmoid(x):
    return x * (1 - x)

# 学习率
yita = 0.4

# 训练轮数
epochs = 50000
for p in range(epochs):
    C = 0
    for k in range(len(X)):
        y_hat  = Y[k]
        a0 = x = X[k]

        # 第一层
        # 注意：这里和理论讲解时的w命名有所区别，例如w12为从x2到x1的权重，但在代码中定义为w12为从x1到x2的权重
        z1[1] = x[1]*w1[1][1] + x[2]*w1[2][1]
        z1[2] = x[1]*w1[1][2] + x[2]*w1[2][2]

        a1[1] = sigmoid(z1[1])
        a1[2] = sigmoid(z1[2])

        # 第二层
        z2[1] = a1[1]*w2[1][1] + a1[2]*w2[2][1]
        z2[2] = a1[1]*w2[1][2] + a1[2]*w2[2][2]

        a2[1] = sigmoid(z2[1])
        a2[2] = sigmoid(z2[2])

        # 第三层
        z3[1] = a2[1]*w3[1][1] + a2[2]*w3[2][1]
        z3[2] = a2[1]*w3[1][2] + a2[2]*w3[2][2]

        a3[1] = sigmoid(z3[1])
        a3[2] = sigmoid(z3[2])

        # ** 是指数运算符，表示对操作符左边的数值进行操作符右边数值的幂运算。所以，**2 表示对左边的数值进行平方运算
        C += (a3[1] - y_hat[1])**2 + (a3[2] - y_hat[2])**2

        # 反向传播 利用第二个钻石通项公式
        # 第三层
        e3[1] = 2*(a3[1] - y_hat[1]) # 𝜕C/𝜕a3_1
        e3[2] = 2*(a3[2] - y_hat[2]) # 𝜕C/𝜕a3_2
        # 第二层
        # d_sigmoid 是指 Sigmoid 函数的导数. Sigmoid 函数的导数是其值的函数
        e2[1] = e3[1] * d_sigmoid(a3[1])*w3[1][1] + e3[2] * d_sigmoid(a3[2])*w3[1][2]
        e2[2] = e3[1] * d_sigmoid(a3[1])*w3[2][1] + e3[2] * d_sigmoid(a3[2])*w3[2][2]
        # 第一层
        e1[1] = e2[1] * d_sigmoid(a2[1])*w2[1][1] + e2[2] * d_sigmoid(a2[2])*w2[1][2]
        e1[2] = e2[1] * d_sigmoid(a2[1])*w2[2][1] + e2[2] * d_sigmoid(a2[2])*w2[2][2]

        # 更新权重 梯度下降
        # 更新权重 梯度下降
        for i in range(1, 3):
            for j in range(1, 3):
                w1[i][j] -= yita * (e1[j]*d_sigmoid(a1[j])*a0[i]) # 𝜕C / 𝜕w1_i_j
                w2[i][j] -= yita * (e2[j]*d_sigmoid(a2[j])*a1[i]) # 𝜕C / 𝜕w2_i_j
                w3[i][j] -= yita * (e3[j]*d_sigmoid(a3[j])*a2[i]) # 𝜕C / 𝜕w3_i_j

    if p % 5000 == 0:
        print('Total Cost: ', C)

# 应用神经网络
x[1] = 0
x[2] = 1

z1[1] = x[1]*w1[1][1] + x[2]*w1[2][1]
z1[2] = x[1]*w1[1][2] + x[2]*w1[2][2]

a1[1] = sigmoid(z1[1])
a1[2] = sigmoid(z1[2])


z2[1] = a1[1]*w2[1][1] + a1[2]*w2[2][1]
z2[2] = a1[1]*w2[1][2] + a1[2]*w2[2][2]

a2[1] = sigmoid(z2[1])
a2[2] = sigmoid(z2[2])

z3[1] = a2[1]*w3[1][1] + a2[2]*w3[2][1]
z3[2] = a2[1]*w3[1][2] + a2[2]*w3[2][2]

a3[1] = sigmoid(z3[1])
a3[2] = sigmoid(z3[2])


print(a3[1], ",", a3[2])
C = (a3[1] - 1)**2 + (a3[2] - 1)**2 # 为什么这里-1呢？
print('Loss = ', C)
