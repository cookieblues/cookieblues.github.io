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
x_, t_ = vert_norm(x[idx], t[idx])

# Begin figure
fig, ax = plt.subplots(figsize=(7, 7/1.4))

ax.scatter(
    x=x,
    y=t,
    s=10,
    color="magenta",
    edgecolor="none"
)

ax.plot(
    x_,
    t_,
    color="forestgreen",
    linewidth=1
)



# x-axis
ax.set_xlabel(r"$x$", fontsize=14)

# y-axis
ax.set_ylabel(r"$t$", fontsize=14)
ax.set_ylim(-6.1, 6.1)

# link
ax.text(
    0.12,
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
plt.savefig("poly_reg_02.png", bbox_inches="tight")
plt.show()