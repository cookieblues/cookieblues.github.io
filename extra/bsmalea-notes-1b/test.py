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

Ms = [2, 8]

fig = plt.figure(figsize=(8, 4))

for i, M in enumerate(Ms):
    N = len(x)
    X = np.zeros((N, M+1))

    for m in range(M+1):
        X[:, m] = x**m

    w = np.linalg.inv(X.T @ X) @ X.T @ t
    h = np.poly1d(np.flip(w, 0))

    x_ = np.linspace(x.min()-0.05, x.max()+0.05, 250)
    t_ = h(x_)

    ax = fig.add_subplot(1,2,i+1)

    ax.scatter(x, t,
        edgecolors = "magenta",
        c = "None",
        s = 12.5,
        marker = "o"
    )
    if i == 0:
        ax.plot(x_, t_,
            color="turquoise",
            linewidth = 1,
            label = "Predicted",
            zorder=2
        )
    else:
        ax.plot(x_, t_,
            color="turquoise",
            linewidth = 1,
            zorder=2
        )
    true = np.linspace(x.min()-0.05, x.max()+0.05, 250)
    if i == 0:
        ax.plot(
            true, f(true),
            color="magenta",
            linewidth = 1,
            label = "True",
            zorder=1
        )
    else:
        ax.plot(
            true, f(true),
            color="magenta",
            linewidth = 1,
            zorder=1
        )

    ax.set_xlim(x.min()-0.05, x.max()+0.05)
    ax.text(0.6, -5, s=r"$M={}$".format(M))
    ax.set_ylim(t.min()-0.5, t.max()+0.5)
    #ax.set_title(str(M))
    if i == 0:
        ax.legend(frameon=False, loc=2)
    
    ax.set_aspect(1/ax.get_data_ratio(), adjustable='box')


plt.tight_layout()
plt.savefig("test.png")
plt.show()


