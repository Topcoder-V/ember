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
# 打印拟合后的模型参数
# 对于线性回归模型，参数包括斜率（coef_）和截距（intercept_）
print(f"斜率（Slope）: {model.coef_}") # 斜率（Slope）: [[2.]]
print(f"截距（Intercept）: {model.intercept_}") # 截距（Intercept）: [3.]
"""
如果你的模型是多元线性回归（即有多个特征变量），model.coef_将是一个数组，其中的每个元素对应一个特征变量的斜率。

请注意，如果你的数据集x是一维的，你需要将其转换为二维数组，因为scikit-learn期望输入数据是2D的。
在上面的示例中，x被写为[[1], [2], [3], [4], [5]]，这是因为每个样本只有一个特征，但它仍然需要是一个二维数组。
如果你的x已经是二维的，那么你不需要进行任何转换。
"""


# plt.plot() 函数用于绘制二维图形 'b' 表示蓝色（blue） '.' 表示点的样式，这里它告诉matplotlib以点的形式来绘制数据。
plt.plot(x, y_hat, 'r.')

x = [[0], [4]]
y = model.predict(x)
plt.plot(x, y, 'b-') # 'k' 表示黑色（black） '-' 表示线的样式，这里它告诉matplotlib以线的形式来绘制预测值。

print('得到的一次回归方程为: y =', model.coef_[0][0], '* x +', model.intercept_[0])

plt.show()