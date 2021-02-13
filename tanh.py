from math import exp
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

#define input value range
input = [x for x in range(-20,20)]

#calculate
output = [tanh(x) for x in input]

#plot
plt.plot(input, output)
plt.savefig('tanh.jpg')