# 线性回归实例
print("Linear Regression")

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3]])
y_hat = np.array([[5] ,[7], [9]])

model = LinearRegression()
model.fit(x, y_hat)
plt.plot(x, y_hat, 'b.')

x = [[0], [4]]
y = model.predict(x)
plt.plot(x, y, 'k-')

print('得到的一次回归方程为: y =', model.coef_[0][0], '* x +', model.intercept_[0])

plt.show()