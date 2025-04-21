# Signal generation

# Importing libraries
import numpy as np
from scipy.signal import chirp, sawtooth, square, gausspulse
import matplotlib.pyplot as plt

t=np.linspace(-1,1,1000) # Create an array of evenly spaced number within -1 to 1
# Display a 4 plots (2 rows and 2 columns) in a single picture using subplot function
# Chirp signal in first row and first column
plt.subplot(221); plt.ylim([-2,2])
plt.plot(t,chirp(t,f0=100,t1=0.5,f1=200))
plt.title("Chirp signal")
# Gauss pulse in first row and second column
plt.subplot(222); plt.ylim([-2,2])
plt.plot(t,gausspulse(t,fc=10,bw=0.5))
plt.title("Gauss pulse")
# Sawtooth signal in second row and first column
plt.subplot(223); plt.ylim([-2,2])
t*=3*np.pi
plt.plot(t,sawtooth(t))
plt.xlabel("Sawtooth signal")
# Square wave signal in second row and second column
plt.subplot(224); plt.ylim([-2,2])
plt.plot(t,square(t))
plt.xlabel("Square wave signal")
plt.show()
