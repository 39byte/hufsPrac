import numpy as np
import matplotlib.pyplot as plt
import scipy

def sin_fun(x, A, B, C):
    return A * np.sin(x + B) + C

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
noise = np.random.random(x.shape) - 0.5
y_noisy = y + noise

popt, pcov = scipy.optimize.curve_fit(sin_fun, x, y_noisy)
A, B, C = popt
y_fit = sin_fun(x, A, B, C)

plt.plot(x,y, color = 'blue', label = "sin(x)")
plt.plot(x,y_noisy, 'ro', label = "noisy")
plt.plot(x, y_fit, 'g--', label = "fitted")

plt.grid(True)
plt.legend()
plt.title("Sin Curve")
plt.show()