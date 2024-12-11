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



