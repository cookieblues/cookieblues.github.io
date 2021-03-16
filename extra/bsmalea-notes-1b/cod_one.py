import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

X = np.array([
    [0.33, 0.88, 0.11],
    [0.74, 0.54, 0.62],
    [0.79, 0.07, 0.31],
    [0.83, 0.24, 0.47],
    [0.05, 0.42, 0.47],
    [0.82, 0.70, 0.10],
    [0.51, 0.76, 0.51],
    [0.71, 0.92, 0.59],
    [0.78, 0.19, 0.05],
    [0.43, 0.53, 0.53]
])
t = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


# one dimension
fig = plt.figure(figsize=(9/golden, 9/golden))
ax = fig.add_subplot(111)

ax.scatter(X[:5,0], [0]*5,
    edgecolors = "magenta",
    c = "None",
    s = 17.5,
    marker = "o",
    label = "Class 0",
    zorder = 2
)
ax.scatter(X[5:,0], [0]*5,
    edgecolors = "turquoise",
    c = "None",
    s = 17.5,
    marker = "o",
    label = "Class 1",
    zorder = 2
)
ax.fill_between([0, 0.2], [0.05, 0.05], [-0.05, -0.05],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.2, 0.4], [0.05, 0.05], [-0.05, -0.05],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.4, 0.6], [0.05, 0.05], [-0.05, -0.05],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
ax.fill_between([0.6, 0.8], [0.05, 0.05], [-0.05, -0.05],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.8, 1.0], [0.05, 0.05], [-0.05, -0.05],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)

ax.tick_params(which="major", width=1.00)
ax.tick_params(which="major", length=5)
ax.tick_params(which="minor", width=0.75)
ax.tick_params(which="minor", length=2.5)

ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.025))

ax.set_xlim(0,1)
ax.set_ylim(-1,1)
ax.get_yaxis().set_visible(False)

ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_position(("data",-0.01295))
ax.spines["bottom"].set_zorder(0)
ax.legend(frameon=False,loc=(0.01,0.55))


plt.tight_layout()
plt.savefig("one_dim_cod.png",
    bbox_inches=mpl.transforms.Bbox([[0, 1.5], [9/golden, (9/golden)-1.25]])
)
plt.show()
