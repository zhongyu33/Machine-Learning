'''方法一'''
from matplotlib import pyplot as plt

x = 100.1
y = 200.1
n = 100
alpha = 0.05
x1 = [i for i in range(1, n + 1)]
y1 = []
for i in range(1, n + 1):
    gx = x * 2
    gy = y * 2


    x = x - alpha * gx
    y = y - alpha * gy

    y1.append(x ** 2 + y ** 2)
# plt.scatter(x1, y1, color="blue", marker="o", s=2, alpha=0.7)
#
# # 添加标题和标签
# plt.title("pic")
# plt.xlabel("X 轴")
# plt.ylabel("Y 轴")
#
# # 显示图像
# plt.show()
#

'''方法二'''

import sympy as sp

cur_x = 100.1
cur_y = 200.1

x, y = sp.symbols('x y')

z = x ** 2 + y ** 2

alpha = 0.05
y2 = []

for i in range(1, n + 1):
    gx = sp.diff(z, x)
    gy = sp.diff(z, y)

    deltax = gx.subs(x, cur_x)
    deltay = gy.subs(y, cur_y)

    cur_x = cur_x - alpha * deltax
    cur_y = cur_y - alpha * deltay
    y2.append(cur_x ** 2 + cur_y ** 2)

# print(x1)
# print(y1)
# print(y2)

plt.scatter(x1, y1, color="red", marker="o", s=2, alpha=0.5)
plt.scatter(x1, y2, color="blue", marker="o", s=2, alpha=0.5)

plt.title("pic")
plt.xlabel("X 轴")
plt.ylabel("Y 轴")

# 显示图像
plt.show()




