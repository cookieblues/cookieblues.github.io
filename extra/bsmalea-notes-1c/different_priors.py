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
        a = 1
        b = 1
        ax.text(
            0.7,
            0.025,
            'cookieblues.github.io',
            fontsize=11,
            horizontalalignment='center',
            verticalalignment='center',
            transform=ax.transAxes,
            color='dimgrey',
            zorder=5
        )
    elif i == 1:
        a = 2
        b = 2
    elif i == 2:
        a = 5
        b = 5
    else:
        a = 5
        b = 2

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
        label = "Likelihood (normalized)",
        zorder = 2
    )

    ax.plot(X, posterior,
        color = mix,
        label = "Posterior",
        zorder = 2
    )

    # X axis
    ax.set_xlabel(r"$\theta$", fontsize=10)
    ax.set_xlim(0, 1)

    # Y axis
    #ax.set_ylabel(r"Pr$(\mathcal{D} | \theta)$")
    ax.set_ylabel(r"PDF", fontsize=10)
    ax.set_ylim(0, y_max)
    #y_ticks = [i*4/100 for i in range(6)]
    #ax.set_yticks(y_ticks)
    #ax.set_yticklabels(y_ticks)

    if i == 0:
        ax.text(0.2, 1.15,
            s = r"Beta(1, 1)",
            fontsize = 12,
            horizontalalignment = "center",
            verticalalignment = "center"
        )
    elif i == 1:
        ax.text(0.2, 1.15,
            s = r"Beta(2, 2)",
            fontsize = 12,
            horizontalalignment = "center",
            verticalalignment = "center"
        )
    elif i == 2:
        ax.text(0.2, 1.15,
            s = r"Beta(5, 5)",
            fontsize = 12,
            horizontalalignment = "center",
            verticalalignment = "center"
        )
    else:
        ax.text(0.2, 1.15,
            s = r"Beta(5, 2)",
            fontsize = 12,
            horizontalalignment = "center",
            verticalalignment = "center"
        )

    if i == 0:
        ax.legend(
            loc="upper left",
            framealpha=0,
            fontsize=10
        )



plt.tight_layout()
plt.savefig("different_priors.png", bbox_inches="tight")
plt.show()

