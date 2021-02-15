import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


x = np.linspace(-6, 6, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-3, scale=1), linestyle="solid")
ax.plot(x, norm.pdf(x, loc=-1, scale=1), linestyle="dotted")
ax.plot(x, norm.pdf(x, loc=1, scale=1), linestyle="dashed")
ax.plot(x, norm.pdf(x, loc=3, scale=1), linestyle="dashdot")

plt.savefig('linestyles.svg', bbox_inches='tight')
plt.show()