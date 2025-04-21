# Lanczos Algorithm for Tridiagonal Matrix Construction
import numpy as np  # Import the NumPy library for numerical operations
from numpy.random import random as rd  # Import the random function from NumPy for generating random numbers
from numpy.linalg import norm as nm  # Import the norm function from NumPy for calculating vector norms

# Define a complex matrix A
A = np.array([[2, -1+1j, -0.5j, 4.25],
              [-1-1j, 4, 1, 7],
              [0.5j, 1, 2, -1+2j],
              [4.25, 7, -1-2j, 1.4]])

N = len(A)  # Get the size of the matrix A (number of rows/columns)
I = np.identity(N)  # Create an identity matrix of size N

# Generate a random starting vector x of size N
x = rd(N)

# Initialize coefficients for the Lanczos iteration
qii = 0  # Previous q value (q_{i-1})
a = [0]  # List to store a coefficients, starting with a_0
b = [nm(x)]  # List to store b coefficients, starting with b_0 as the norm of x

# Lanczos iteration loop
for i in range(1, N + 1):
    # Calculate the normalized vector q_i
    qi = x / b[i - 1]  # Normalize x by the previous b value

    # Append the value of a_i = q_i^* * A * q_i to the list
    a.append(np.conj(qi).dot(A.dot(qi)))

    # Orthogonalize A.q_i
    x = np.dot((A - a[i] * I), qi) - b[i - 1] * qii  # Update x for the next iteration

    # Append b_i = |x| if i < N
    if i < N:
        b.append(nm(x))  # Append the norm of x to the b list

        # Store the current qi as qii for the next iteration
        qii = qi

# Drop the initial values and remove any small complex round-off error present
a = np.real_if_close(a[1:])  # Keep only the relevant a coefficients
b = np.real_if_close(b[1:])  # Keep only the relevant b coefficients

# Construct the tridiagonal matrix T using the a and b coefficients
T = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)  # Create the tridiagonal matrix

# Print the resulting tridiagonal matrix T
print(T)  # Output the tridiagonal matrix
