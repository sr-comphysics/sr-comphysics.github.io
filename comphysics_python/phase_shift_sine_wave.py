# Visualizing a Phase-Shifted Sine Wave with NumPy and Matplotlib

# Import NumPy library for numerical operations and arrays.
import numpy as np
# Import pyplot from matplotlib for plotting data.
import matplotlib.pyplot as plt
# Set the wavelength to 555 nm.
wl = 555
# Set the initial phase to 90° (π/2 radians).
phi = np.pi / 2
# Set the wave amplitude to 1.
ampl = 1
# Calculate the wave
# Create an array 'x' of 256 equally spaced points between 0 and 1.
x = np.linspace(0, 1, 256)
y = ampl * np.sin(2 * np.pi * x / (wl / 1000) + phi)
# Compute the sine wave 'y':
# - Multiply x by (2π) to set the scale of one full cycle.
# - Divide by (wl / 1000) to adjust for wavelength (assuming conversion factor, e.g., nm to µm).
# - Add the phase shift 'phi' (90° in radians).
# - Multiply by amplitude 'ampl' to scale the wave.

# Create the matplotlib figure
# Create a figure and a single subplot (axes) for plotting; 
fig, ax = plt.subplots(1, 1)
# "fig" is the figure object and "ax" is the Axes object.
# Plot the sine wave using x as the x-axis and y as the y-axis data.
ax.plot(x, y)
# Display the plot window with the current figure.
plt.show()
