# Contour Plot with Gradient Vectors and Streamlines
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Create an array of coordinates from -2 to 2 with 101 points
coords = np.linspace(-2, 2, 101)  
# Create a meshgrid for X and Y using every 5th coordinate
X, Y = np.meshgrid(coords[::5], coords[::5])  
# Calculate the radial distance from the origin
R = np.sqrt(X**2 + Y**2)  
# Calculate the Z values based on the Gaussian function
Z = np.exp(-R**2)  

# Create a finer meshgrid for x and y
x, y = np.meshgrid(coords, coords)  
# Calculate the radial distance for the finer grid
r = np.sqrt(x**2 + y**2)  
# Calculate the Z values for the finer grid
z = np.exp(-r**2)  

# Calculate the spacing between the coordinates
ds = coords[5] - coords[0]  
# Calculate the gradients of Z in the X and Y directions
dX, dY = np.gradient(Z, ds)  

# Create a filled contour plot of z
plt.contourf(x, y, z, 25)  
plt.set_cmap('coolwarm')  # Set the colormap for the contour plot

# Add quiver arrows to represent the gradient vectors
plt.quiver(X, Y, dX.transpose(), dY.transpose(), scale=25, color='k')  

# Create a stream plot for the vector field defined by Vx and Vy
# Note: Vx and Vy need to be defined for this to work
plt.streamplot(X, Y, dX, dY)  # Use dX and dY as the vector field for streamlines

# Display the plot
plt.colorbar()  # Add a colorbar to the contour plot
plt.title("Contour Plot with Gradient Vectors and Streamlines")  # Add a title
plt.xlabel("X-axis")  # Label for the x-axis
plt.ylabel("Y-axis")  # Label for the y-axis
plt.show()  # Show the plot
