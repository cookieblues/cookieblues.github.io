import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.constants import golden

def sse(true, pred):
    return sum((true-pred)**2)

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

turq = mpl.colors.to_rgb("turquoise")
mage = mpl.colors.to_rgb("magenta")
fg = mpl.colors.to_rgb("forestgreen")
gold = mpl.colors.to_rgb("goldenrod")

cdict3 = {"red":  ((0.0, gold[0], gold[0]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (0.06, 1.0, 1.0),
                   (1.0, fg[0], fg[0])),

         "green": ((0.0, gold[1], gold[1]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (0.06, 1.0, 1.0),
                   (1.0, fg[1], fg[1])),

         "blue":  ((0.0, gold[2], gold[2]),
                   #(0.25, 1.0, 1.0),
                   #(0.5, 1.0, 1.0),
                   (0.06, 1.0, 1.0),
                   (1.0, fg[2], fg[2]))
        }
mycmp = mpl.colors.LinearSegmentedColormap("mycmp", cdict3)


x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])
X = np.vstack([np.ones(x.shape), x]).T

from numpy.linalg import lstsq
w, residuals, rank, singular_vals = lstsq(X,t)
print(w)

w_0_min, w_0_max = w[0]-0.75, w[0]+0.75
w_1_min, w_1_max = w[1]-0.75, w[1]+0.75
#w_0_min, w_0_max = -2, 2
#w_1_min, w_1_max = -1, 4
n_points = 1000

w0,w1 = np.meshgrid(np.linspace(w_0_min,w_0_max,n_points),np.linspace(w_1_min,w_1_max,n_points))
all_ = np.c_[w0.ravel(), w1.ravel()]

reg_vals = [X @ ws for ws in all_]
sse_vals = np.array([sse(t, reg_val) for reg_val in reg_vals])
sse_vals = sse_vals.reshape(w0.shape)


# begin contour
fig = plt.figure(figsize=(7, 7/golden))
ax = fig.add_subplot(111)

con_line = ax.contour(w0,w1,sse_vals,levels=[19,22,25],colors="black",alpha=1.0,linestyles="solid",linewidths=0.75)
ax.clabel(con_line, fmt="%1.0f", use_clabeltext=True, rightside_up=True)

con = ax.imshow(sse_vals,
    extent=[w_0_min, w_0_max, w_1_min, w_1_max],
    origin="lower",
    cmap=mycmp,
    aspect="equal",
    alpha=1.0
)
cbar = plt.colorbar(con,ax=ax,label="SSE")
cbar.set_label(label="SSE",size=14)
cbar.solids.set_edgecolor("face")
ax.scatter(w[0],w[1],color="black",marker="x") # minimum

ax.set_xticks([-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4])
ax.set_xticklabels(["$-0.8$", "$-0.6$", "$-0.4$", "$-0.2$","$0.0$", "$0.2$", "$0.4$"])
#ax.set_yticks([0.6, 1.0, 1.4, 1.8, 2.2])
#ax.set_yticklabels(["$0.7$", "$1.0$", "$1.3$", "$1.6$", "$1.9$", "$2.2$"])
ax.set_xlabel("$w_0$", fontsize=14)
ax.set_ylabel("$w_1$", rotation=0, labelpad=10, fontsize=14)


ax.text(
    0.21,
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
plt.savefig("weights.png", bbox_inches="tight")
plt.show()
