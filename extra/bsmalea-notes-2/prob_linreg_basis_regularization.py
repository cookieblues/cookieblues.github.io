import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.constants import golden
from sklearn.preprocessing import StandardScaler

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
fig = plt.figure(figsize=(7, 7/golden))

Ms = [8, 8, 8, 8]
lambdas = [0, 10e-5, 10e-4, 10e-3]
for idx, M in enumerate(Ms):
    lambda_reg = lambdas[idx]
    Phi = np.ones((t.shape[0], M))
    mus = [m/M for m in range(1,M)]

    for m in range(M-1):
        Phi[:, m+1] = np.vectorize(gaussian_basis)(x, mus[m])

    #w, residuals, rank, s = np.linalg.lstsq(Phi.T @ Phi + lambda_reg * np.identity(M), Phi.T @ t, rcond=-1)
    #from sklearn.linear_model import Ridge
    
    #w = Ridge(alpha=lambda_reg, fit_intercept=False).fit(Phi, t).coef_
    w = np.linalg.inv(lambda_reg * np.identity(M) + Phi.T @ Phi) @ Phi.T @ t
    #w = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t

    alpha = sum((t - Phi @ w)**2) / len(t)
    h = np.vectorize(lambda w, phi: w @ phi, signature="(m),(n,m)->(n)")

    x_ = np.linspace(x.min()-0.05, x.max()+0.05, 250)
    Phi_ = np.ones((x_.shape[0], M))
    for m in range(M-1):
        Phi_[:, m+1] = np.vectorize(gaussian_basis)(x_, mus[m])
    t_ = w @ Phi_.T


    ax = fig.add_subplot(2, 2, int(idx+1))

    plot_homogen_prob_density(x_, t_, alpha, ax=ax, cmap=mycmp, alpha=1)
    ax.scatter(x, t,
        edgecolors = "magenta",
        c = "None",
        s = 12.5,
        marker = "o",
        zorder = 3
    )
    ax.plot(x_, t_,
        color="darkturquoise",
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

    if lambda_reg == 10e-5:
        tex_lambda = "10^{-5}"
    elif lambda_reg == 10e-4:
        tex_lambda = "10^{-4}"
    elif lambda_reg == 10e-3:
        tex_lambda = "10^{-3}"
    else:
        tex_lambda = "0"

    ax.text(0.5, -3.5,s=r"$\lambda={}$".format(tex_lambda))
    ax.text(0.5, -5,s=r"$M={}$".format(M))
    ax.set_xlim(x.min()-0.05, x.max()+0.05)
    ax.set_ylim(t.min()-0.5, t.max()+0.5)

    if idx==0:
        ax.legend(frameon=False)


plt.tight_layout()
plt.savefig("prob_linreg_basis_regularization.png", bbox_inches="tight")
plt.show()


