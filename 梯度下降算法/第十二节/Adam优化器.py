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

optimizer = torch.optim.Adam([x, y], lr = 0.005)
cur = [0]
for i in range(30000):
    cur[0] += 1
    optimizer.zero_grad()
    z = rosenbrock(x, y)
    z.backward()
    optimizer.step()
    if i % 10000 == 0:
        print(x.item(), y.item(), z.item())


