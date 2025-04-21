# Draw P-V curves for thermal processes (Isobaric, Isothermal, Adiabatic).

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

Va = 5 # Set the initial volume limit
P= 20 # Pressure
NkT = Va*P # Ideal Gas law equation
Vb = 20 # Set the final volume limit
dV = 0.1 # Infinitesimal volume within the system
V = np.arange(Va,Vb,dV) # Set the range with the given limits using numpy
P_isobaric = np.zeros(len(V))+P # Isobaric process (P = 0, Constant Pressure)
P_isothermal = NkT/V # Isothermal process (P = NkT/V)
P_adiabatic = P*(Va/V)**(5/3) # Adiabatic process
# Plotting for thermal processes
plt.plot(V,P_isobaric,color='black',linestyle='solid')
plt.plot(V,P_isothermal,color='black',linestyle='dotted')
plt.plot(V,P_adiabatic,color='black',linestyle='dashed')
plt.legend(('isobaric','isothermal','adiabatic'),framealpha=0)
plt.xlim((0,25))
plt.ylim((0,25))
plt.xlabel('V (m$^3$)')
plt.ylabel('P (pascal)')
plt.show()