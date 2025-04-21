# Symbolic Derivation of Thermodynamic Properties for Ideal Gases
# Importing the necessary library for symbolic mathematics
import sympy as sp  # Importing SymPy for symbolic calculations

# Calculate pressure from symbolic differentiation.

# Define symbolic variables
k, T, N, V, h, m, pi = sp.symbols('k_{B} T N V h m \pi')  # Defining symbols for Boltzmann constant, temperature, number of particles, volume, Planck's constant, mass, and pi

# Internal energy of an ideal gas
U = (3/2) * N * k * T  # Formula for the internal energy of an ideal gas

# Entropy of an ideal gas
S = (3/2) * sp.ln((4 * pi * m * (V**(2/3)) * U) / (3 * (N**(5/3)) * (h**2))) + (5/2)  # Entropy formula
S = k * N * S  # Converting entropy to the appropriate units

# Helmholtz Free Energy
F = U - T * S  # Formula for Helmholtz free energy

# Displaying the entropy for an ideal gas
print('S for ideal gas')  # Printing the description
display(S.nsimplify())  # Displaying the simplified entropy expression
print('')  # Printing a blank line for spacing

# Calculating pressure from the Helmholtz free energy
print('P from -(dF/dV) for ideal gas')  # Printing the description
P = -sp.diff(F, V)  # Calculating pressure as the negative derivative of Helmholtz free energy with respect to volume
display(sp.nsimplify(P))  # Displaying the simplified pressure expression
print('')  # Printing a blank line for spacing

# Redefining P as a new symbolic variable (overriding the previous definition)
P = sp.symbols('P')  # Creating a new symbolic variable for pressure

# Gibbs Free Energy
G = U - T * S + P * V  # Formula for Gibbs free energy

# Calculate chemical potential from symbolic differentiation
print('mu from (dG/dN) for ideal gas')  # Printing the description
mu = sp.diff(G, N)  # Calculating the chemical potential as the derivative of Gibbs free energy with respect to the number of particles
mu = mu.collect(k).collect(T)  # Collecting terms involving k and T for clarity
display(sp.nsimplify(mu))  # Displaying the simplified chemical potential expression
