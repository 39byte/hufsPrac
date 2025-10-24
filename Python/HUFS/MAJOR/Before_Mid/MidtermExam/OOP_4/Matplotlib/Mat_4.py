import numpy as np
import matplotlib.pyplot as plt

samp1 = np.random.normal(loc=0., scale=1., size=100)
samp2 = np.random.normal(loc=0., scale=2., size=100)
samp3 = np.random.normal(loc=0., scale=1.2, size=100)

plt.grid(True)
plt.boxplot((samp1, samp2, samp3))
plt.xticks([1, 2, 3], ['sample1', 'sample2', 'sample3'])
plt.show()