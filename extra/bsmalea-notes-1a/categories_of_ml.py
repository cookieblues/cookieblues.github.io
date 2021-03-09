import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_blobs, make_classification
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

fig = plt.figure(figsize=(6, 6))
mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")




### CLASSIFICATION PLOT
ax1 = fig.add_subplot(221)

# presets
x_min = -6
x_max = 6
y_min = -6
y_max = 6

turq = mpl.colors.to_rgb("turquoise")
mage = mpl.colors.to_rgb("magenta")
gold = mpl.colors.to_rgb("goldenrod")

cdict3 = {"red":  ((0.0, mage[0], mage[0]),
                   #(0.25, 0.0, 0.0),
                   (0.5, turq[0], turq[0]),
                   #(0.75, 1.0, 1.0),
                   (1.0, gold[0], gold[0])),

         "green": ((0.0, mage[1], mage[1]),
                   #(0.25, 0.0, 0.0),
                   (0.5, turq[1], turq[1]),
                   #(0.75, 0.0, 0.0),
                   (1.0, gold[1], gold[1])),

         "blue":  ((0.0, mage[2], mage[2]),
                   #(0.25, 1.0, 1.0),
                   (0.5, turq[2], turq[2]),
                   #(0.75, 0.0, 0.0),
                   (1.0, gold[2], gold[2]))
        }

colormap = LinearSegmentedColormap("whatever", cdict3)

# dataset
X, t = make_blobs(
    n_samples = 99,
    n_features = 2,
    centers = [[-2.5, -2.5], [0, 0], [2.5, 2.5]],
    random_state = 1
)
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, num=1000),
    np.linspace(y_min, y_max, num=1000)
)

# model
clf = MLPClassifier(
    hidden_layer_sizes = (8, 8,),
    activation = "identity",
    solver = "sgd",
    tol = 2e-6,
    max_iter = 10000,
    random_state = 1
)
clf.fit(X, t)
preds = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# axes
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)

clrs = ["magenta", "turquoise", "goldenrod"]
mrks = ["v", "x", "o"]

ax1.imshow(preds, cmap=colormap, extent=[x_min,x_max,y_min,y_max], alpha=0.25, origin="lower")
ax1.contour(xx, yy, preds, colors="black", linestyles="solid", linewidths=0.2)

for i in range(3):
    X_ = X[np.flatnonzero(t == i)]
    ax1.scatter(X_[:,0], X_[:,1],
        c = clrs[i],
        s = 12.5,
        marker = mrks[i]
    )

ax1.set_title("Classification", fontsize=16)




### REGRESSION PLOT
ax2 = fig.add_subplot(222)

# dataset
X = np.linspace(0, 1, num=70)
t = np.sin(-(3/2) * np.pi * X) + (1/3) * np.sin(5 * np.pi * X)
np.random.seed(4)
t += np.random.normal(loc=0, scale=0.13, size=70) # noise

# model
X_ = np.linspace(0, 1, num=250)
w = np.polyfit(X, t, deg=7)
h = np.poly1d(w)
y = h(X_)


# axes
ax2.plot(X_, y,
    color = "turquoise",
    linewidth = 1
)
ax2.scatter(X, t,
    c = "None",
    s = 12.5,
    marker = "o",
    edgecolors = "magenta"
)

ax2.set_title("Regression", fontsize=16)




### CLUSTERING PLOT
ax3 = fig.add_subplot(223)

# dataset
np.random.seed(1)
X_1 = np.random.multivariate_normal(mean=[5, 5], cov=[[2, 1], [1, 1]], size=70)
np.random.seed(1)
X_2 = np.random.multivariate_normal(mean=[10, 10], cov=[[2, -0.5], [-0.5, 1]], size=50)
X_ = np.concatenate([X_1, X_2], axis=0)

# model
model = KMeans(
    n_clusters = 2,
    random_state = 1,
    algorithm = "full"
)
model.fit(X_)
preds = model.predict(X_)

# axes
ax3.scatter(X_1[:, 0], X_1[:, 1],
    c = "turquoise",
    s = 12.5,
    marker = "o"
)
ax3.scatter(X_2[:, 0], X_2[:, 1],
    c = "turquoise",
    s = 12.5,
    marker = "o"
)

