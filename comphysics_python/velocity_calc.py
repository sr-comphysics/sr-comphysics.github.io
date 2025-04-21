# Velocity of an Object Under Constant Acceleration
# Import necessary libraries
import numpy as np  # Import NumPy for numerical operations
from scipy.integrate import odeint as od  # Import the odeint function for solving ordinary differential equations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Initial velocity of the object
vo = 1  # Initial velocity in m/s

# Define the function that computes the derivative of velocity
def velderiv(v, t):
    a = 9.8  # Acceleration due to gravity in m/s^2
    dvdt = a  # The change in velocity (acceleration) is constant
    return dvdt  # Return the derivative

# Create an array of time values from 0 to 3 seconds, with 30 points
times = np.linspace(0, 3, 30)

# Solve the ordinary differential equation for velocity over time
velocity = od(velderiv, vo, times)  # Integrate the velocity derivative

# Plot the velocity as a function of time
plt.plot(times, velocity)  # Create a line plot of velocity vs. time
plt.xlabel("time (sec)")  # Label the x-axis
plt.ylabel("velocity (m/s)")  # Label the y-axis
plt.show()  # Display the plot
