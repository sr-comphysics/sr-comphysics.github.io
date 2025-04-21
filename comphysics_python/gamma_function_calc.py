# Calculation of the Gamma Function's Logarithmic Derivative Using SciPy
import scipy.special as ss  # Import the special functions module from SciPy

# Calculate the logarithmic derivative of the Gamma function (psi function) multiplied by 10^10
gamma = 10**10 * ss.psi(10**15)  
# Print the result
print(gamma)
