import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


x = np.linspace(-2, 9, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

for i in range(1,7):
    ax.plot(x, norm.pdf(x, loc=i, scale=1), color="black", linewidth=i/2)

plt.savefig('linewidths.svg', bbox_inches='tight')
plt.show()