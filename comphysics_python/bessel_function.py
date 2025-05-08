"""
Topic: Bessel Functions Demonstration and Visualization

This program demonstrates various functionalities from the SciPy library related to
Bessel functions. It includes:
  - Calculation of the Bessel functions of the first kind (Jn) and second kind (Yn) at given points.
  - Extraction and display of the zeros of the Bessel function of the first kind.
  - Plotting the Bessel functions (J0 through J3) over a defined range using different
    line styles and markers for visual distinction.
"""

# Import required functions and libraries:
from scipy.special import jn, yn, jn_zeros, yn_zeros  # Import Bessel functions and zeros from SciPy
import numpy as np                                  # Import NumPy for numerical operations
import matplotlib.pyplot as plt                     # Import Matplotlib for plotting

# Set the order of the Bessel function and the evaluation point.
n = 0        # Order of the Bessel function (J_0 and Y_0)
x = 0.0      # Evaluation point

# Calculate and print the value of the Bessel function of the first kind, J_n(x), at x = 0.0.
print("J_%d(%f)= %f" % (n, x, jn(n, x)))  # Expected: J_0(0.0)= 1.000000 (since J_0(0)=1)

# Change the evaluation point for the Neumann (Bessel function of the second kind).
x = 1.0      # Now set x = 1.0 for evaluating Y_n(x)
print("Y_%d(%f)= %f" % (n, x, yn(n, x)))  # Print the value of Y_0(1.0)

# Extract zeros for the Bessel function of the first kind
n = 0   # Reset the order (here it's J_0)
m = 4   # Number of zeros to compute for J_0(x)
zeros = jn_zeros(n, m)  # Compute the first m zeros of J_0
print("Zeros of Bessel function J_%d: %s" % (n, zeros))  # Display the computed zeros

# Generate x values using NumPy for plotting Bessel functions
x = np.linspace(0, 10, 50)  # Create an array of 50 equally spaced points between 0 and 10

# Define markers and line styles for differentiating between plotted series.
markers = ["o", "s", "*", "+"]                     # Markers for plotting different orders
line_styles = ['-', '--', '-.', ':']                # Different line styles for visual variety

# Create a Matplotlib figure and an axes object for plotting.
fig, ax = plt.subplots()

# Loop through the first 4 orders (0, 1, 2, and 3) of Bessel functions Jn.
for n in range(4):
    # Plot the Bessel function J_n(x) for each order using specific marker and line style.
    ax.plot(x, jn(n, x), ls=line_styles[n], marker=markers[n],
            label=r"$J_%d(x)$" % n)  # Use LaTeX formatting for the legend label

# Add a legend to the plot to identify each line by Bessel function order.
ax.legend()

# Display the final plot.
plt.show()
