import turtle
import matplotlib.pyplot as plt
import numpy as np
import os


class Shape:
    type = 0
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Input(self):
        pass

    def Print(self):
        pass

    def Draw(self, screen):
        pass


class Circle(Shape):
    r = 0

    def __init__(self, x=0, y=0, r=10):
        Shape.__init__(self, x, y)
        self.r = r

    def Input(self):
        print('输入圆心和半径：X-Y-R')
        in_num = 1
        while in_num:
            try:
                self.x = float(input('X='))
                self.y = float(input('Y='))
                self.r = float(input('R='))
            except:
                print('请输入数字')
            else:
                in_num = 0

    def Print(self):
        print("圆：(X=" + str(self.x) + ", Y=" + str(self.y) + ", R=" + str(self.r) + ")")

    def Draw(self, x_min, x_max, y_min, y_max):
        if ((self.x - self.r) < x_min):
            x_min = (self.x - self.r) - 100
        if ((self.x + self.r) > x_max):
            x_max = (self.x + self.r) + 100
        if ((self.y - self.r) < y_min):
            y_min = (self.y - self.r) - 100
        if ((self.y + self.r) > y_max):
            y_max = (self.y + self.r) + 100

        print(x_min, x_max, y_min, y_max, '圆')

        # 绘制圆形
        circle = plt.Circle((self.x, self.y), self.r, color='blue', fill=False)
        # 将图形添加到当前的axes

        plt.gca().add_artist(circle)

        return x_min, x_max, y_min, y_max


class Rect(Shape):
    w = 0
    h = 0

    def __init__(self, x=0, y=0, w=10, h=5):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h

    def Input(self):
        print('输入左上角坐标（0-100）和宽高：X-Y-W-H')
        in_num = 1
        while in_num:
            try:
                self.x = float(input('X='))
                self.y = float(input('Y='))
                self.w = float(input('W='))
                self.h = float(input('H='))
            except:
                print('请输入数字')
            else:
                in_num = 0

    def Print(self):
        print("方形：(X=" + str(self.x) + ", Y=" + str(self.y) + ", W=" + str(self.w) + ", H=" + str(self.h) + ")")

    def Draw(self, x_min, x_max, y_min, y_max):
        if ((self.x - self.w) < x_min):
            x_min = (self.x - self.w) - 100
        if ((self.x + self.w) > x_max):
            x_max = (self.x + self.w) + 100
        if ((self.y - self.h) < y_min):
            y_min = (self.y - self.h) - 100
        if ((self.y + self.h) > y_max):
            y_max = (self.y + self.h) + 100

        # 绘制长方形
        rectangle = plt.Rectangle((self.x, self.y), self.w, self.h, color='red', fill=False)
        # 将图形添加到当前的axes
        plt.gca().add_artist(rectangle)

        print(x_min, x_max, y_min, y_max, '方')

        return x_min, x_max, y_min, y_max


class MIS:

    def __init__(self):
        self.data = []
        self.x_min = 0
        self.x_max = 1
        self.y_min = 0
        self.y_max = 1

    def Add(self):
        shape = input('输入图形： 1-圆形，2-方形')
        if shape == '1':
            c = Circle()
            c.Input()
            self.data.append(c)
            print('圆形已添加')
        elif shape == '2':
            r = Rect()
            r.Input()
            self.data.append(r)
            print('方形已添加')
        else:
            print("错误输入")

    def Print(self):
        for s in self.data:
            s.Print()
        print("图形总数：" + str(len(self.data)))

    def Reset(self):
        self.data.clear()

    def Save(self):
        filename = input("请输入要保存的文件名：")
        try:

            # with open(filename, 'w') as file:
            #     for shape in self.data:
            #         if isinstance(shape, Circle):
            #             file.write(f"Circle: X={shape.x}, Y={shape.y}, R={shape.r}\n")
            #         elif isinstance(shape, Rect):
            #             file.write(f"Rect: X={shape.x}, Y={shape.y}, W={shape.w}, H={shape.h}\n")
            #
            #     print(f"图形已保存到文件：{filename}")

            # 创建一个新的figure
            plt.figure()
            print(self.x_min, self.x_max, self.y_min, self.y_max, 'pure')

            for shape in self.data:
                x_min_res, x_max_res, y_min_res, y_max_res = shape.Draw(self.x_min, self.x_max, self.y_min, self.y_max)
                self.x_min = x_min_res
                self.x_max = x_max_res
                self.y_min = y_min_res
                self.y_max = y_max_res

            print(x_min_res, x_max_res, y_min_res, y_max_res, 'last')

            plt.xlim(x_min_res, x_max_res)
            plt.ylim(y_min_res, y_max_res)

            # 确定保存路径
            save_dir = 'D:\\homework'
            save_path = os.path.join(save_dir, f"{filename}.png")

            # 如果保存路径中的文件夹不存在，则创建它
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # 保存图形到文件
            plt.savefig(save_path)

            print(f"图形已保存到文件：{save_path}")



        except IOError as e:
            print(f"保存文件时发生错误：{e}")

    def Remove(self):
        shape_type = input("请输入要删除的图形类型：1-圆形，2-方形")
        initial_count = len(self.data)
        if shape_type == '1':
            self.data = [s for s in self.data if not isinstance(s, Circle)]
            print('已删除所有圆形')
        elif shape_type == '2':
            self.data = [s for s in self.data if not isinstance(s, Rect)]
            print('已删除所有方形')
        else:
            print("错误输入")

        final_count = len(self.data)
        if final_count == initial_count:
            print("没有找到要删除的图形")
        else:
            print(f"剩余图形总数：{final_count}")

    def DrawAll(self):

        # 创建一个新的figure
        plt.figure()
        print(self.x_min, self.x_max, self.y_min, self.y_max, 'pure')

        for shape in self.data:
            x_min_res, x_max_res, y_min_res, y_max_res = shape.Draw(self.x_min, self.x_max, self.y_min, self.y_max)
            self.x_min = x_min_res
            self.x_max = x_max_res
            self.y_min = y_min_res
            self.y_max = y_max_res

        print(x_min_res, x_max_res, y_min_res, y_max_res, 'last')

        plt.xlim(x_min_res, x_max_res)
        plt.ylim(y_min_res, y_max_res)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('equal')  # 确保x和y的单位长度相同
        # 显示图形
        plt.show()


class Main:
    def Welcome(self):
        print("欢迎使用图形管理系统")

    def Menu(self):
        print("a-添加，d-删除，s-保存，p-打印，g-绘制，e-退出")

    def Run(self):
        mis = MIS()
        self.Welcome()
        self.Menu()

        cmd = input()
        while cmd != 'e':
            if cmd == 'a':
                mis.Add()
            elif cmd == 'd':
                mis.Remove()
            elif cmd == 's':
                mis.Save()
            elif cmd == 'p':
                mis.Print()
            elif cmd == 'g':
                mis.DrawAll()

            elif cmd == 'e':
                print("退出系统")
            else:
                print("错误命令")

            self.Menu()
            cmd = input()


main = Main()
main.Run()

