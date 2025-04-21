# Simulation of Radioactive Decay
# Import necessary libraries
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Initial conditions
y = 1  # Initial quantity of the substance (e.g., counts per minute)
n = 300  # Number of time steps
h = 0.01  # Time step size (in minutes)

# Initialize lists to store time and quantity values
tv = [0]  # Time values
yv = [y]  # Quantity values

# Loop to calculate radioactive decay using Euler's method
for i in range(1, n + 1):
    f = -y  # The rate of decay (negative because the quantity decreases)
    y = y + f * h  # Update the quantity using Euler's method
    tv.append(i * h)  # Append the current time to the time list
    yv.append(y)  # Append the current quantity to the quantity list
    print(y)  # Print the current quantity (optional)

# Calculate the theoretical decay for comparison
np.exp(-n * h)  # This line is not used but shows the theoretical decay factor
tt = np.linspace(0, n * h, n)  # Create an array of time values for theoretical decay
ty = 1 * np.exp(-tt)  # Calculate the theoretical decay values

# Plot the theoretical decay curve
plt.plot(tt, ty, 'red', label='Theoretical Decay')  # Plot theoretical decay in red
plt.xlabel('time (minutes)')  # Label the x-axis
plt.ylabel('Counts per minute')  # Label the y-axis

# Scatter plot of the calculated decay values
plt.scatter(tv, yv, label='Calculated Decay')  # Scatter plot of calculated values
plt.legend()  # Show legend
plt.show()  # Display the plot
