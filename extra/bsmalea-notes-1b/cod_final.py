import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import LinearSegmentedColormap
from scipy.constants import golden
from sklearn.linear_model import LogisticRegression

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

turq = mpl.colors.to_rgb("turquoise")
mage = mpl.colors.to_rgb("magenta")
gold = mpl.colors.to_rgb("goldenrod")

cdict3 = {"red":  ((0.0, mage[0], mage[0]),
                   #(0.25, 0.0, 0.0),
                   (0.5, 1.0, 1.0),
                   #(0.75, 1.0, 1.0),
                   (1.0, turq[0], turq[0])),

         "green": ((0.0, mage[1], mage[1]),
                   #(0.25, 0.0, 0.0),
                   (0.5, 1.0, 1.0),
                   #(0.75, 0.0, 0.0),
                   (1.0, turq[1], turq[1])),

         "blue":  ((0.0, mage[2], mage[2]),
                   #(0.25, 1.0, 1.0),
                   (0.5, 1.0, 1.0),
                   #(0.75, 0.0, 0.0),
                   (1.0, turq[2], turq[2]))
        }

colormap = LinearSegmentedColormap("whatever", cdict3)


### Begin plot
fig = plt.figure(figsize=(7, 7))
n_points = 100

# Generate data
for i in range(9):
    np.random.seed(4)
    ax = fig.add_subplot(3, 3, int(i+1))
    n_dims = 2**(i+1)
    X = np.random.normal(size=(100, n_dims))
    t = np.random.randint(2, size=(100, 1))

    # FIND NORMAL TO HYPERPLANE
    clf = LogisticRegression()
    clf.fit(X, t)
    u1 = clf.coef_[0]
    u1 = u1/np.sqrt(u1.dot(u1))

    # CREATE RANDOM DIRECTION PERPENDICULAR TO U1
    u2 = np.random.normal(size=n_dims)
    u2 = u2 - u1.dot(u2)*u1
    u2 = u2/np.sqrt(u2.dot(u2))

    u = np.vstack([u1, u2])

    # PROJECT ONTO U1, U2 PLANE
    p = u @ X.T
    p2 = u @ X.T

    # PLOT TRAIN DATA (KEEP CORRECT COLOR IN FRONT)
    idx0 = np.flatnonzero(t==0)
    idx1 = np.flatnonzero(t==1)

    ax.scatter(p[0, idx0], p[1, idx0], color="none", edgecolor="turquoise")
    ax.scatter(p[0, idx1], p[1, idx1], color="none", edgecolor="magenta")

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    ax.set_title(f"{n_dims}-dimensional")

ax.text(
    0.6,
    0.04,
    'cookieblues.github.io',
    fontsize=11,
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes,
    color='dimgrey'
)

plt.tight_layout()
plt.savefig("cod_final.png", bbox_inches="tight")
plt.show()