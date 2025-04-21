# Comparison of Different Distributions Using Bar Plots
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Example of different distributions
dist1 = np.array([70, 25, 5])  # Distribution 1
dist2 = np.array([100, 100, 100]) / 3  # Distribution 2 (equal distribution)
dist3 = np.array([10, 80, 10])  # Distribution 3
dists = (dist1, dist2, dist3)  # Tuple of distributions
titles = ('(a)', '(b)', '(c)')  # Titles for each subplot
xaxis = ('Low', 'Med', 'High')  # Labels for x-axis

# Create a figure with 3 subplots for vertical bar plots
fig, axes = plt.subplots(1, 3, sharey=True, figsize=(8, 3))

# Draw vertical bar plots for each distribution
axes[0].bar(xaxis, dist1, color='black')  # Bar plot for distribution 1
axes[1].bar(xaxis, dist2, color='black')  # Bar plot for distribution 2
axes[2].bar(xaxis, dist3, color='black')  # Bar plot for distribution 3

# Set common properties for the subplots
axes[0].set_ylabel('Percent')  # Y-axis label
for i in range(3):
    axes[i].set_title(titles[i])  # Set title for each subplot
    axes[i].set_ylim((0, 100))  # Set y-axis limits
    axes[i].set_yticks((0, 50, 100))  # Set y-axis ticks
    axes[i].set_xlim((-1, 3))  # Set x-axis limits

plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('fig_ch5_distrib_vertical.eps')  # Save the vertical bar plot
plt.show()  # Display the vertical bar plot

# Create a new figure with 3 subplots for horizontal bar plots
fig, axes = plt.subplots(1, 3, sharey=True, figsize=(8, 3))

# Draw horizontal bar plots for each distribution
for i in range(3):
    axes[i].barh(xaxis, dists[i], color='black')  # Horizontal bar plot for each distribution
    axes[i].set_title(titles[i])  # Set title for each subplot
    axes[i].set_xlim((0, 100))  # Set x-axis limits
    axes[i].set_xticks((0, 50, 100))  # Set x-axis ticks
    axes[i].set_ylim((-1, 3))  # Set y-axis limits
    axes[i].set_xlabel('Percent')  # X-axis label

axes[0].set_ylabel('Levels')  # Y-axis label for the first subplot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('fig_ch5_distrib_horizontal.eps')  # Save the horizontal bar plot
plt.show()  # Display the horizontal bar plot
