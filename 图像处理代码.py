import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


# plt.plot(x, y)
# plt.title('折线图')

# plt.scatter(x, y)
# plt.title('散点图')


plt.xlabel('x 轴')
plt.ylabel('y 轴')


# 条形图
# x = ['A', 'B', 'C', 'D']
# y = [10, 15, 7, 12]
#
# plt.bar(x, y)
# plt.title('条形图')
# plt.xlabel('类别')
# plt.ylabel('值')

# 饼图
# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
#
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title('饼图')
# plt.axis('equal')
# plt.show()


# 多图合并
# # 创建数据
x = [1, 2, 3, 4]
y1 = [1, 3, 2, 4]
y2 = [3, 1, 4, 2]

# 创建子图 1
plt.subplot(2, 1, 1)  # 2 行 1 列，第 1 个子图
plt.plot(x, y1)
plt.title('子图 1')
plt.xlabel('x 轴')
plt.ylabel('y1 轴')

n=9
# 创建子图 2
plt.subplot(2, 1, 2)  # 2 行 1 列，第 2 个子图
plt.plot(x, y2)
plt.title(f'子图{n}')
plt.xlabel('x 轴')
plt.ylabel('y2 轴')


# 调整子图布局
plt.tight_layout()

# 显示图形
plt.show()
class Draw_all_to_one():
    def __init__(self,raw,col):
        super(Draw_all_to_one,self).__init__()
        self.r=raw
        self.c=col
        x=[]
        y=[]
        for i in range(self.r):
            for j in range(self.c):
                x.append(i)
                y.append(j)
                plt.subplot(self.r,self.c,i*self.c+j+1)
                plt.plot(x,y)
        plt.tight_layout()
        plt.show()

Draw_all_to_one(4,5)