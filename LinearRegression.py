# 线性回归实例
print("Linear Regression")

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3]])
y_hat = np.array([[5] ,[7], [9]])

model = LinearRegression()
# fit 方法的作用是：它使用输入特征 x 和对应的目标值 y_hat 来训练模型，即调整模型内部的参数，以便模型能够尽可能准确地预测或拟合给定的数据。
model.fit(x, y_hat)
# plt.plot() 函数用于绘制二维图形 'b' 表示蓝色（blue） '.' 表示点的样式，这里它告诉matplotlib以点的形式来绘制数据。
plt.plot(x, y_hat, 'r.')

x = [[0], [4]]
y = model.predict(x)
plt.plot(x, y, 'b-') # 'k' 表示黑色（black） '-' 表示线的样式，这里它告诉matplotlib以线的形式来绘制预测值。

print('得到的一次回归方程为: y =', model.coef_[0][0], '* x +', model.intercept_[0])

plt.show()