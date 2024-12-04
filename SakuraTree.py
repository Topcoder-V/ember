# 广度优先算法绘制樱花树 Breath First Algorithm (BF)
import matplotlib.pyplot as plt
import random
import math

# branches 枝干

# 生长（在枝干t的末端，产生角度为d的分支）
def grow(t, d, color, length, linewidth):
    # 新枝干tn的坐标起始位置，是枝干t的末端。
    tn = {'x1': t['x2'], 'y1': t['y2'], 'x2': 0, 'y2': 0, 'angle':0, 'level': t['level']+1,
          'length': length, 'color': color, 'linewidth':linewidth}
    # 单独拿出来写表示强调
    tn['angle'] = t['angle'] + d
    tn['x2'] = tn['x1'] + math.cos(tn['angle'])*tn['length']
    tn['y2'] = tn['y1'] + math.sin(tn['angle'])*tn['length']

    return tn

# 队列
queue = []

# 字典存放根枝干信息
t = {'x1': 100, 'y1': 0, 'x2': 100, 'y2': 30, 'angle': math.pi*0.5, 'level': 1, 'length': 30, 'color': '#a0522d', 'linewidth':10.0}

queue.insert(0, t) # 入队

max_level =  random.randint(7,8) # 树的最大深度（最大层数）
print('max_level', max_level)

def Tree(t, max_level):
    while len(queue) > 0:

        t = queue.pop() # 出队
        # print(t)

        # 绘制枝干
        plt.plot([t['x1'], t['x2']], [t['y1'], t['y2']], color=t['color'], linewidth=t['linewidth'] )


        # 生长
        if t['level'] < max_level:
            # 随机产生角度, 对称即可，剩余的视觉冲击力交给长度随机。
            d = random.uniform(0.2, 0.5)
            length = random.uniform(10, 20)

            if t['linewidth'] > 2.0:
                linewidth = t['linewidth'] - 2.0  # 枝干宽度减小

            # 末梢
            if t['level'] == max_level - 1:
                colors = ['white', 'lightcoral'] # 淡珊瑚色
                probabilities = [0.3, 0.7]  # 假设白色出现的概率是60%，粉色是40%
                # 使用random.choices()来根据概率选择颜色
                color = random.choices(colors, weights=probabilities, k=1)[0] # 参数k表示随机抽取的个数
                length = random.uniform(3, 5)
                linewidth = 5.0
            else:
                color = '#a0522d' # 不同深度的枝干用不同颜色表示

            if t['level'] == max_level - 2:
                length = random.uniform(3, 10)

            # 左分支生长
            t1 = grow(t, d, color ,length, linewidth)
            queue.insert(0, t1) # 从左向右入队

            # 同一节点的两个叶子颜色互异
            # if t['level'] == max_level - 1:
            #     colors = ['white', 'pink']
            #     color = colors[1] if color == colors[0] else colors[0]

            # 右分支生长
            t2 = grow(t, -d, color, length, linewidth)
            queue.insert(0, t2) # 从左向右入队


Tree(t, max_level)
# 设置图形背景颜色
plt.gca().set_facecolor('#f5deb3')  # 设置轴的背景颜色为浅灰色
plt.show()


