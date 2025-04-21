# Numerov-Cooley Method for Solving the SchrÃ¶dinger Equation in a Central Potential
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Discretize the r grid
dr = 0.001  # Step size for r
r = np.arange(1e-15, 60 + dr, dr)  # Create an array of r values from a small positive number to 60
N = r.shape[0]  # Number of points in the r array

# Define the effective potential V as a function of angular momentum l
Veff = lambda l: -1 / r + l * (l + 1) / (2 * r**2)

# Hydrogen energy eigenvalues
En = lambda n: -1 / (2 * n**2)

# Initial trial energy and potential
E = En(1)  # Initial energy for the ground state (n=1)
V = Veff(0)  # Effective potential for l=0
k = dr**2 / 12  # Numerov parameter

# Iterate the Numerov-Cooley method for 1000 maximum steps
for i in range(1000):
    P = -2 * (V - E)  # Calculate the potential term

    # Set the two initial conditions for the wavefunction at both boundaries
    psi = np.zeros_like(r)  # Initialize the wavefunction array
    psi[1] = 1e-6  # Small value at the first point
    psi[-1] = 1e-6  # Small value at the last point

    # Outward integration to point m-1
    for j in range(1, N - 1):
        psi[j + 1] = 2 * psi[j] * (1 - 5 * k * P[j]) - psi[j - 1] * (1 + k * P[j - 1])
        psi[j + 1] /= 1 + k * P[j + 1]  # Normalize the wavefunction

        # When the first turning point is found, set it as the match point
        if psi[j] < psi[j - 1]:
            m = j + 1  # Match point index
            psi_out_m = psi[m]  # Value of the wavefunction at the match point
            break

    # Inward integration to point m+1
    for j in range(N - 2, m, -1):
        psi[j - 1] = 2 * psi[j] * (1 - 5 * k * P[j]) - psi[j + 1] * (1 + k * P[j + 1])
        psi[j - 1] /= 1 + k * P[j - 1]  # Normalize the wavefunction

    # Scale outward and inward integration so psi(m)=1
    psi[:m] /= psi_out_m  # Normalize the outward wavefunction
    psi[m:] /= psi[m]  # Normalize the inward wavefunction

    # Cooley's energy correction formula
    Y = (1 + k * P) * psi  # Calculate the modified wavefunction
    dE = (psi[m].conj() / np.sum(np.abs(psi)**2)) * \
         (-0.5 * (Y[m + 1] - 2 * Y[m] + Y[m - 1]) / (dr**2) + (V[m] - E) * psi[m])
    E += dE  # Update the energy

    # If dE is smaller than a set precision, exit the loop early
    if np.abs(dE) < 1e-6:
        break

# The final wavefunction and energy in Hartrees
S = E * 27.21  # Convert energy to Hartrees
print(S, psi)  # Print the energy and wavefunction

# Plot the wavefunction against energy
plt.plot(r, psi)  # Plot the wavefunction as a function of r
plt.title("Wavefunction of the Hydrogen Atom")  # Title for the plot
plt.xlabel("Radius (r)")  # Label for the x-axis
plt.ylabel("Wavefunction (Ï)")  # Label for the y-axis
plt.grid()  # Add a grid to the plot
plt.show()  # Display the plot
