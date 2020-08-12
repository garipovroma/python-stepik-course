import matplotlib.pyplot as plt
import math

fig = plt.figure()

plt.axis([0, 10, -1.5, 1.5])

plt.xlabel('x')
plt.ylabel('sin(x)')

xs = []
sin_vals = []

x = 0.0
while x < 10.0:
    sin_vals.append(math.sin(x))
    xs.append(x)
    x += 0.01

plt.plot(xs, sin_vals)

fig.savefig('sin.png')