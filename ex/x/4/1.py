import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# تعریف توابع
def f1(x):
    return np.sqrt(x)


def f2(x):
    return x**2


# دامنه x
x = np.linspace(0, 2, 100)

# دوران توابع حول محور x
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# محاسبه دوران حول محور x برای هر تابع
Y1 = f1(X) * np.cos(Theta)
Z1 = f1(X) * np.sin(Theta)

Y2 = f2(X) * np.cos(Theta)
Z2 = f2(X) * np.sin(Theta)

# نمایش نمودار سه‌بعدی
fig = plt.figure(figsize=(14, 7))

# دوران y=√x
ax1 = fig.add_subplot(121, projection="3d")
ax1.plot_surface(X, Y1, Z1, color="cyan", alpha=0.7)
ax1.set_title("Rotation of y = √x around x-axis")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# دوران y=x^2
ax2 = fig.add_subplot(122, projection="3d")
ax2.plot_surface(X, Y2, Z2, color="magenta", alpha=0.7)
ax2.set_title("Rotation of y = x^2 around x-axis")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

plt.show()
