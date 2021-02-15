import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-4, 4, num=20)
y1 = x
y2 = -y1
y3 = y1**2


fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()


ax.scatter(x=x, y=y1, marker="v", s=1000)
ax.scatter(x=x, y=y2, marker="X", s=100)
ax.scatter(x=x, y=y3, marker="s", s=10)


plt.tight_layout()
plt.savefig('markers.svg', bbox_inches='tight')
plt.show()