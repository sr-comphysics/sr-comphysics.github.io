# Calculating Roots of a Quadratic Equation
# Importing the NumPy library for numerical operations
import numpy as np  # Importing NumPy for mathematical functions

# Defining a function to calculate the roots of a quadratic equation
def roots(a, b, c):
    # Calculating the discriminant
    d = np.sqrt(b * b - 4 * a * c)  # Using the quadratic formula to find the discriminant
    # Calculating the two roots using the quadratic formula
    x1 = (-b + d) / (2 * a)  # First root
    x2 = (-b - d) / (2 * a)  # Second root
    # Printing the roots
    print('x1 : {0}'.format(x1))  # Displaying the first root
    print('x2 : {0}'.format(x2))  # Displaying the second root

# Taking user input for the coefficients of the quadratic equation
a = input('Enter a : ')  # Prompting the user to enter the coefficient a
b = input('Enter b : ')  # Prompting the user to enter the coefficient b
c = input('Enter c : ')  # Prompting the user to enter the coefficient c

# Calling the roots function with the user-provided coefficients
roots(float(a), float(b), float(c))  # Converting input to float and passing to the roots function
