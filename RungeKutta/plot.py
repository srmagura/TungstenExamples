import numpy as np
import matplotlib.pyplot as plt
import math

def eval_y(t):
    return math.exp(t / 2) * math.sin(5*t)

h = 0.025
t_exact_array = np.arange(0, 9+h, h)
y_exact_array = np.array([eval_y(t) for t in t_exact_array])
plt.plot(t_exact_array, y_exact_array, label='Exact solution')

t_array = []
y_array = []

with open('data.txt') as infile:
    for line in infile.readlines():
        parts = line.split(',')
        t_array.append(float(parts[0]))
        y_array.append(float(parts[1]))

plt.plot(t_array, y_array, label='Numerical solution', marker='o', linestyle='none', markersize=4)

N = len(t_array) - 1
plt.title('N = {}'.format(N))

plt.legend()
plt.show()

