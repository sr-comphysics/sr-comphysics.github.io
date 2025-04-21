# 3D Visualization of Vectors and Their Cross Product
# Importing Libraries
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining vectors A and B
A = np.array([2, 1, 0])  # Creating a NumPy array for vector A
B = np.array([0, 0, 1])  # Creating a NumPy array for vector B

# Calculating the cross product of vectors A and B
C = np.cross(A, B)  # Computing the cross product, resulting in vector C

# Creating a meshgrid for the x and z coordinates
x, z = np.meshgrid(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))  # Generating a grid of points in the x-z plane
y = x / 2  # Defining the y-coordinates based on the x-coordinates to form a plane

# Setting up the figure for 3D plotting
fig = plt.figure(figsize=(5, 5))  # Creating a new figure with a specified size
ax = plt.axes(projection='3d')  # Adding a 3D axis to the figure

# Plotting the surface defined by the meshgrid
ax.plot_surface(x, y, z, color='#CCCCCC', alpha=0.2)  # Drawing the surface with a light gray color and transparency

# Plotting the vectors A, B, and C as arrows
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='k', arrow_length_ratio=0.1, normalize=True)  # Plotting vector A
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='k', arrow_length_ratio=0.1, normalize=True)  # Plotting vector B
ax.quiver(0, 0, 0, C[0], C[1], C[2], color='k', arrow_length_ratio=0.1, normalize=True)  # Plotting vector C (cross product)

# Adding text labels for the vectors
ax.text(1, 0.5, 0, r"$\vec{A}$")  # Label for vector A
ax.text(0, 0, 1.1, r"$\vec{B}$")  # Label for vector B
ax.text(0.5, -1, 0, r"$\vec{A}\times\vec{B}$")  # Label for vector C (cross product)

# Setting the ticks and limits for the axes
ax.set_xticks((-1, 0, 1))  # Setting x-axis ticks
ax.set_yticks((-1, 0, 1))  # Setting y-axis ticks
ax.set_zticks((-1, 0, 1))  # Setting z-axis ticks
ax.set_xlim(-1, 1)  # Setting x-axis limits
ax.set_ylim(-1, 1)  # Setting y-axis limits
ax.set_zlim(-1, 1)  # Setting z-axis limits

# Labeling the axes
ax.set_xlabel('x')  # Label for the x-axis
ax.set_ylabel('y')  # Label for the y-axis
ax.set_zlabel('z')  # Label for the z-axis

# Setting the viewing angle for the 3D plot
ax.view_init(20, -120)  # Adjusting the elevation and azimuthal angle for better visualization
