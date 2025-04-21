# Simulation of Electromagnetic Wave Propagation in Free Space Using FDTD Method
# Importing libraries
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Define parameters for the simulation
ke = 200  # Number of spatial cells
ex = np.zeros(ke)  # Initialize the Ex electric field array
hy = np.zeros(ke)  # Initialize the Hy magnetic field array

# Pulse parameters
kc = int(ke / 2)  # Center index for the pulse
t0 = 40  # Time at which the pulse is centered
spread = 12  # Spread of the Gaussian pulse
nsteps = 100  # Number of time steps for the simulation

# Main FDTD Loop
for time_step in range(1, nsteps + 1):
    # Calculate the Ex field
    for k in range(1, ke):
        ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])  # Update Ex field based on Hy field

    # Put a Gaussian pulse in the middle
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread) ** 2)  # Create a Gaussian pulse
    ex[kc] = pulse  # Place the pulse in the center of the Ex field

    # Calculate the Hy field
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])  # Update Hy field based on Ex field

    # Plot the outputs as shown in Fig. 1.2
    plt.rcParams['font.size'] = 12  # Set font size for plots
    plt.figure(figsize=(8, 3.5))  # Create a figure with specified size

    # Plot the Ex field
    plt.subplot(211)  # Create a subplot for Ex field
    plt.plot(ex, color='k', linewidth=1)  # Plot Ex field
    plt.ylabel('E$_x$', fontsize='14')  # Label y-axis
    plt.xticks(np.arange(0, 201, step=20))  # Set x-ticks
    plt.xlim(0, 200)  # Set x-axis limits
    plt.yticks(np.arange(-1, 1.2, step=1))  # Set y-ticks
    plt.ylim(-1.2, 1.2)  # Set y-axis limits
    plt.text(100, 0.5, 'T = {}'.format(time_step), horizontalalignment='center')  # Display time step

    # Plot the Hy field
    plt.subplot(212)  # Create a subplot for Hy field
    plt.plot(hy, color='k', linewidth=1)  # Plot Hy field
    plt.ylabel('H$_y$', fontsize='14')  # Label y-axis
    plt.xlabel('FDTD cells')  # Label x-axis
    plt.xticks(np.arange(0, 201, step=20))  # Set x-ticks
    plt.xlim(0, 200)  # Set x-axis limits
    plt.yticks(np.arange(-1, 1.2, step=1))  # Set y-ticks
    plt.ylim(-1.2, 1.2)  # Set y-axis limits

    plt.subplots_adjust(bottom=0.2, hspace=0.45)  # Adjust subplot spacing
    plt.show()  # Display the plots
