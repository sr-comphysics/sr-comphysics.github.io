# Damped Oscillation vs. Constant Amplitude Oscillation
import numpy as np  # Import the NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Generate an array of time values from 0 to 10 seconds, with 100 points
time = np.linspace(0, 10, 100)  
# Calculate the height of the damped oscillation using the exponential decay and sine function
height = np.exp(-time / 3.0) * np.sin(time * 3)  

# Create a new figure for plotting
plt.figure()  
# Plot the damped oscillation with magenta line and triangle markers
plt.plot(time, height, 'm-^')  
# Plot the constant amplitude oscillation with a green line
plt.plot(time, 0.3 * np.sin(time * 3), 'g-')  
# Add a legend to differentiate between the two plots
plt.legend(["damped", "constant amplitude"], loc='upper right')  
# Label the x-axis with "Time (s)"
plt.xlabel("Time (s)")  
# Display the plot
plt.show()
