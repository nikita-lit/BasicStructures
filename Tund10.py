# --------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y)
# plt.title("Lihtne graafik")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.show()

# x = np.arange(-5, 10, 0.5)
# y = x**2-2*x+6

# plt.figure(facecolor="green")
# plt.title("Parabola")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.grid(True)
# plt.plot(x, y, color="blue", linestyle="-", marker="D", markersize=8)
# plt.show()

# --------------------------------------
plt.figure(facecolor="green")
plt.title("Glasses")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)

x = np.arange(-9, -1, 0.01)
y = -(1/16)*(x+5)**2 + 2
plt.plot(x, y, color="blue", linestyle="-", marker="D", markersize=8)

x = np.arange(1, 9, 0.01)
y = -(1/16)*(x-5)**2 + 2
plt.plot(x, y, color="blue", linestyle="-", marker="D", markersize=8)

x = np.arange(-9, -1, 0.01)
y = (1/4)*(x+5)**2 - 3
plt.plot(x, y, color="blue", linestyle="-", marker="D", markersize=8)

x = np.arange(1, 9, 0.01)
y = (1/4)*(x-5)**2 - 3
plt.plot(x, y, color="blue", linestyle="-", marker="D", markersize=8)

x = np.arange(-9, -6, 0.01)
y = -(x+7)**2 + 5
plt.plot(x, y, color="black", linestyle="-", marker="D", markersize=8)

x= np.arange(6, 9, 0.01)
y = -(x-7)**2 + 5
plt.plot(x, y, color="black", linestyle="-", marker="D", markersize=8)

x = np.arange(-1, 1, 0.01)
y = -0.5*x**2 + 1.5
plt.plot(x, y, color="red", linestyle="-", marker="D", markersize=8)

plt.show()