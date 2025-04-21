# Visualization of the Lorenz Attractor
# Import necessary libraries
import numpy as np  # Import NumPy for numerical operations
from scipy.integrate import odeint as od  # Import the odeint function for solving ordinary differential equations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit from Matplotlib
# Define parameters for the Lorenz system
sigma = 10.0  # The sigma parameter
b = 8 / 3.0  # The b parameter
r = 28.0  # The r parameter
# Define the Lorenz system of equations as a function
f = lambda x, t: [
    sigma * (x[1] - x[0]),  # dx/dt = sigma * (y - x)
    r * x[0] - x[1] - x[0] * x[2],  # dy/dt = r * x - y - x * z
    x[0] * x[1] - b * x[2]  # dz/dt = x * y - b * z
]
# Create a time array from 0 to 20 with 2000 points
t = np.linspace(0, 20, 2000)
# Initial conditions for the Lorenz system
y0 = [5.0, 5.0, 5.0]  # Starting values for x, y, z
# Solve the Lorenz system using odeint
solution = od(f, y0, t)  # Integrate the system of equations
# Extract the solution components
X = solution[:, 0]  # x values
Y = solution[:, 1]  # y values
Z = solution[:, 2]  # z values
# Create a new figure for 3D plotting
fig = plt.figure()
# Add a 3D subplot to the figure
ax = fig.add_subplot(projection='3d')
# Plot the Lorenz attractor in 3D space
plt.plot(X, Y, Z)
# Display the plot
plt.show()  # Show the generated plot of the Lorenz attractor
