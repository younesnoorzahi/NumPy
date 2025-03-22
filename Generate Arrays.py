import numpy as np

# Create an array of zeros
zeros = np.zeros((3, 3))
print("Zeros:\n", zeros)

# Create an array of ones
ones = np.ones((2, 2))
print("Ones:\n", ones)

# Create an identity matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# Create an array with a range of values
range_arr = np.arange(0, 10, 2)  # Start, Stop, Step
print("Range Array:", range_arr)

# Create an array with evenly spaced values
linspace_arr = np.linspace(0, 1, 5)  # Start, Stop, Number of points
print("Linspace Array:", linspace_arr)
