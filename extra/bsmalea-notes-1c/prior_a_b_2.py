import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import binom, gamma
from scipy.stats import beta

# turq 06C2AC, mag C20076, mixed 646191

# Set matplotlib font
mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

def likelihood(theta, n, k):
    return binom(n, k) * theta**k * (1-theta)**(n-k)

n = 11
k = 8
a = 2
b = 2

X = np.linspace(0, 1, num=1000)
t = likelihood(X, n, k) * gamma(n+2) / (gamma(k+1)*gamma((n-k)+1)*binom(n, k))
prior = beta.pdf(X, a, b)
posterior = beta.pdf(X, a+k, b+(n-k))

fig, ax = plt.subplots(figsize=(7, 7/1.4))
y_max = 4


turq = mpl.colors.to_rgb("turquoise")
mag = mpl.colors.to_rgb("magenta")
mix = [(turq[i]+mag[i])/2 for i in range(3)]
ax.plot(X, prior,
    color = turq,
    label = "Prior",
    zorder = 2
)

ax.plot(X, t,
    color = mag,
    label = "Likelihood (normalized)",
    zorder = 2
)

ax.plot(X, posterior,
    color = mix,
    label = "Posterior",
    zorder = 2
)
theta_map = (a+k-1) / (a+b+n-2)
posterior_max = beta.pdf(theta_map, a+k, b+(n-k))
ax.axvline(theta_map,
    ymin = 0,
    ymax = posterior_max/y_max,
    linestyle = "--",
    color = [mix[i]/2 for i in range(3)],
    zorder = 1
)
ax.text(theta_map, -0.16,
    s = r"$\hat{\theta}_{\mathrm{MAP}}$",
    fontsize = 18,
    horizontalalignment = "center",
    verticalalignment = "center"
)

# X axis
ax.set_xlabel(r"$\theta$", fontsize=14)
ax.set_xlim(0, 1)

# Y axis
#ax.set_ylabel(r"Pr$(\mathcal{D} | \theta)$")
ax.set_ylabel(r"PDF", fontsize=14)
ax.set_ylim(0, y_max)
#y_ticks = [i*4/100 for i in range(6)]
#ax.set_yticks(y_ticks)
#ax.set_yticklabels(y_ticks)

ax.legend(
    loc="upper left",
    framealpha=0,
    fontsize=12
)

plt.tight_layout()
plt.savefig("prior_a_b_2.svg", bbox_inches="tight")
plt.show()

