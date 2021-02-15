import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 2, num=100)
y1 = x
y2 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')

ax.legend()

plt.tight_layout()
plt.savefig('legend.svg', bbox_inches='tight')
plt.show()
