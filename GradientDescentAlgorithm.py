# 梯度下降算法 学习w和b参数实例

# 初值
w = 4
b = 3
yita = 0.01  # 学习率

x_arr = [1, 2, 3]
y_hat_arr = [5, 7, 10]

flag = True
epoch = 0
while flag: # 或者指定轮数: epoch < 5
    epoch += 1
    i = 0
    for i in range(len(x_arr)):
        x = x_arr[i]
        y_hat = y_hat_arr[i]
        # 偏导数
        pL_w = -2*y_hat*x + 2*b*x + 2*w*x*x
        pL_b = -2*y_hat + 2*b + 2*w*x

        print(pL_w)
        print(pL_b)

        w = w - yita*pL_w
        b = b - yita*pL_b
        print("w = ", round(w, 5), "\t", "b: ", round(b, 5))

        if abs(pL_w) < 0.02 and abs(pL_b) < 0.02:
            flag = False
            break
