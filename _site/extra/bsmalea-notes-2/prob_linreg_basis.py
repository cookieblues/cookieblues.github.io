import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")

turq = mpl.colors.to_rgb("turquoise")
cdict3 = {"red":  ((0.0, turq[0], turq[0]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         "green": ((0.0, turq[1], turq[1]),
                   #(0.25, 0.0, 0.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         "blue":  ((0.0, turq[2], turq[2]),
                   #(0.25, 1.0, 1.0),
                   #(0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0))
        }
mycmp = mpl.colors.LinearSegmentedColormap("mycmp", cdict3)

x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])

def f(x):
    return 3*np.sin((1/2)*np.pi * x) - 2*np.sin((3/2) * np.pi * x)

def gaussian_basis(x, mu, gamma=1):
    return np.exp(-gamma * np.linalg.norm(mu-x)**2)

def plot_homogen_prob_density(x, y, variance, ax, l=1000, **kwargs):
    y_min, y_max = y.min()-2*np.sqrt(variance), y.max()+2*np.sqrt(variance)
    yy = np.linspace(y_min, y_max, l)
    a = [np.exp(-(y_-yy)**2/variance) / np.sqrt(variance) for y_ in y]
    a = np.array(a).reshape(len(y), l)
    ax.imshow(
        -a.T,
        aspect="auto",
        origin="lower",
        extent=(x.min(), x.max(), y_min, y_max),
        **kwargs
    )


### figure
fig = plt.figure(figsize=(6,6/golden))

Ms = [2, 4, 6, 8]
for idx, M in enumerate(Ms):
    Phi = np.ones((t.shape[0], M))
    mus = [m/M for m in range(1,M)]

    for m in range(M-1):
        Phi[:, m+1] = np.vectorize(gaussian_basis)(x, mus[m])

    w = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t
    #w, residuals, rank, s = np.linalg.lstsq(Phi, t)
    alpha = sum((t - Phi @ w)**2) / len(t)

    h = np.vectorize(lambda w,phi: w @ phi, signature="(m),(n,m)->(n)")

    x_ = np.linspace(x.min()-0.05, x.max()+0.05, 250)
    Phi_ = np.ones((x_.shape[0], M))
    for m in range(M-1):
        Phi_[:, m+1] = np.vectorize(gaussian_basis)(x_, mus[m])
    t_ = w @ Phi_.T


    ax = fig.add_subplot(2, 2, int(idx+1))

    plot_homogen_prob_density(x_, t_, alpha, ax=ax, cmap=mycmp, alpha=0.625)
    ax.scatter(x, t,
        edgecolors = "magenta",
        c = "None",
        s = 12.5,
        marker = "o",
        zorder = 3
    )
    ax.plot(x_, t_,
        color="turquoise",
        linewidth = 1,
        label = "Predicted (mean)"
    )
    true = np.linspace(x.min()-0.05, x.max()+0.05, 250)
    ax.plot(
        true, f(true),
        color="magenta",
        linewidth = 1,
        label = "True"
    )
    ax.text(0.6, -5, s=r"$M={}$".format(M))
    ax.set_xlim(x.min()-0.05, x.max()+0.05)
    ax.set_ylim(t.min()-0.5, t.max()+0.5)
    ax.legend(frameon=False,loc=2)


plt.tight_layout()
plt.savefig("prob_linreg_basis.svg")
plt.show()


