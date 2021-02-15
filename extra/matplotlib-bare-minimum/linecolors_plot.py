import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


x = np.linspace(-4, 4, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-1, scale=1), color="magenta")
ax.plot(x, norm.pdf(x, loc=0, scale=1), color=(0.85, 0.64, 0.12))
ax.plot(x, norm.pdf(x, loc=1, scale=1), color="#228B22")

plt.savefig('colours.svg', bbox_inches='tight')
plt.show()