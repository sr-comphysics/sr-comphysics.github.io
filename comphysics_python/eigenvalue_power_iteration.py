# Power Iteration Method for Finding the Dominant Eigenvalue and Eigenvector
import numpy as np  # Import the NumPy library for numerical operations

# Function to calculate the Rayleigh quotient
def rayleigh_quotient(A, x):
    # Return the Rayleigh quotient, which is the ratio of the quadratic form to the norm of the vector
    return np.dot(x, np.dot(A, x)) / np.dot(x, x)

# Function to normalize a vector
def normalise(x, eps=1e-10):
    # Calculate the norm of the vector
    N = np.sqrt(np.sum(abs(x)**2))
    if N < eps:  # Check if the vector is close to the zero vector
        return x  # Return the original vector if it is zero
    else:
        return x / N  # Return the normalized vector

# Define a complex matrix A
A = np.array([[6, -1j, 2],
              [1j, 2, 4 + 7j],
              [3, 2 - 7j, -2]])

# Choose the starting vector and normalize it
x = normalise(np.array([1, 1, 1]))
RQnew = rayleigh_quotient(A, x)  # Calculate the initial Rayleigh quotient
RQold = 0  # Initialize the old Rayleigh quotient

# Perform the power iteration to find the dominant eigenvalue and eigenvector
while np.abs(RQnew - RQold) > 1e-6:  # Continue until convergence
    RQold = RQnew  # Update the old Rayleigh quotient
    x = normalise(np.dot(A, x))  # Update the vector by multiplying with A and normalizing
    RQnew = rayleigh_quotient(A, x)  # Calculate the new Rayleigh quotient

# Print the dominant eigenvector and eigenvalue
print("Dominant eigenvector:", x)  
print("Dominant eigenvalue: {:.5f}".format(RQnew))  
