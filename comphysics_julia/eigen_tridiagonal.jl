################################################################################
# Title:      Eigen Analysis & Visualization of a Tridiagonal Matrix
#
# Description:
#   This program constructs a symmetric tridiagonal matrix H of size 10x10,
#   computes its eigenvalues and eigenvectors using functions from the
#   LinearAlgebra package, and visualizes the first three eigenvectors using
#   the PyPlot package.
#
# Instructions:
#   1. Ensure that both the LinearAlgebra and PyPlot packages are installed.
#      You can install PyPlot via the Julia package manager if needed:
#         using Pkg
#         Pkg.add("PyPlot")
#
#   2. Save this file as, for instance, eigen_tridiagonal.jl.
#
#   3. Run the program from the command line with:
#         julia eigen_tridiagonal.jl
################################################################################

# Import the necessary packages.
using LinearAlgebra  # Provides linear algebra routines including eigenvalue computations.
using PyPlot         # Enables plotting capabilities.

# Construct the symmetric tridiagonal matrix H:
# H is defined as:
#   2 on the main diagonal (10 elements),
#   -1 on the subdiagonals above and below the main diagonal (9 elements each).
A = 2 * diagm(0 => ones(10)) - diagm(1 => ones(9)) - diagm(-1 => ones(9))

# Compute the eigen decomposition of matrix H.
# F contains both the eigenvalues and eigenvectors.
F = eigen(A)
evals = F.values   # Extract the eigenvalues.
evecs = F.vectors  # Extract the corresponding eigenvectors.

# Plot the first three eigenvectors.
figure()                      # Create a new figure window.
subplot(3, 1, 1)              # Define a subplot structure of 3 rows x 1 column; select the first subplot.
plot(evecs[:, 1])             # Plot the first eigenvector (all rows, first column) in the first subplot.
title("Eigenvector 1")        # Set the title of subplot 1.

subplot(3, 1, 2)              # Select the second subplot.
plot(evecs[:, 2])             # Plot the second eigenvector.
title("Eigenvector 2")        # Set the title of subplot 2.

subplot(3, 1, 3)              # Select the third subplot.
plot(evecs[:, 3])             # Plot the third eigenvector.
title("Eigenvector 3")        # Set the title of subplot 3.

tight_layout()                # Adjust subplot parameters for a neat layout.
show()                        # Display the figure window containing the plots.

# Print the first three eigenvalues to the console.
println("E1 = ", evals[1])
println("E2 = ", evals[2])
println("E3 = ", evals[3])
