import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

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


class QDA:
    def fit(self, X, t):
        self.priors = dict()
        self.means = dict()
        self.covs = dict()
        
        self.classes = np.unique(t)

        for c in self.classes:
            X_c = X[t == c]
            self.priors[c] = X_c.shape[0] / X.shape[0]
            self.means[c] = np.mean(X_c, axis=0)
            self.covs[c] = np.cov(X_c, rowvar=False)

    def predict(self, X):
        preds = list()
        for x in X:
            posts = list()
            for c in self.classes:
                prior = np.log(self.priors[c])
                inv_cov = np.linalg.inv(self.covs[c])
                inv_cov_det = np.linalg.det(inv_cov)
                diff = x-self.means[c]
                likelihood = 0.5*np.log(inv_cov_det) - 0.5*diff.T @ inv_cov @ diff
                post = prior + likelihood
                posts.append(post)
            pred = self.classes[np.argmax(posts)]
            preds.append(pred)
        return np.array(preds)


data = np.loadtxt("../data.csv", delimiter=",", skiprows=1)

X = data[:, 0:2]
t = data[:, 2]

qda = QDA()
qda.fit(X, t)
preds = qda.predict(X)


# Figure
fig = plt.figure(figsize=(8, 8/1.4))
ax = fig.add_subplot(111)

class_clrs = ["magenta", "turquoise"]
alpha = 0.2
for c in qda.classes:
    draw_ellipse(
        qda.means[c],
        qda.covs[c],
        facecolor=class_clrs[int(c)],
        edgecolor="none",
        alpha=alpha,
        zorder=1,
        ax=ax
    )
for c in reversed(qda.classes):
    draw_ellipse(
        qda.means[c],
        qda.covs[c],
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
plt.savefig("preds.svg", bbox_inches="tight")
plt.show()

