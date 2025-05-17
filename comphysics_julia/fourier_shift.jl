################################################################################
# Title:      Fourier Transform Shift Visualization with FFTW and PyPlot
#
# Description:
#   This program demonstrates the Fourier transform process of a Gaussian
#   function using FFTW and visualizes its transformation using PyPlot.
#   It performs the following tasks:
#     1. Generates a Gaussian function defined on a specified range.
#     2. Computes its Fourier transform and applies a phase shift corresponding
#        to a spatial translation.
#     3. Reconstructs the shifted function via the inverse FFT.
#     4. Plots the original function, its shifted version, and the real and
#        imaginary parts of its Fourier transform.
#
# Instructions:
#   1. Ensure that the PyPlot and FFTW packages are installed.
#      To install, use:
#         using Pkg
#         Pkg.add("PyPlot")
#         Pkg.add("FFTW")
#
#   2. Save this file as, for example, fourier_shift.jl.
#
#   3. Run the program from the command line with:
#         julia fourier_shift.jl
################################################################################

using PyPlot   # Provides plotting capabilities.
using FFTW     # Provides FFT functions.

# Set up the spatial grid.
n = 50                              # Number of points in the spatial grid.
x = range(-5.0, stop = 15.0, length = n)  # Define the x-axis range from -5 to 15.
dx = x[2] - x[1]                    # Compute the spacing between consecutive x values.

# Set up the corresponding frequency (k) grid.
# The frequency range is determined by the spacing dx and covers -π/dx to π/dx.
k = range(-pi/dx, stop = pi/dx, length = n)

# Define the original function: a Gaussian function.
y = exp.(-x.^2)                     # Element-wise exponentiation to compute exp(-x^2).

# Compute the Fourier transform of the Gaussian function using FFT.
ft = fftshift(fft(y))               # Compute FFT, then shift zero frequency component to the center.

# Apply a spatial shift in the Fourier domain.
x0 = 10                            # Define the spatial shift value.
gk = ft .* exp.(-1im * x0 .* k)      # Multiply by a complex exponential to implement a phase shift.
                                    # Note: This uses the shift theorem of Fourier transforms.

# Compute the inverse FFT to obtain the shifted function.
g = ifft(ifftshift(gk))             # Unshift before applying the inverse FFT.

# Begin plotting the results.
clf()                             # Clear the current figure.

# Top subplot: Plot original and reconstructed (shifted) functions.
subplot2grid((2,2), (0,0), colspan = 2)  # Create a subplot spanning the top row.
plot(x, y, label=L"$y(x)$")         # Plot the original Gaussian function.
plot(x, real(g), label=L"$\Re\{g(x)\}$")  # Plot the real part of the shifted function.
xlabel(L"$x$")                    # Label x-axis.
ylabel(L"$f(x)$")                 # Label y-axis.
legend()                          # Display the legend for the plotted functions.

# Bottom-left subplot: Real part of the Fourier transform.
subplot2grid((2,2), (1,0))         # Position for the bottom-left subplot.
plot(k, real(ft))                 # Plot the real part of the Fourier transform.
xlabel(L"$k$")                    # Label the x-axis (frequency).
ylabel(L"$\Re\{\tilde{f}(k)\}$")  # Label the y-axis with the real component descriptor.

# Bottom-right subplot: Imaginary part of the Fourier transform.
subplot2grid((2,2), (1,1))         # Position for the bottom-right subplot.
plot(k, imag(ft))                 # Plot the imaginary part of the Fourier transform.
xlabel(L"$k$")                    # Label the x-axis (frequency).
ylabel(L"$\Im\{\tilde{f}(k)\}$")  # Label the y-axis with the imaginary component descriptor.

# Adjust the layout for better spacing between subplots.
tight_layout()

# Render the figure.
show()
