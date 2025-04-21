# Head-On Collision Simulation and Visualization of Elastic Collisions
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

def headon_collision(u1, u2, m1, m2):
    # u1 and u2: pre-collision velocities of the two masses
    # v1 and v2: post-collision velocities of the two masses
    v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)  # Calculate post-collision velocity of mass 1
    v2 = (2 * m1 * u1 + (m2 - m1) * u2) / (m1 + m2)  # Calculate post-collision velocity of mass 2
    return v1, v2  # Return the post-collision velocities

def plot_pre_post_collision(velocity1, velocity2, m1, m2):
    x1, x2 = (-1, 1)  # Locations of m1 and m2 on the plot
    y = 1  # Arbitrary y-coordinate for the particles
    marker_size = 100  # Size of the markers for the particles
    scale = 0.5  # Scale for the length of the velocity arrows
    title_str = ('Before', 'After')  # Titles for the subplots
    c1 = 'black'  # Color for mass 1
    c2 = 'gray'  # Color for mass 2
    fig, ax = plt.subplots(1, 2, figsize=(8, 1))  # Create a figure with two subplots

    for i in range(2):  # Loop over the two subplots
        ax[i].scatter(x1, y, s=marker_size, color=c1)  # Plot mass 1
        ax[i].scatter(x2, y, s=marker_size, color=c2)  # Plot mass 2
        # Draw an arrow for mass 1 if its velocity is significant
        if abs(velocity1[i]) > 0.01:
            ax[i].arrow(x1, y, velocity1[i] * scale, 0, color=c1, head_width=0.1)
        # Draw an arrow for mass 2 if its velocity is significant
        if abs(velocity2[i]) > 0.01:
            ax[i].arrow(x2, y, velocity2[i] * scale, 0, color=c2, head_width=0.1)
        ax[i].set_xlim((-2, 2))  # Set x-axis limits
        ax[i].set_ylim((0.8, 1.2))  # Set y-axis limits
        ax[i].set_title(title_str[i])  # Set the title for the subplot
        ax[i].axis('off')  # Turn off the axis

    plt.tight_layout()  # Adjust layout to prevent overlap

# Case 1: m2 is much more massive than m1 and is at rest
print('Case 1: m2 is much more massive than m1 and is at rest.')
m1, m2 = (1, 2000)  # Masses of m1 and m2
u1, u2 = (1, 0)  # Initial velocities of m1 and m2
v1, v2 = headon_collision(u1, u2, m1, m2)  # Calculate post-collision velocities
plot_pre_post_collision((u1, v1), (u2, v2), m1, m2)  # Plot the pre- and post-collision states

# Case 2: m1 = m2, and m2 is initially at rest
print('Case 2: m1 = m2, and m2 is initially at rest.')
m1, m2 = (1, 1)  # Masses of m1 and m2
u1, u2 = (1, 0)  # Initial velocities of m1 and m2
v1, v2 = headon_collision(u1, u2, m1, m2)  # Calculate post-collision velocities
plot_pre_post_collision((u1, v1), (u2, v2), m1, m2)  # Plot the pre- and post-collision states
assert v1 == 0  # Assert that the post-collision velocity of m1 is 0
assert v2 == u1  # Assert that the post-collision velocity of m2 is equal to the initial velocity of m1

# Case 3: m1 = m2, and they move toward each other
print('Case 3: m1 = m2, and they move toward each other.')
