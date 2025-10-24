import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

t = np.linspace(0, 20, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='red')
plt.show()