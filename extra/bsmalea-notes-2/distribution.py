import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

# Define data
x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])

# Create vertical normal distribution
def vert_norm(x_val, y_val, std=1, y_min=-10, y_max=10):
    y_ = np.linspace(y_min, y_max, num=1000)
    x_ = x_val+norm.pdf(y_, loc=y_val, scale=std)
    return x_, y_

t_ = np.linspace(-10, 10)
x_ = norm.pdf(t_)
idx = 2

# Begin figure
fig, ax = plt.subplots(figsize=(7, 7/1.4))
x_min, x_max = -1.1, 1.1
y_min, y_max = -6.1, 6.1


# Calc polynomial
M = 3
N = len(x)
X = np.zeros((N, M+1))

for m in range(M+1):
    X[:, m] = x**m

beta = np.linalg.inv(X.T @ X) @ X.T @ t
h = np.poly1d(np.flip(beta, 0))
x_p = np.linspace(x.min()-0.1, x.max()+0.1, 250)
t_p = h(x_p)


x_, t_ = vert_norm(x[idx], h(x[idx]))

ax.plot(x_p, t_p,
    color="turquoise",
    linewidth = 1,
    label = r"$h$"
)


ax.scatter(
    x=x,
    y=t,
    edgecolors = "magenta",
    c = "None",
    s = 12.5,
    marker = "o",
    zorder = 3
)

ax.plot(
    x_,
    t_,
    color="forestgreen",
    linewidth=1,
    alpha=0.5
)

ax.arrow(
    x=x[idx]+0.025,
    y=h(x[idx])+0.5,
    dx=0,
    dy=0.5,
    width=0.005,
    length_includes_head=True,
    head_width=0.02,
    head_length=0.15,
    facecolor="black",
    edgecolor="none",
    shape="full"
)
ax.arrow(
    x=x[idx]+0.025,
    y=h(x[idx])+0.5,
    dx=0,
    dy=-0.35,
    width=0.005,
    length_includes_head=True,
    head_width=0.02,
    head_length=0.15,
    facecolor="black",
    edgecolor="none",
    shape="full"
)
ax.text(
    0.255,
    (h(x[idx])+0.55-y_min)/(y_max-y_min),
    r"$\sigma$",
    fontsize=11,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color="black",
    zorder=5
)


ax.arrow(
    x=x[idx]+0.025,
    y=h(x[idx])-0.5,
    dx=0,
    dy=-0.5,
    width=0.005,
    length_includes_head=True,
    head_width=0.02,
    head_length=0.15,
    facecolor="black",
    edgecolor="none",
    shape="full"
)
ax.arrow(
    x=x[idx]+0.025,
    y=h(x[idx])-0.5,
    dx=0,
    dy=0.35,
    width=0.005,
    length_includes_head=True,
    head_width=0.02,
    head_length=0.15,
    facecolor="black",
    edgecolor="none",
    shape="full"
)
ax.text(
    0.255,
    (h(x[idx])-0.6-y_min)/(y_max-y_min),
    r"$\sigma$",
    fontsize=11,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color="black",
    zorder=5
)


ax.axhline(
    h(x[idx]),
    xmin=0,
    xmax=(x[idx]-x_min)/(x_max-x_min),
    color="forestgreen",
    linestyle="--",
    alpha=0.5
)
ax.text(
    -0.1,
    (h(x[idx])-y_min)/(y_max-y_min),
    r"$h(\mathbf{x}_i, \mathbf{w})$",
    fontsize=18,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color="forestgreen",
    zorder=5
)
ax.axvline(
    x[idx],
    ymin=0,
    ymax=(h(x[idx])-y_min)/(y_max-y_min),
    color="forestgreen",
    linestyle="--",
    alpha=0.5
)
ax.text(
    (x[idx]-x_min)/(x_max-x_min),
    -0.06,
    r"$\mathbf{x}_i$",
    fontsize=18,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color="forestgreen",
    zorder=5
)




# x-axis
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_xlim(x_min, x_max)

# y-axis
ax.set_ylabel(r"$t$", fontsize=14)
ax.set_ylim(y_min, y_max)

ax.legend(framealpha=0, fontsize=14)

# link
ax.text(
    0.87,
    0.02,
    'cookieblues.github.io',
    fontsize=11,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color='dimgrey',
    zorder=5
)


plt.tight_layout()
plt.savefig("distribution.svg", bbox_inches="tight")
plt.show()