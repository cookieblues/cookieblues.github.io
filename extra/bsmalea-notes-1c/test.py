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

fig = plt.figure(figsize=(7, 7))

for i in range(4):
    ax = fig.add_subplot(2, 2, int(i+1))

    n = 11
    k = 8
    if i == 0:
        a = 1.5
        b = 2
    elif i == 1:
        a = 1.5
        b = 3
    elif i == 2:
        a = 1.5
        b = 4
    else:
        a = 1.5
        b = 5

    X = np.linspace(0, 1, num=1000)
    t = likelihood(X, n, k) * gamma(n+2) / (gamma(k+1)*gamma((n-k)+1)*binom(n, k))
    prior = beta.pdf(X, a, b)
    posterior = beta.pdf(X, a+k, b+(n-k))

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
        label = "Likelihood",
        zorder = 2
    )

    ax.plot(X, posterior,
        color = mix,
        label = "Posterior",
        zorder = 2
    )

    # X axis
    #ax.set_xlabel(r"$\theta$", fontsize=10)
    ax.set_xlim(0, 1)
    x_ticks = [i/4 for i in range(5)]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks)

    # Y axis
    #ax.set_ylabel(r"Pr$(\mathcal{D} | \theta)$")
    #ax.set_ylabel(r"PDF", fontsize=10)
    ax.set_ylim(0, y_max)
    y_ticks = [i for i in range(5)]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_ticks)

    if i == 0:
        ax.legend(
            loc="upper left",
            framealpha=0,
            fontsize=14
        )

plt.tight_layout()
plt.savefig("test.png", bbox_inches="tight")
plt.show()

