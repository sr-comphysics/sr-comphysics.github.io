# Entropy of argon gas as a function of temperature

# Importing the necessary libraries
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining constants
m = 6.6 * 10**-26  # Mass of an argon atom in kilograms
h = 6.63 * 10**-34  # Planck's constant in Joule-seconds
p = np.pi  # Value of pi
N = 6 * 10**23  # Number of argon particles (Avogadro's number)
V = 10 * -3  # Volume of the container in cubic meters (note: this should be positive)
dT = 0.0001  # Temperature step in Kelvin
T = np.arange(dT, 300, dT)  # Creating an array of temperature values from dT to 300 K
k = 1.38 * 10**-23  # Boltzmann constant in Joules per Kelvin

# Calculating the internal energy U of the gas
U = (3/2) * N * k * T  # Internal energy in Joules

# Calculating the entropy S in units of Joules per Kelvin
S = (3/2) * np.log(4 * p * m * (V**(2/3) * U) / (3 * (N**(5/3)) * (h**2))) + (5/2)  # Entropy formula
S = k * N * S  # Converting entropy to the appropriate units

# Plotting the entropy as a function of temperature
plt.plot(T, S, color='k')  # Creating a line plot of entropy S vs. temperature T
plt.xlabel('T (K)')  # Labeling the x-axis
plt.ylabel('S (J/K)')  # Labeling the y-axis
plt.show()  # Displaying the plot
