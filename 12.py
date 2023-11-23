import numpy as np
import matplotlib.pyplot as plt


# 创建函数，用于生成不同属于一个平面的100个离散点
def not_all_in_plane(a, b, c):
    x = np.random.uniform(-10, 10, size=100)
    y = np.random.uniform(-10, 10, size=100)
    z = (a * x + b * y + c) + np.random.normal(-1, 1, size=100)
    return x, y, z


# 调用函数，生成离散点
x, y, z = not_all_in_plane(2, 5, 6)
N = 100
# ------------------------构建系数矩阵-----------------------------
A = np.array([[sum(x ** 2), sum(x * y), sum(x)],
              [sum(x * y), sum(y ** 2), sum(y)],
              [sum(x), sum(y), N]])

B = np.array([[sum(x * z), sum(y * z), sum(z)]])

# 求解
X = np.linalg.solve(A, B.T)
print('平面拟合结果为：z = %.3f * x + %.3f * y + %.3f' % (X[0], X[1], X[2]))
# -------------------------结果展示-------------------------------
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.scatter(x, y, z, c='r', marker='o')
x_p = np.linspace(-10, 10, 100)
y_p = np.linspace(-10, 10, 100)
x_p, y_p = np.meshgrid(x_p, y_p)
z_p = X[0] * x_p + X[1] * y_p + X[2]
ax1.plot_wireframe(x_p, y_p, z_p, rstride=10, cstride=10)
plt.show()