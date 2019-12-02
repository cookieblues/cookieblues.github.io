import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])

def f(x):
    return 3*np.sin((1/2)*np.pi * x) - 2*np.sin((3/2) * np.pi * x)

M = 4
N = len(x)
X = np.zeros((N, M+1))

for m in range(M+1):
    X[:, m] = x**m

beta = np.linalg.inv(X.T @ X) @ X.T @ t

h = np.poly1d(np.flip(beta, 0))

x_ = np.linspace(x.min()-0.025, x.max()+0.025, 250)
t_ = h(x_)

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

ax.scatter(x, t,
    edgecolors = "magenta",
    c = "None",
    s = 12.5,
    marker = "o"
)
ax.plot(x_, t_,
    color="turquoise",
    linewidth = 1,
    label = "Predicted"
)
true = np.linspace(x.min()-0.025, x.max()+0.025, 250)
ax.plot(
    true, f(true),
    color="magenta",
    linewidth = 1,
    label = "True"
)

ax.set_xlim(x.min()-0.025, x.max()+0.025)
ax.set_xticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_xticklabels(["$-1.0$", "$-0.8$", "$-0.6$", "$-0.4$", "$-0.2$", "$0.0$", "$0.2$", "$0.4$", "$0.6$", "$0.8$", "$1.0$"])
ax.legend(frameon=False)


plt.tight_layout()
plt.savefig("poly_reg.svg")
plt.show()


