import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30, density=True, color='b', alpha= 0.6)
plt.hist(data, bins=30, density=True, color='r', cumulative=True, alpha= 0.2)

plt.show()