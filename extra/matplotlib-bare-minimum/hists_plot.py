import matplotlib.pyplot as plt
import numpy as np


x1 = np.random.randn(10000)-1
x2 = np.random.randn(10000)+1

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x1, color='turquoise', edgecolor='none', bins=50, alpha=0.5, density=True)
ax.hist(x2, color='magenta', edgecolor='none', bins=200, alpha=0.5, density=True)

plt.tight_layout()
plt.savefig('hists.svg', bbox_inches='tight')
plt.show()
