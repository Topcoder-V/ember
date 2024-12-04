'''
1963年，麻省理工学院的伊凡·苏泽兰（Ivan Sutherland）为交互界面添加了第二个维度。
苏泽兰在其博士论文中提出了交互式绘图程序SketchPad[1]，通过SketchPad和一支光笔，用户可以在屏幕上自由地绘制和缩放图形。
SketchPad的提出，开创了图形化用户界面的先河，也是人机交互发展史上的一大飞跃。
后续WIMP（Window、Icon、Menu、Pointer，视窗、图标、菜单、指针）界面、鼠标和所见即所得技术（what you see is what you get）的发展，
降低了计算机的学习成本，个人电脑和计算机应用得到了空前的发展，计算也由主机时代向个人计算时代过渡。
'''


class Shape:
    # 类属性：修改类属性会影响所有未覆盖该属性的实例。
    type = 0
    x = 0
    y = 0

    # 实例属性：修改一个实例的属性不会影响其他实例或类属性。
    def __init__(self, x=0, y=0):  # 构造方法
        self.x = x
        self.y = y

    def Input(self):
        pass

    def Print(self):
        pass

    def Draw(self):
        pass


# 将Shape作为父类传入
class Circle(Shape):
    # 圆心x, y继承Shape类
    r = 0  # 半径

    def __init__(self, x=0, y=0, r=10):
        Shape.__init__(self, x, y)  # 调用父类 Shape的构造方法
        self.r = r

    def Input(self):
        print('输入圆心和半径：X-Y-R')
        in_num = 1
        while in_num:
            try:  # 注意 try-except-else的用法
                self.x = float(input('X='))
                self.y = float(input('Y='))
                self.r = float(input('R='))
            except:
                print('请输入数字')
            # else通常用于在确定没有异常后执行额外的逻辑
            else:
                in_num = 0

    def Print(self):
        print("圆：(X=" + str(self.x) + ", Y=" + str(self.y) + ", R=" + str(self.r) + ")")


class Rect(Shape):
    # 左上角坐标x,y继承Shape
    w = 0  # 宽 width
    h = 0  # 高 height

    def __init__(self, x=0, y=0, w=10, h=5):
        Shape.__init__(self, x, y)  # 调用父类 Shape的构造方法
        self.w = w
        self.h = h

    def Input(self):
        print('输入左上角坐标和宽高：X-Y-W-H')
        in_num = 1
        while in_num:
            try:  # 注意 try-except-else的用法
                self.x = float(input('X='))
                self.y = float(input('Y='))
                self.z = float(input('W='))
                self.z = float(input('H='))
            except:
                print('请输入数字')
            # else通常用于在确定没有异常后执行额外的逻辑
            else:
                in_num = 0

    def Print(self):
        print("圆：(X=" + str(self.x) + ", Y=" + str(self.y) + ", W=" + str(self.w) + ", H=" + str(self.h) + ")")


class MIS:
    data = []

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


class Main:
    def Welcome(self):
        print("欢迎使用图形管理系统")

    def Menu(self):
        print("a-添加，d-删除，p-打印 ······")

    def Run(self):
        mis = MIS()  # 信息管理系统 Management Information System
        self.Welcome()
        self.Menu()

        cmd = input()  # 输入命令
        while cmd != 'e':
            if cmd == 'a':  # 添加 add
                mis.Add()
            elif cmd == 'd':  # 删除 remove
                mis.Delete()
            elif cmd == 's':  # 保存 save
                mis.Save()
            elif cmd == 'p':  # 打印Print
                mis.Print()
            elif cmd == 'e':  # 退出系统exit
                print("退出系统")
            else:
                print("错误命令")

            self.Menu()
            cmd = input()


main = Main()
main.Run()