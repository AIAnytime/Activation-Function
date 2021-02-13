import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

#Defining the relu activation function
def rectified_linear_unit(x):
    return max(0, x)

#define input data in a range of -10 and 10
data = [x for x in range(-8,8)]

#calculing outputs
output = [rectified_linear_unit(x) for x in data]

#plot data vs outputs

plt.plot(data, output)
plt.savefig('relu_function.jpg')

"""When using the ReLU function for hidden layers, it is a good practice to use a “He Normal” or “He Uniform” weight initialization and scale input data to the range 0-1 (normalize) prior to training."""
