# Symbolic Derivation of Entropy and Pressure Relationships in Ideal Gases
# Importing the necessary library for symbolic mathematics
import sympy as sp  # Importing SymPy for symbolic calculations

# Defining the symbols used in the equations
k, T, N, V, h, m, pi = sp.symbols('k_{B} T N V h m \pi')  # Defining symbols for Boltzmann constant, temperature, number of particles, volume, Planck's constant, mass, and pi

# Calculating the internal energy U of the gas
U = (3/2) * N * k * T  # Internal energy formula for an ideal gas

# Calculating the entropy S using the given formula
S = (3/2) * sp.ln(4 * pi * m * (V**(2/3)) * U) / (3 * (N**(5/3)) * (h**2)) + (5/2)  # Entropy formula
S = k * N * S  # Converting entropy to the appropriate units

# Calculating the pressure P of the gas
P = N * k * T / V  # Pressure formula for an ideal gas

# Displaying the derivative of entropy with respect to volume for fixed temperature and number of particles
print('dS/dV for fixed T and N')  # Printing the description
dS_over_dV = sp.diff(S, V)  # Calculating the derivative of S with respect to V
display(sp.nsimplify(dS_over_dV))  # Displaying the simplified result

# Displaying the derivative of pressure with respect to temperature for fixed volume and number of particles
print('dP/dT for fixed V and N')  # Printing the description
dP_over_dT = sp.diff(P, T)  # Calculating the derivative of P with respect to T
display(sp.nsimplify(dP_over_dT))  # Displaying the simplified result

# Printing a note about the equality of the two expressions
print('Note that these two expressions are equal')  # Indicating that the two derivatives are equal
