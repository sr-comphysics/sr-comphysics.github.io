# Visualization of 1D and 2D Fast Fourier Transforms of Block Matrices

import numpy as np  # Import the NumPy library for numerical operations
from scipy.fftpack import fft, fft2, fftshift  # Import FFT functions from SciPy for 1D and 2D Fourier transforms
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Create a 4x4 matrix of ones
B = np.ones((4, 4))  
# Create a 4x4 matrix of zeros
W = np.zeros((4, 4))  

# Construct a block matrix with B in the top-left and bottom-right, and W in the other two quadrants
signal = np.bmat("B,W;W,B")  

# Compute the 1D Fast Fourier Transform of the signal with a length of 16
fft_1D = fft(signal, n=16)  

# Compute the 2D Fast Fourier Transform of the signal, reshaping it to 16x16
fft_2D = fft2(signal, shape=(16, 16))  

# Create a new figure for plotting
plt.figure()  
plt.gray()  # Set the colormap to grayscale

# Create a subplot for the 1D FFT result
plt.subplot(121, aspect='equal')  
# Create a pseudocolor plot of the real part of the 1D FFT result
plt.pcolormesh(fft_1D.real)  
# Add a colorbar to the 1D FFT plot with horizontal orientation
plt.colorbar(orientation='horizontal')  

# Create a subplot for the 2D FFT result
plt.subplot(122, aspect='equal')  
# Create a pseudocolor plot of the real part of the 2D FFT result, shifted for better visualization
plt.pcolormesh(fftshift(fft_2D.real))  
# Add a colorbar to the 2D FFT plot with horizontal orientation
plt.colorbar(orientation='horizontal')  

# Display the plots
plt.show()
