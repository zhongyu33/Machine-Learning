#使用时需保证date1.txt与该文件在同一目录下

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
x = []
y = []

k1, k0 = sp.symbols('k1 k0')

z = 0
cnt = 0
with open("data1.txt", "r", encoding="utf-8") as f:
    for line in f:
        if not line:
            break

        cur = line.strip()
        cur = cur.split(",")
        if cur[0] == 'x':
            continue
        cur[0] = float(cur[0])
        cur[1] = float(cur[1])
        x.append(cur[0])
        y.append(cur[1])
        cnt += 1
        z += (k1 * cur[0] + k0 - cur[1]) ** 2

z /= cnt

alpha = 0.00001

fig, ax = plt.subplots()

# 计算符号梯度放在外面
gk0 = sp.diff(z, k0)
gk1 = sp.diff(z, k1)

gk0 = sp.lambdify((k0, k1), gk0, "numpy")
gk1 = sp.lambdify((k0, k1), gk1, "numpy")

cur_k0, cur_k1 = 0, 0
z_zhi = sp.lambdify((k0, k1), z, "numpy")
for i in range(100):

    deltak0 = gk0(cur_k0, cur_k1)
    deltak1 = gk1(cur_k0, cur_k1)

    cur_k0 -= deltak0 * alpha
    cur_k1 -= deltak1 * alpha
    if i % 10 == 0:
        plt.cla()
        plt.scatter(x, y, color='blue', label='数据点')
        x_line = np.linspace(min(x), max(x), 1000)
        y_line = cur_k1 * x_line + cur_k0
        plt.plot(x_line, y_line, color='red', label=f'拟合直线: z={cur_k1:.2f}x+{cur_k0:.2f}')
        plt.pause(0.1)
        print(i, z_zhi(cur_k0, cur_k1), cur_k0, cur_k1)
    sleep(0.1)
plt.close('all')
