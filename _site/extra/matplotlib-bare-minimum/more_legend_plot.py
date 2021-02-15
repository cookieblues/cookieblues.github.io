import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 2, num=100)
y1 = x
y2 = np.sin(x)+np.cos(x)
y3 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')
ax.plot(x, y3, color='forestgreen', label='Third')

ax.legend(loc='lower center', frameon=False, ncol=3)

plt.tight_layout()
plt.savefig('more_legend.svg', bbox_inches='tight')
plt.show()
