import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(10000)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x)

plt.tight_layout()
plt.savefig('hist.svg', bbox_inches='tight')
plt.show()
