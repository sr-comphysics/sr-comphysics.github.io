# Visualization of 2D Vectors: A, B, and C
# Importing the necessary libraries
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining vector A
A = np.array([1, 2])  # Creating a NumPy array for vector A with components (1, 2)

# Plotting vector A as an arrow
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1)  # Drawing the vector A from the origin (0,0)
plt.text(A[0] + 0.1, A[1] + 0.1, r"$\vec{A}$")  # Adding a label for vector A

# Defining vector B
B = np.array([1, -2])  # Creating a NumPy array for vector B with components (1, -2)

# Plotting vector B as an arrow
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1)  # Drawing the vector B from the origin (0,0)
plt.text(B[0] + 0.1, B[1] + 0.1, r"$\vec{B}$")  # Adding a label for vector B

# Defining vector C
C = np.array([-2, -1])  # Creating a NumPy array for vector C with components (-2, -1)

# Plotting vector C as an arrow
plt.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1)  # Drawing the vector C from the origin (0,0)
plt.text(C[0] + 0.1, C[1] - 0.5, r"$\vec{C}$")  # Adding a label for vector C

# Setting up the grid and axis properties
plt.grid()  # Enabling the grid on the plot
plt.axis('square')  # Setting the aspect ratio of the plot to be equal
plt.xlabel('x')  # Labeling the x-axis
plt.ylabel('y')  # Labeling the y-axis

# Setting the limits for the axes
lim = 3  # Defining the limit for the axes
plt.xlim((-lim, lim))  # Setting the x-axis limits
plt.ylim((-lim, lim))  # Setting the y-axis limits

# Setting the ticks for the axes
plt.xticks(np.arange(-lim, lim + 0.1))  # Setting x-axis ticks
plt.yticks(np.arange(-lim, lim + 0.1))  # Setting y-axis ticks

# Displaying the plot
plt.show()  # Rendering the plot to the screen
