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

fig = plt.figure(figsize=(8, 8/golden))
ax = fig.add_subplot()

for idx, x_i in enumerate(x):
    x_pred = h(x_i)
    if x_pred > t[idx]:
        ax.axvline(
            x_i,
            ymin = abs((t[idx]+6.2)/12.4),
            ymax = abs((x_pred+6.2)/12.4),
            color = "turquoise",
            linestyle = "--",
            zorder=1
        )
    else:
        if idx == 0:
            ax.axvline(
                x_i,
                ymin = abs((x_pred+6.2)/12.4),
                ymax = abs((t[idx]+6.2)/12.4),
                color = "turquoise",
                linestyle = "--",
                zorder=1,
                label="Residual"
            )
        else:
            ax.axvline(
                x_i,
                ymin = abs((x_pred+6.2)/12.4),
                ymax = abs((t[idx]+6.2)/12.4),
                color = "turquoise",
                linestyle = "--",
                zorder=1
            )


ax.scatter(x, t,
    edgecolors = "magenta",
    facecolor = "white",
    s = 12.5,
    marker = "o",
    label = "Data",
    zorder = 2
)
ax.plot(x_, t_,
    color="turquoise",
    linewidth = 1,
    label = "Polynomium",
    zorder = 1
)
true = np.linspace(x.min()-0.025, x.max()+0.025, 250)
# ax.plot(
#     true, f(true),
#     color="magenta",
#     linewidth = 1,
#     label = "True"
# )

ax.set_xlabel("Input", fontsize=14)
ax.set_xlim(x.min()-0.025, x.max()+0.025)
ax.set_xticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_xticklabels(["$-1.0$", "$-0.8$", "$-0.6$", "$-0.4$", "$-0.2$", "$0.0$", "$0.2$", "$0.4$", "$0.6$", "$0.8$", "$1.0$"], fontsize=10)

ax.set_ylabel("Target", fontsize=14)
ax.set_ylim(-6.2, 6.2)

ax.legend(frameon=False, fontsize=14)


plt.tight_layout()
plt.savefig("residuals.svg")
plt.show()


