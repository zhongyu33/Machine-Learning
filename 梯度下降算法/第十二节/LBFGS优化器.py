#需要定义closure,且调用次数并非真实调用次数
import numpy as np
import matplotlib.pyplot as plt
import torch
def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)

x = torch.tensor(1.3, requires_grad=True)
y = torch.tensor(6.7, requires_grad=True)

optimizer = torch.optim.LBFGS([x, y])
cur = [0]
for i in range(19):
    def closure():
        cur[0] += 1
        optimizer.zero_grad()
        z = rosenbrock(x, y)
        z.backward()
        print(cur[0], x.item(), y.item(), z.item())
        return z
    optimizer.step(closure)

# Z = rosenbrock(X, Y)
# x = torch.tensor(1.3, requires_grad=True)
# y = torch.tensor(6.7, requires_grad=True)

# borad = plt.figure()
# axis = borad.add_subplot(1, 1, 1, projection='3d')
# axis.plot_surface(X, Y, Z)
# plt.show()
