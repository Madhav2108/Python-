import numpy as np
# Create an array of ones
a=np.ones((3,4))
print(a)
# Create an array of zeros
a=np.zeros((2,3,4),dtype=np.int16)
print(a)
# Create an array with random values
a=np.random.random((2,2))
print(a)
# Create an empty array
a=np.empty((3,2))
print(a)
# Create a full array
a=np.full((2,2),7)
print(a)
# Create an array of evenly-spaced values
a=np.arange(10,25,5)
print(a)
# Create an array of evenly-spaced values
a=np.linspace(0,2,9)
print(a)
