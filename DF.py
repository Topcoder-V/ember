# 深度优先（生成树）
import matplotlib.pyplot as plt
import math

# 生长（在t的末端产生角度为d的分枝）
def grow(t, d):
    pass

stack = [] # 栈

t = {'x1': 100, 'y1': 0, 'x2': 100, 'y2': 30, 'angle': math.pi*0.5, 'level': 1, 'length': 30, 'branch': 2, 'sub': 0}

stack.append(t)
plt.plot([t['x1'], t['x2']], [t['y1'], t['y2']])

max_level = 4

while len(stack) > 0:
    t = stack[len(stack) - 1]
    if t['sub'] > t['branch']:
        stack.pop()
    else:
        if t['level'] < max_level:
            if t['sub'] == 0:
                t1 = grow(t, 0.3)
                stack.append(t1)
                plt.plot([t1['x1'], t1['x2']], [t1['y1'], t1['y2']])
            elif t['sub'] == 1:
                t2 = grow(t, -0.3)
                stack.append(t2)
                plt.plot()
