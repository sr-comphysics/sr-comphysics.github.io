# Finite-Difference Time-Domain (FDTD) Simulation of Electromagnetic Wave Propagation
import numpy as np  # Import NumPy for numerical operations
from matplotlib import pyplot as plt  # Import Matplotlib for plotting

# Define the number of spatial points
ke = 200  
# Initialize electric field (Ex) and magnetic field (Hy) arrays
ex = np.zeros(ke)  
hy = np.zeros(ke)  

# Pulse parameters
kc = int(ke / 2)  # Center index for the pulse
t0 = 40  # Time at which the pulse is centered
spread = 12  # Spread of the Gaussian pulse
boundary_low = [0, 0]  # Low boundary conditions
boundary_high = [0, 0]  # High boundary conditions
nsteps = 250  # Number of time steps for the simulation

# Dictionary to keep track of desired points for plotting
plotting_points = [
    {'num_steps': 100, 'data_to_plot': None, 'label': ''},
    {'num_steps': 225, 'data_to_plot': None, 'label': ''},
    {'num_steps': 250, 'data_to_plot': None, 'label': 'FDTD cells'}
]

# Main FDTD Loop
for time_step in range(1, nsteps + 1):
    # Calculate the Ex field
    for k in range(1, ke):
        ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])  # Update Ex field based on Hy field
        
    # Put a Gaussian pulse in the middle
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread) ** 2)  # Gaussian pulse equation
    ex[kc] = pulse  # Set the pulse at the center

    # Absorbing Boundary Conditions
    ex[0] = boundary_low.pop(0)  # Update low boundary condition
    boundary_low.append(ex[1])  # Store the new low boundary condition
    ex[ke - 1] = boundary_high.pop(0)  # Update high boundary condition
    boundary_high.append(ex[ke - 2])  # Store the new high boundary condition

    # Calculate the Hy field
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])  # Update Hy field based on Ex field

    # Save data at certain points for later plotting
    for plotting_point in plotting_points:
        if time_step == plotting_point['num_steps']:
            plotting_point['data_to_plot'] = np.copy(ex)  # Store the Ex field for plotting

# Plot the outputs
plt.rcParams['font.size'] = 12  # Set font size for plots
fig = plt.figure(figsize=(8, 5.25))  # Create a figure for plotting

def plot_e_field(data, timestep, label):
    """Plot of E field at a single time step"""
    plt.plot(data, color='k', linewidth=1)  # Plot the electric field
    plt.ylabel('E$_x$', fontsize='14')  # Label for the y-axis
    plt.xticks(np.arange(0, 199, step=20))  # Set x-ticks
    plt.xlim(0, 199)  # Set x-axis limits
    plt.yticks(np.arange(0, 1.2, step=1))  # Set y-ticks
    plt.ylim(-0.2, 1.2)  # Set y-axis limits
    plt.text(100, 0.5, 'T = {}'.format(timestep), horizontalalignment='center')  # Add time step text
    plt.xlabel('{}'.format(label))  # Label for the x-axis

# Plot the E field at each of the time steps saved earlier
for subplot_num, plotting_point in enumerate(plotting_points):
    ax = fig.add_subplot(3, 1, subplot_num + 1)  # Create subplots
    plot_e_field(plotting_point['data_to_plot'], plotting_point['num_steps'], plotting_point['label'])  # Plot the data

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plots
