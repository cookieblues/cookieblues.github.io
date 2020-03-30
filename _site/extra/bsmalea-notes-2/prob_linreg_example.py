import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")


x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
t = np.array([1.15, 0.84, 0.39, 0.14, 0, 0.56, 1.16, 1.05, 1.45, 2.39, 1.86])

def f(x):
    return 1 + np.sin(-(3/2) * np.pi * x) + (1/3) * np.sin(5 * np.pi * x)

M = 3
N = len(x)
X = np.zeros((N, M+1))

for m in range(M+1):
    X[:, m] = x**m
beta = np.linalg.inv(X.T @ X) @ X.T @ t
h = np.poly1d(np.flip(beta, 0))

x_ = np.linspace(0.219, 0.421, 250)
t_ = h(x_)

xs = np.array([0.28, 0.38])



fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()


ax.plot(x_, t_,
    color = "turquoise",
    linewidth = 1,
    zorder = 1
)
ax.scatter(xs, h(xs),
    edgecolors = "magenta",
    c = "None",
    s = 12.5,
    marker = "o",
    zorder = 2
)

ax.set_xticks(xs)
ax.set_xticklabels(["$x_i$", "$x_j$"])
ax.set_xlim(0.22, 0.42)
ax.set_yticks(h(xs))
ax.set_yticklabels(["$h(x_i, \mathbf{w})$", "$h(x_j, \mathbf{w})$"])
ax.set_ylim(0.12, 0.32)


plt.tight_layout()
#plt.savefig("poly_reg.svg")
plt.show()