centers = model.cluster_centers_

mean_1 = np.mean(np.linalg.norm(X_[np.flatnonzero(model.labels_ == 0)] - centers[0], axis=1)**2)
mean_2 = np.mean(np.linalg.norm(X_[np.flatnonzero(model.labels_ == 1)] - centers[1], axis=1)**2)

circ_1 = mpl.patches.Circle(
    centers[0],
    fill=False,
    radius=mean_1,
    edgecolor="magenta",
    linewidth=2
)
circ_2 = mpl.patches.Circle(
    centers[1],
    fill=False,
    radius=mean_2,
    edgecolor="magenta",
    linewidth=2
)

ax3.add_artist(circ_1)
ax3.add_artist(circ_2)

ax3.set_title("Clustering", fontsize=16)





### DENSITY ESTIMATION PLOT
ax4 = fig.add_subplot(224)

def draw_ellipse(position, covariance, ax=None, **kwargs):
    """Draw an ellipse with a given position and covariance"""
    ax = ax or plt.gca()

    # Convert covariance to principal axes
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)

    # Draw the Ellipse
    for nsig in range(1, 4):
        ax.add_patch(mpl.patches.Ellipse(position, nsig * width, nsig * height, angle, **kwargs))

# dataset
np.random.seed(3)
X_1 = np.random.multivariate_normal(mean=[-1, 3], cov=[[0.7, -0.5], [-0.5, 0.7]], size=70)
np.random.seed(1)
X_2 = np.random.multivariate_normal(mean=[1, -3], cov=[[1, -0.5], [-0.5, 0.5]], size=70)
X_ = np.concatenate([X_1, X_2], axis=0)

# model
model = GaussianMixture(
    n_components = 2,
    covariance_type = "full",
    random_state = 1
)
model.fit(X_)
means = model.means_
covs = model.covariances_

# axes
ax4.scatter(X_1[:, 0], X_1[:, 1],
    c = "None",
    s = 12.5,
    marker = "o",
    edgecolors = "turquoise"
)
ax4.scatter(X_2[:, 0], X_2[:, 1],
    c = "None",
    s = 12.5,
    marker = "o",
    edgecolors = "turquoise"
)

draw_ellipse(means[0], covs[0], ax=ax4, color="magenta", alpha=0.2)
draw_ellipse(means[1], covs[1], ax=ax4, color="magenta", alpha=0.2)

ax4.set_title("Density estimation", fontsize=16)


#plt.tight_layout()

box1 = ax1.get_position()
box1.x0 = box1.x0 - 0.015
box1.x1 = box1.x1 - 0.015
box1.y0 = box1.y0 + 0.015
box1.y1 = box1.y1 + 0.015
ax1.set_position(box1)

box2 = ax2.get_position()
box2.x0 = box2.x0 + 0.015
box2.x1 = box2.x1 + 0.015
box2.y0 = box2.y0 + 0.015
box2.y1 = box2.y1 + 0.015
ax2.set_position(box2)

box3 = ax3.get_position()
box3.x0 = box3.x0 - 0.015
box3.x1 = box3.x1 - 0.015
box3.y0 = box3.y0 - 0.075
box3.y1 = box3.y1 - 0.075
ax3.set_position(box3)

box4 = ax4.get_position()
box4.x0 = box4.x0 + 0.015
box4.x1 = box4.x1 + 0.015
box4.y0 = box4.y0 - 0.075
box4.y1 = box4.y1 - 0.075
ax4.set_position(box4)


fig.text(0.5,0.965,
    s=r"Supervised learning: $\mathcal{D} = \{ (\mathbf{x}_1, t_1), \dots, (\mathbf{x}_N, t_N ) \}$",
    fontsize = 20,
    horizontalalignment="center",
    verticalalignment="center"
)
fig.text(0.5,0.46,
    s=r"Unsupervised learning: $\mathcal{D} = \{ \mathbf{x}_1, \dots, \mathbf{x}_N \}$",
    fontsize = 20,
    horizontalalignment="center",
    verticalalignment="center"
)

#plt.savefig("categories_of_ml.svg")
plt.show()