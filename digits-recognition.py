# 数字识别
# 用sklearn的digits数据集训练MLP

# https://blog.csdn.net/wlddhj/article/details/139124584
from sklearn.datasets import load_digits
# 作用：提供手写数字（0-9）的数据集，每个样本都是8x8的图像。这是一个用于图像识别和机器学习入门的数据集。

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 加载数据集
digits = load_digits()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# 创建MLP分类器
mlp = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000, random_state=42)

# 训练模型
mlp.fit(X_train, y_train)

# 预测测试集
y_pred = mlp.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)     # 输出准确率

# 可视化测试集中的一些图像及其预测结果
test_images = X_test[:16]  # 取测试集的前16张图像
test_labels = y_test[:16]  # 和对应的标签
predictions = y_pred[:16]  # 和对应的预测结果

images_to_show = test_images.reshape(-1, 8, 8)  # 将图像数据重塑为8x8的形状

fig, axes = plt.subplots(4, 4)
fig.subplots_adjust(hspace=1, wspace=0.5)

for i, ax in enumerate(axes.flat):
    ax.imshow(images_to_show[i], cmap='gray_r')
    ax.set_title(f"True: {test_labels[i]}")
    ax.set_xlabel(f"Prediction: {predictions[i]}")
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
