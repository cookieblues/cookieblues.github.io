import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 2, num=20)
y = x ** 3 - x

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y, 'H-g')

plt.tight_layout()
plt.savefig('linescatter.svg', bbox_inches='tight')
plt.show()
