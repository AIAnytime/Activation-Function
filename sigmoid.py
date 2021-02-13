import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from math import exp




#define the function of sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

#input data
data = [x for x in range(-15, 15)]

#calculate the function
output = [sigmoid(x) for x in data]

#plot the graph
plt.plot(data, output)
plt.savefig('sigmoid.jpg')
