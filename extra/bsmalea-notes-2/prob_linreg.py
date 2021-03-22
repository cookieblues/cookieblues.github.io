import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

turq = mpl.colors.to_rgb("turquoise")
cdict3 = {"red":  ((0.0, turq[0], turq[0]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         "green": ((0.0, turq[1], turq[1]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         "blue":  ((0.0, turq[2], turq[2]),
                   #(0.25, 1.0, 1.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0))
        }
mycmp = mpl.colors.LinearSegmentedColormap("mycmp", cdict3)

x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])

def f(x):
    return 3*np.sin((1/2)*np.pi * x) - 2*np.sin((3/2) * np.pi * x)

def plot_homogen_prob_density(x, y, variance, ax, l=1000, **kwargs):
    y_min, y_max = y.min()-2*np.sqrt(variance), y.max()+2*np.sqrt(variance)
    yy = np.linspace(y_min, y_max, l)
    a = [np.exp(-(y_-yy)**2/variance) / np.sqrt(variance) for y_ in y]
    a = np.array(a).reshape(len(y), l)
    ax.imshow(
        -a.T,
        aspect="auto",
        origin="lower",
        extent=(x.min(), x.max(), y_min, y_max),
        **kwargs
    )

X = np.vstack([np.ones(x.shape), x]).T

w = np.linalg.inv(X.T @ X) @ X.T @ t
alpha = sum((t - X @ w)**2) / len(t)

h = np.poly1d(np.flip(w, 0))

x_ = np.linspace(x.min()-0.025, x.max()+0.025, 250)
t_ = h(x_)

fig = plt.figure(figsize=(7,7/golden))
ax = fig.add_subplot()

plot_homogen_prob_density(x_, t_, alpha, ax=ax, cmap=mycmp, alpha=0.625)
# ax.fill_between(x_, t_-np.sqrt(alpha), t_+np.sqrt(alpha),
#     color="turquoise",
#     linewidth = 0,
#     alpha = 0.25
# )
ax.scatter(x, t,
    edgecolors = "magenta",
    c = "None",
    s = 12.5,
    marker = "o",
    zorder = 3
)
ax.plot(x_, t_,
    color="turquoise",
    linewidth = 1,
    label = "Predicted (mean)"
)
true = np.linspace(x.min()-0.025, x.max()+0.025, 250)
ax.plot(
    true, f(true),
    color="magenta",
    linewidth = 1,
    label = "True"
)

ax.set_xlim(x.min()-0.025, x.max()+0.025)
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_xticklabels([-1, -0.5, 0, 0.5, 1])
ax.set_xlabel(r"$x$", fontsize=14)

ax.set_yticks([-6, -4, -2, 0, 2, 4, 6])
ax.set_yticklabels([-6, -4, -2, 0, 2, 4, 6])
ax.set_ylabel(r"$t$", fontsize=14)

ax.legend(frameon=False, fontsize=14)

ax.text(
    0.88,
    0.025,
    'cookieblues.github.io',
    fontsize=11,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color='dimgrey',
    zorder=5
)

plt.tight_layout()
plt.savefig("prob_linreg.png", bbox_inches="tight")
plt.show()


