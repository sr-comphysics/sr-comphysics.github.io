# Estimation of Pi Using Polygon Approximation of a Unit Circle
import numpy as np  # Import the NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Define the value of pi
pi = 3.141592  
# Define the angular increment for theta (lesser the delta_theta value, more the precise in the estimation of pi)
delta_theta = 0.004
# Create an array of theta values from 0 to 2*pi with the specified increment
theta = np.arange(0, 2*pi + delta_theta, delta_theta)  
# Calculate the x-coordinates of the unit circle
x = np.cos(theta)  
# Calculate the y-coordinates of the unit circle
y = np.sin(theta)  
# Get the number of data points
N = len(theta)  
# Print the number of data points
print("Number of data points = %d" % N)  

# Loop through the data points to plot the polygon
for i in range(N - 1):
    # Plot line segments between successive points
    plt.plot((x[i], x[i + 1]), (y[i], y[i + 1]), color='black')  

# Connect the last point to the first point to close the polygon
plt.plot((x[-1], x[0]), (y[-1], y[0]), color='black')  

# Draw a box around the polygon
plt.plot((-1, 1), (1, 1), color='gray')  # Top edge
plt.plot((1, 1), (1, -1), color='gray')  # Right edge
plt.plot((1, -1), (-1, -1), color='gray')  # Bottom edge
plt.plot((-1, -1), (-1, 1), color='gray')  # Left edge

# Set the limits for the x and y axes
plt.xlim((-2, 2))  
plt.ylim((-2, 2))  
# Set equal scaling for both axes
plt.axis('equal')  
# Turn off the axis
plt.axis('off')  
# Save the figure as an EPS file
plt.savefig('fig_ch1_draw_circle.eps')  
# Display the plot
plt.show()  

# Calculate the perimeter of the polygon by summing the distances between successive points
d = 0  # Start with zero
for i in range(N - 1):
    # Add the distance between the next two points
    d = d + np.sqrt((x[i] - x[i + 1])**2 + (y[i] - y[i + 1])**2)  

# Add the distance between the first and last point to close the polygon
d = d + np.sqrt((x[-1] - x[0])**2 + (y[-1] - y[0])**2)  

# Estimate pi using the perimeter of the polygon (d = 2*pi*r with r=1 for a unit circle)
pi_estimate = d / 2  
# Print the estimated value of pi
print('Our estimate of pi (with a polygon of %d sides)' % N)  
print(pi_estimate)  
