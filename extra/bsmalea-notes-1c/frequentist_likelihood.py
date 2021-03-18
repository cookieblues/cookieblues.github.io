import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import binom


# Set matplotlib font
mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

def likelihood(theta, n, k):
    return binom(n, k) * theta**k * (1-theta)**(n-k)

n = 11
k = 8

X = np.linspace(0, 1, num=1000)
t = likelihood(X, n, k)


fig, ax = plt.subplots(figsize=(7, 7/1.4))

y_max = 0.3

ax.plot(X, t,
    color = "magenta",
    zorder = 2
)

theta_mle = 8/11
likelihood_max = likelihood(theta_mle, n, k)
ax.axvline(theta_mle,
    ymin = 0,
    ymax = likelihood_max/y_max,
    linestyle = "--",
    color = "darkmagenta",
    zorder = 1
)

ax.text(theta_mle, -0.012,
    s = r"$\hat{\theta}_{\mathrm{MLE}}$",
    fontsize = 18,
    horizontalalignment = "center",
    verticalalignment = "center"
)

# X axis
ax.set_xlabel(r"$\theta$", fontsize=14)
ax.set_xlim(0, 1)

# Y axis
#ax.set_ylabel(r"Pr$(\mathcal{D} | \theta)$")
ax.set_ylabel(r"Likelihood", fontsize=14)
ax.set_ylim(0, y_max)
y_ticks = np.linspace(0, y_max, num=6)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

plt.tight_layout()
plt.savefig("frequentist_likelihood.svg", bbox_inches="tight")
plt.show()

