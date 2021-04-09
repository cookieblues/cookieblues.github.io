import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(3)

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

# Class 1
a = np.random.multivariate_normal(
    mean = [-1.5, -1],
    cov = [[0.15, 0.05], [0.05 , 0.5]],
    size = 125
)
b = np.random.multivariate_normal(
    mean = [0.2, -0.5],
    cov = [[0.5, 0.75], [0.75, 0.5]],
    size = 125
)
c1 = np.concatenate([a, b])

# Class 2
a = np.random.multivariate_normal(
    mean = [-1, 1],
    cov = [[0.5, -0.15], [-0.15 , 0.5]],
    size = 125
)
b = np.random.multivariate_normal(
    mean = [1, -0.5],
    cov = [[1.25, 0], [0, 0.2]],
    size = 125
)
c2 = np.concatenate([a, b])


df = pd.DataFrame(index=range(500), columns=["first", "second", "target"])
df[["first", "second"]] = np.concatenate([c1, c2])
df["target"].iloc[:250] = 0
df["target"].iloc[250:] = 1
df.to_csv("data.csv", index=False)


fig = plt.figure(figsize=(8, 8/1.4))
ax = fig.add_subplot(111)

ax.scatter(
    x = c1[:, 0],
    y = c1[:, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.8,
    label = "Class 0"
)
ax.scatter(
    x = c2[:, 0],
    y = c2[:, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.8,
    label = "Class 1"
)
ax.scatter(
    x = c2[:, 0],
    y = c2[:, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.4
)
ax.scatter(
    x = c1[:, 0],
    y = c1[:, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.4
)

ax.legend(framealpha=0, loc="upper left", fontsize=14)
ax.axis("equal")
# xticks = range(-4, 5)
# ax.set_xlim(-4, 5)
# ax.set_xticks(xticks)
# ax.set_xticklabels(xticks, fontsize=14)

# yticks = range(-4, 4)
# ax.set_ylim(-4, 4)
# ax.set_yticks(yticks)
# ax.set_yticklabels(yticks, fontsize=14)


plt.tight_layout()
plt.savefig("data.png", bbox_inches="tight")
plt.show()

