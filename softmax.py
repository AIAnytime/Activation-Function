from math import exp

def softmax(x):
    return exp(x) / exp(x).sum()

input = [1, 5, 3]

output = softmax(input)

print(output)
print(output.sum())