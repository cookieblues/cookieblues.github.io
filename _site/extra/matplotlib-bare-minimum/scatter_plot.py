import matplotlib.pyplot as plt
import numpy as np


#fig = plt.figure(figsize=(8, 5))
#ax = fig.add_subplot()

x = np.linspace(-3, 3, num=100)
y = np.sin(x)


plt.plot(x, y)


plt.savefig("smooth_line_plot.svg")
plt.show()
