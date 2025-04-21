# Numerical Integration of a Function Using the Trapezoidal Rule
# Importing the libraries
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining the step size for the numerical calculation
dx = 0.001  # Setting the increment for the x values

# Creating an array of x values from 0 to 10 with the defined step size
x = np.arange(0, 10, dx)  # Generating x values in the range [0, 10)

# Calculating the function values y = sqrt(x) * exp(-x)
y = x**(0.5) * np.exp(-x)  # Computing the function for each x value

# Plotting the function
plt.plot(x, y, color='k')  # Creating a line plot of y vs. x in black color
plt.xlabel('x')  # Labeling the x-axis
plt.show()  # Displaying the plot

# Calculating the integral using the trapezoidal rule
print("Integral = %8.7f" % (np.sum(y) * dx))  # Printing the numerical approximation of the integral
