import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden
from scipy.stats import norm

# x = np.linspace(-4, 4, num=100)

# fig = plt.figure(figsize=(6,6/golden))
# ax = fig.add_subplot()

# ax.plot(x, norm.pdf(x, loc=-1, scale=1), color="magenta")
# ax.plot(x, norm.pdf(x, loc=0, scale=1), color=(0.85, 0.64, 0.12))
# ax.plot(x, norm.pdf(x, loc=1, scale=1), color="#228B22")

# plt.tight_layout()
# plt.savefig("colours.svg")
# plt.show()




# x = np.linspace(-6, 6, num=100)

# fig = plt.figure(figsize=(6,6/golden))
# ax = fig.add_subplot()

# ax.plot(x, norm.pdf(x, loc=-3, scale=1), linestyle="solid")
# ax.plot(x, norm.pdf(x, loc=-1, scale=1), linestyle="dotted")
# ax.plot(x, norm.pdf(x, loc=1, scale=1), linestyle="dashed")
# ax.plot(x, norm.pdf(x, loc=3, scale=1), linestyle="dashdot")

# plt.tight_layout()
# plt.savefig("linestyles.svg")
# plt.show()



x = np.linspace(-2, 9, num=100)

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

for i in range(1,7):
    ax.plot(x, norm.pdf(x, loc=i, scale=1), color="black", linewidth=i/2)

plt.tight_layout()
plt.savefig("linewidths.svg")
plt.show()
