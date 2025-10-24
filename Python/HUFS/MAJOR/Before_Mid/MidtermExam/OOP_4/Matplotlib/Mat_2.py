import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
x = np.linspace(0, 10, 50)
y1 = np.power(x, 2)
y2 = np.power(x, 3)

plt.plot(x, y1, 'b-', label='$x^2$')
plt.xlim((1, 5))
plt.ylim((0, 30))
plt.xlabel('my x label')
plt.ylabel('my y label')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('plot title , including $\Omega$')
plt.plot(x, y2, 'go', label='$x^3$')
plt.xlim((1, 3))
plt.ylim((0, 30))
plt.legend()


plt.show()