# Recursive Permutation Generation for Energy Distribution
# Importing the necessary libraries
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting
import numpy as np  # Importing NumPy for numerical operations

# Defining a recursive function to calculate permutations
def perm_recursive(e, N, E):
    # Asserting that E and N are non-negative and that all elements in e are non-negative
    assert E >= 0
    assert N >= 0
    assert all(e >= 0)
    
    # Converting N and E to integers
    N = int(N)
    E = int(E)
    
    # Getting the dimension of the input array e
    dim = len(e)
    
    # Base case: if N is 0
    if (N == 0):
        # If E is also 0, return a zero array of shape (1, dim)
        if E == 0:
            return np.zeros((1, dim))
        else:
            return np.zeros((0, dim))  # Return an empty array if E is not 0
    
    # Initialize an empty array to store results
    n = np.zeros((0, dim))
    
    # Loop through each element in e
    for i in range(dim):
        # Check if the current element can be subtracted from E
        if (E - e[i]) >= 0:
            # Recursively call the function to find permutations for the remaining values
            n_next = perm_recursive(e, N - 1, E - e[i])
            if len(n_next) > 0:  # If there are valid permutations
                n_next[:, i] = n_next[:, i] + 1  # Increment the count for the current element
                n = np.vstack((n, n_next))  # Stack the new results
    
    return n  # Return the accumulated results

# Setting parameters for the recursive function
N = 10  # Total number of items
E = 5   # Total energy or sum to achieve
e = np.arange(0, E + 1, 1)  # Creating an array of possible energy levels from 0 to E

# Calling the recursive function to get all permutations
n = perm_recursive(e, N, E)

# Finding unique permutations and their counts
n, counts = np.unique(n, axis=0, return_counts=True)

# Asserting that the sum of each row equals N and the dot product equals E
assert all(np.sum(n, axis=1) == N)
assert all(np.dot(n, e) == E)

# Printing the results
print('All possibilities:')
print(np.array(n).astype(int))  # Displaying the unique permutations as integers

# Plotting the average occupancy as a bar graph
print('Bar graph of average occupancy')
plt.bar(np.arange(0, E + 1), np.mean(n, axis=0), color='k')  # Creating a bar graph of average occupancy
plt.ylabel('Average Occupancy')  # Labeling the y-axis
plt.xlabel('E')  # Labeling the x-axis
plt.show()  # Displaying the plot
