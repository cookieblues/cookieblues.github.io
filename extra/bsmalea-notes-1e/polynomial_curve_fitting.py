import numpy as np
import matplotlib.pyplot as plt 

# Let's first generate some data points.
N_train = 10
X_train = np.linspace(start=0,stop=1,num=N_train)
y_train = np.sin(2*np.pi*X_train) + np.random.normal(0,0.1,10)

beta = 

exit()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X_train,y_train)
plt.show()






