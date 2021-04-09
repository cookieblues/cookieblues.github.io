import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec


mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

class LDA:
    def fit(self, X, t):
        self.priors = dict()
        self.means = dict()
        self.cov = np.cov(X, rowvar=False)
        
        self.classes = np.unique(t)

        for c in self.classes:
            X_c = X[t == c]
            self.priors[c] = X_c.shape[0] / X.shape[0]
            self.means[c] = np.mean(X_c, axis=0)
            
    def predict(self, X):
        preds = list()
        for x in X:
            posts = list()
            for c in self.classes:
                prior = np.log(self.priors[c])
                inv_cov = np.linalg.inv(self.cov)
                inv_cov_det = np.linalg.det(inv_cov)
                diff = x-self.means[c]
                likelihood = 0.5*np.log(inv_cov_det) - 0.5*diff.T @ inv_cov @ diff
                post = prior + likelihood
                posts.append(post)
            pred = self.classes[np.argmax(posts)]
            preds.append(pred)
        return np.array(preds)


    def predict_prob(self, X):
        probs = np.zeros((X.shape[0], len(self.classes)))
        for idx, x in enumerate(X):
            posts = list()
            for c in self.classes:
                prior = np.log(self.priors[c])
                inv_cov = np.linalg.inv(self.cov)
                inv_cov_det = np.linalg.det(inv_cov)
                diff = x-self.means[c]
                likelihood = 0.5*np.log(inv_cov_det) - 0.5*diff.T @ inv_cov @ diff
                post = prior + likelihood
                posts.append(post)
            probs[idx] = np.array(posts) / np.array(posts).sum()
        return np.array(probs)


data = np.loadtxt("../data.csv", delimiter=",", skiprows=1)

X = data[:, 0:2]
t = data[:, 2]

lda = LDA()
lda.fit(X, t)
preds = lda.predict(X)


# Figure
fig = plt.figure(figsize=(700/96, 1.2*700/96))
gs = GridSpec(3, 2, figure=fig)

# DATA
ax = fig.add_subplot(gs[0, 0])
ax.scatter(
    x = X[t == 0, 0],
    y = X[t == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.8,
    label = "Class 0"
)
ax.scatter(
    x = X[t == 1, 0],
    y = X[t == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.8,
    label = "Class 1"
)
ax.scatter(
    x = X[t == 0, 0],
    y = X[t == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.4
)
ax.scatter(
    x = X[t == 1, 0],
    y = X[t == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.4
)

ax.axis("equal")

xticks = range(-4, 6, 2)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, fontsize=12)

yticks = range(-4, 5)
ax.set_ylim(-4, 4)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=12)

ax.set_title("Data", fontsize=14)


# DISTRIBUTIONS
ax = fig.add_subplot(gs[0, 1])

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

class_clrs = ["magenta", "turquoise"]
alpha = 0.2
for c in lda.classes:
    draw_ellipse(
        lda.means[c],
        lda.cov,
        facecolor=class_clrs[int(c)],
        edgecolor="none",
        alpha=alpha,
        zorder=1,
        ax=ax
    )
for c in reversed(lda.classes):
    draw_ellipse(
        lda.means[c],
        lda.cov,
        facecolor=class_clrs[int(c)],
        edgecolor="none",
        alpha=alpha/2,
        zorder=1,
        ax=ax
    )

ax.scatter(
    x = X[preds == 0, 0],
    y = X[preds == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.8,
    label = "Pred 0",
    zorder=2
)
ax.scatter(
    x = X[preds == 1, 0],
    y = X[preds == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.8,
    label = "Pred 1",
    zorder=2
)
ax.scatter(
    x = X[preds == 1, 0],
    y = X[preds == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.4,
    zorder=2
)
ax.scatter(
    x = X[preds == 0, 0],
    y = X[preds == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.4,
    zorder=2
)

ax.axis("equal")

xticks = range(-4, 6, 2)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, fontsize=12)

yticks = range(-3, 4)
ax.set_ylim(-3.7, 3.7)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=12)

ax.set_title("Class distributions", fontsize=14)



# DECISION BOUNDARY
ax = fig.add_subplot(gs[1:3, 0:2])

white = mpl.colors.to_rgb("whitesmoke")
dturq = mpl.colors.to_rgb("darkturquoise")
turq = mpl.colors.to_rgb("turquoise")
dmage = mpl.colors.to_rgb("darkmagenta")
mage = mpl.colors.to_rgb("magenta")

cdict3 = {"red":  ((0.0, dmage[0], dmage[0]),
                   (0.375, mage[0], mage[0]),
                   (0.5, white[0], white[0]),
                   (0.625, turq[0], turq[0]),
                   (1.0, dturq[0], dturq[0])),

         "green": ((0.0, dmage[1], dmage[1]),
                   (0.375, mage[1], mage[1]),
                   (0.5, white[1], white[1]),
                   (0.625, turq[1], turq[1]),
                   (1.0, dturq[1], dturq[1])),

         "blue":  ((0.0, dmage[2], dmage[2]),
                   (0.375, mage[2], mage[2]),
                   (0.5, white[2], white[2]),
                   (0.625, turq[2], turq[2]),
                   (1.0, dturq[2], dturq[2])),
         "alpha": ((0.0, 0.4, 0.4),
                    (1.0, 0.4, 0.4)),
        }

colormap = LinearSegmentedColormap("whatever", cdict3)

def decision_contour(model, X, y, fig, ax, cmap=colormap, alpha=0.4):
    cm = cmap
    y_color = np.array([1.0 if target == 1 else 0.0 for target in y])


    x_points, y_points = fig.get_size_inches()*fig.dpi / 10
    x_points = int(x_points)
    y_points = int(y_points)
    
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 1*x_points), np.linspace(y_min, y_max, 1*y_points))
    all_ = np.c_[xx.ravel(),  yy.ravel()]

    probs = model.predict_prob(all_)
    probs = probs[:, 0].reshape(xx.shape)
    con = ax.imshow(probs, extent=[x_min, x_max, y_min, y_max], origin="lower", cmap=cm, aspect="auto", vmin=0, vmax=1)
    cbar = plt.colorbar(con, ax=ax)
    cbar.solids.set_rasterized(True)
    #cbar.solids.set_edgecolor("face")


# # Scatter
ax.scatter(
    x = X[t == 0, 0],
    y = X[t == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.8,
    label = "Pred 0",
    zorder=2
)
ax.scatter(
    x = X[t == 1, 0],
    y = X[t == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.8,
    label = "Pred 1",
    zorder=2
)
ax.scatter(
    x = X[t == 1, 0],
    y = X[t == 1, 1],
    c = "none",
    edgecolor = "turquoise",
    alpha = 0.4,
    zorder=2
)
ax.scatter(
    x = X[t == 0, 0],
    y = X[t == 0, 1],
    c = "none",
    edgecolor = "magenta",
    alpha = 0.4,
    zorder=2
)

ax.axis("equal")

xticks = range(-4, 6, 2)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, fontsize=12)

yticks = range(-3, 4)
ax.set_ylim(-3.7, 3.7)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=12)

decision_contour(lda, X, t, fig, ax, cmap=colormap)

ax.set_title("Decision boundary", fontsize=14)





plt.tight_layout()
plt.savefig("preds.svg", bbox_inches="tight")
plt.show()

