import numpy as np


def gaussian_basis(x, mu, gamma=1):
    return np.exp(-gamma * np.linalg.norm(mu-x)**2)


x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])
M = 4
lambd = 0.0001 # regularization parameter

# Calculate design matrix Phi
Phi = np.ones((t.shape[0], M))
for m in range(M-1):
    mu = m/M
    Phi[:, m+1] = np.vectorize(gaussian_basis)(x, mu)

# Calculate parameters w and alpha
w = np.linalg.inv(lambd * np.identity(M) + Phi.T @ Phi) @ Phi.T @ t
alpha = sum((t - Phi @ w)**2) / len(t)



fig = plt.figure(figsize=(7, 7/1.4))
ax = fig.add_subplot(111)

x_ = np.linspace(x.min()-0.05, x.max()+0.05, 250)

Phi_ = np.ones((x_.shape[0], M))
for m in range(M-1):
    mu = m/M
    Phi_[:, m+1] = gaussian_basis(x_, mu)

t_ = w @ Phi_.T

ax.plot(x_, t_,
    color="darkturquoise",
    linewidth = 1,
    label = "Predicted (mean)"
)

plt.show()
