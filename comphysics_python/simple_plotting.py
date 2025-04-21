# Importing modules
import numpy as np
import matplotlib.pyplot as plt

x= np.array([1,2,3,4,5]) # Declaring x as a variable and assign the value for x-axis
y=x+3 # Declaring y as a variable and assign f(x) = x+3 NOTE: You can change the value of f(x) as in your problems.
plt.plot(x,y) # Calling matplotlib, assign the value of x and y as a parameters in the plot function
plt.plot(x,y, 'bo') # To make a scatter plot, b represent blue (user can replace with whatever colour you want) and o represent dot in scatter plot (user can replace with x as well)