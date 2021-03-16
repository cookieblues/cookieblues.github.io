import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import LinearSegmentedColormap
from scipy.constants import golden
from sklearn.linear_model import LogisticRegression, Perceptron

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


fig = plt.figure(figsize=(8/golden, 8/golden))
ax = fig.add_subplot(111)

ax.scatter(X[:5,0], X[:5,1],
    edgecolors = "magenta",
    c = "None",
    s = 17.5,
    marker = "o",
    label = "Class 0",
    zorder = 2
)
ax.scatter(X[5:,0], X[5:,1],
    edgecolors = "turquoise",
    c = "None",
    s = 17.5,
    marker = "o",
    label = "Class 1",
    zorder = 2
)
### 0-0.2
ax.fill_between([0, 0.2], [0.0, 0.0], [0.2, 0.2],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0, 0.2], [0.2, 0.2], [0.4, 0.4],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0, 0.2], [0.4, 0.4], [0.6, 0.6],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0, 0.2], [0.6, 0.6], [0.8, 0.8],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0, 0.2], [0.8, 0.8], [1.0, 1.0],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
### 0.2-0.4
ax.fill_between([0.2, 0.4], [0.0, 0.0], [0.2, 0.2],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.2, 0.4], [0.2, 0.2], [0.4, 0.4],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.2, 0.4], [0.4, 0.4], [0.6, 0.6],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.2, 0.4], [0.6, 0.6], [0.8, 0.8],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.2, 0.4], [0.8, 0.8], [1.0, 1.0],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
### 0.4-0.6
ax.fill_between([0.4, 0.6], [0.0, 0.0], [0.2, 0.2],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.4, 0.6], [0.2, 0.2], [0.4, 0.4],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.4, 0.6], [0.4, 0.4], [0.6, 0.6],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
ax.fill_between([0.4, 0.6], [0.6, 0.6], [0.8, 0.8],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
ax.fill_between([0.4, 0.6], [0.8, 0.8], [1.0, 1.0],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
### 0.6-0.8
ax.fill_between([0.6, 0.8], [0.0, 0.0], [0.2, 0.2],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
ax.fill_between([0.6, 0.8], [0.2, 0.2], [0.4, 0.4],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.6, 0.8], [0.4, 0.4], [0.6, 0.6],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.6, 0.8], [0.6, 0.6], [0.8, 0.8],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.6, 0.8], [0.8, 0.8], [1.0, 1.0],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
### 0.8-1.0
ax.fill_between([0.8, 1.0], [0.0, 0.0], [0.2, 0.2],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.8, 1.0], [0.2, 0.2], [0.4, 0.4],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.8, 1.0], [0.4, 0.4], [0.6, 0.6],
    alpha = 0.2,
    color = "magenta",
    zorder = 1
)
ax.fill_between([0.8, 1.0], [0.6, 0.6], [0.8, 0.8],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)
ax.fill_between([0.8, 1.0], [0.8, 0.8], [1.0, 1.0],
    alpha = 0.2,
    color = "turquoise",
    zorder = 1
)


# model = LogisticRegression(penalty="none",solver="lbfgs",tol=1e-10,max_iter=10*6)
# #model = Perceptron()
# model.fit(X[:,0:2], t)
# inter = model.intercept_
# coef = model.coef_
# xx, yy = np.meshgrid(
#     np.linspace(0, 1, num=1000),
#     np.linspace(0, 1, num=1000)
# )
# preds = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# ax.contour(xx, yy, preds, colors="black", linestyles="solid", linewidths=0.2)
# ax.imshow(preds, cmap=colormap, extent=[0,1,0,1], alpha=0.25, origin="lower")

# def h(x):
#     return 1.169 - 0.835 * x
# x_dec = np.linspace(-0.01,1.01,num=1000)
# y_dec = h(x_dec)
# ax.plot(x_dec,y_dec,linewidth=0.5,color="black",linestyle=(0, (5, 5)))

ax.set_xlim(0.0,1.0)
ax.set_ylim(0.0,1.0)

#ax.legend(frameon=False,loc="upper left")

plt.tight_layout()
plt.savefig("two_dim_cod.png")
plt.show()
