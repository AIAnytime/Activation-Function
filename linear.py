from math import exp
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def linear(x):
    return x

input = [x for x in range(-10,10)]

output = [linear(x) for x in input]

plt.plot(input, output)
plt.savefig('linear.png')