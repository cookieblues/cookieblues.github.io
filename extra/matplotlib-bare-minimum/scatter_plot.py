import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

x = np.linspace(-3, 3, num=100)
y = np.sin(x)


ax.plot(x, y)

plt.tight_layout()
plt.savefig("smooth_line_plot.svg")
plt.show()
