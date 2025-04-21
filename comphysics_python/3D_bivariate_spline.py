# 3D Surface Plot of a Bivariate Spline Interpolation
import numpy as np  # Import the NumPy library for numerical operations
import scipy.interpolate as si  # Import the SciPy interpolation module
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit from Matplotlib

# Define the range for x and y
x = y = np.arange(10)  
# Define a function to interpolate: f(i, j) = sin(i) * cos(j)
f = (lambda i, j: np.sin(i) * np.cos(j))  
# Generate a 10x10 array of samples using the function
A = np.fromfunction(f, (10, 10))  

# Create a bivariate spline interpolation of the generated samples
spline = si.RectBivariateSpline(x, y, A)  

# Create a new figure for plotting
fig = plt.figure()  
# Add a 3D subplot to the figure
subplot = fig.add_subplot(111, projection='3d')  

# Create a larger grid for plotting the surface
xx = np.mgrid[0:9:100j, 0:9:100j]  
# Evaluate the spline on the larger grid
A = spline(np.linspace(0, 9, 100), np.linspace(0, 9, 100))  

# Plot the surface using the evaluated spline
subplot.plot_surface(xx[0], xx[1], A)  
# Display the plot
plt.show()  
