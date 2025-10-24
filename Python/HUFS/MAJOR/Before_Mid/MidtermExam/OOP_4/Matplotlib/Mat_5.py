import numpy as np
import matplotlib.pyplot as plt

A = np.random.random((100, 100))

plt.imshow(A, cmap="coolwarm")
plt.colorbar()

plt.show()