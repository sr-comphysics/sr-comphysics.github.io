# Visualizing Occupancy Distributions Across Energy Levels
# Importing the necessary libraries
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining a function to visualize occupancy
def sketch_occupancy(n):
    # Makes a cartoon of occupancy plot.
    # Boxes: levels or states (e.g., number of bills)
    # Dots: occupation numbers (e.g., number of people)

    # Define the size of boxes
    marg = 0.1  # Size of margin for the boxes
    h = 1.0 - 2 * marg  # Height of the boxes
    w = 1.0 - 2 * marg  # Width of the boxes
    
    # Define the coordinates for the boxes
    xbox = np.array([marg, marg + w, marg + w, marg])  # x-coordinates of the box corners
    ybox = np.array([marg, marg, marg + h, marg + h])  # y-coordinates of the box corners
    
    N = len(n)  # Number of levels (states)
    
    # Loop through each level to draw boxes and dots
    for i in range(N):
        plt.fill(xbox, ybox + i, color='#CCCCCC')  # Draw the box for the current level
        
        # Generate random x-coordinates for dots representing occupation numbers
        x = (np.random.uniform(size=n[i]) - 0.5) * w * 0.9 + 0.5
        
        # Generate random y-coordinates for dots, offset by the level index
        y = (np.random.uniform(size=n[i]) - 0.5) * h * 0.9 + 0.5 + i
        
        # Scatter plot the dots for the current level
        plt.scatter(x, y, marker='.', color='k', s=50, zorder=2.5)
    
    # Set the limits and ticks for the y-axis
    plt.ylim(-0.5, N + 0.5)  # Set y-axis limits
    plt.yticks(ticks=np.arange(N) + 0.5, labels=np.arange(N) + 1)  # Set y-ticks to represent levels
    plt.xticks([])  # Remove x-ticks
    
    # Set the aspect ratio and title for the plot
    plt.axis('equal')  # Ensure equal scaling on both axes
    plt.title("Occupancy:\n%s" % n)  # Set the title to show the occupancy numbers
    plt.box(on=False)  # Remove the box outline around the plot

# Try out different configurations (microstates).
n = [2, 0, 0, 0, 0, 1]  # First configuration of occupancy
fig = plt.figure(figsize=(2, 8))  # Create a new figure with specified size
sketch_occupancy(n)  # Call the function to visualize the occupancy
plt.show()  # Display the plot

# Second configuration of occupancy
n = [1, 1, 0, 0, 1, 0]  # Define the second occupancy configuration
fig = plt.figure(figsize=(2, 8))  # Create a new figure
sketch_occupancy(n)  # Visualize the second occupancy
plt.show()  # Display the plot

# Third configuration of occupancy
n = [0, 1, 2, 0, 0, 0]  # Define the third occupancy configuration
fig = plt.figure(figsize=(2, 8))  # Create a new figure
sketch_occupancy(n)  # Visualize the third occupancy
plt.show()  # Display the plot
