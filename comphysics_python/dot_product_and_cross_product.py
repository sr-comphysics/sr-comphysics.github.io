#importig module
import numpy as np
# Declare two variables a & b and assign a list of value using numpy array function (any 3 data)
a = np.array([5,7,3])
b = np.array([0,4,2])
dot = np.dot(a, b) #Dot product (scalar)
print("Dot product = ", dot, "\n")
cross = np.cross(a, b)
print("Cross product = ", cross) # Cross Product (vector)