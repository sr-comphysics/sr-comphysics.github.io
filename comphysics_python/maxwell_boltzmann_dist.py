# Maxwell-Boltzmann Distribution

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

""" Define probability distribution function, MB_distribution and a parameters is 
v, T, dv (where, v = velocity, T= Temperature, dv = infinitesimal velocity)"""
def MB_distribution (v,T=1,dv=0.01):
# Probability distribution equation, p 
    p = v**2*np.exp(-v**2/T)
    p = p/(np.sum(p)*dv) # normalize.
    return p
dv = 0.01 # Infinitesimal velocity within the system
v = np.arange(0,5,dv) # Set the range between 0 and 5 using numpy
# Plotting the Probability distribution function
plt.plot(v,MB_distribution(v,T=1,dv=dv),color='k',linestyle='solid')
plt.plot(v,MB_distribution(v,T=2,dv=dv),color='k',linestyle='dotted')
plt.plot(v,MB_distribution(v,T=4,dv=dv),color='k',linestyle='dashed')
legend_txt = ('Cold ','Warm ','Hot ')
plt.legend(legend_txt,framealpha=0)
plt.xlabel('Velocity (a.u.)')
plt.ylabel('Probability')
plt.yticks((0,0.5,1))
plt.title('Maxwell-Boltzmann Distribution')
plt.show()