# Symbolic Integration of a Function Using SymPy
# Importing the necessary libraries
import sympy as sp  # Importing SymPy for symbolic mathematics

# Defining the symbolic variable
x = sp.Symbol('x')  # Creating a symbolic variable x for integration

# Performing the definite integral of the function x^(0.5) * exp(-x) from 0 to infinity
y = sp.integrate(x**(0.5) * sp.exp(-x), (x, 0, sp.oo))  # Calculating the integral

# Printing the result of the integral
print(y)  # Displaying the value of the integral
