# Path: test-venv.py
import os
import numpy as np

# print("Hello World!")

# 使用画图库matplotlib，打印出一个高斯分布的图像

import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# 创建图像
plt.figure()
plt.plot(x, y)
plt.show()

# 保存图像
plt.savefig("sin.png")

