# Simulation of Motion with Linear Air Resistance
# Import necessary libraries
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Define constants for mass, air resistance coefficient, and gravitational acceleration
m, k, g = 1.0, 0.2, 9.8  # m: mass (kg), k: air resistance coefficient (kg/s), g: acceleration due to gravity (m/s^2)

# Define time step and maximum simulation time
dt = 0.01  # Time step (s)
tmax = 30.0  # Maximum time for the simulation (s)
num_steps = int(tmax / dt)  # Total number of time steps

# Define the function for the derivative of position with respect to time
def dxdt(vel):
    return vel  # The rate of change of position is equal to velocity

# Define the function for the derivative of velocity with respect to time
def dvdt(vel):
    return g - k/m * vel  # The rate of change of velocity is affected by gravity and air resistance

# Initialize arrays to store position and velocity over time
x = np.zeros(num_steps + 1)  # Position array
v = np.zeros(num_steps + 1)  # Velocity array

# Time integration loop using Euler's method
for i in range(1, num_steps + 1):
    x[i] = x[i - 1] + dt * dxdt(v[i - 1])  # Update position
    v[i] = v[i - 1] + dt * dvdt(v[i - 1])  # Update velocity

# Create an array of time values for plotting
time = np.arange(0, tmax + dt, dt)

# Create subplots for position and velocity
fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # Create a figure with 1 row and 2 columns

# Plot position vs. time
axes[0].plot(time, x)  # Plot position
axes[0].set_xlabel("time, s")  # Label x-axis
axes[0].set_ylabel("x, m")  # Label y-axis

# Plot velocity vs. time
axes[1].plot(time, v)  # Plot velocity
axes[1].set_xlabel("time, s")  # Label x-axis
axes[1].set_ylabel("v, m/s")  # Label y-axis

# Save the figure as an EPS file
fig.savefig("linear_air_resistance.eps")  # Save the plot to a file
