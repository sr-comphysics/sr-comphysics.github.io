# Draw a PV diagram of Carnot cycle and calculating Carnot's efficiency

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Going through four different thermal states of a, b, c, and d.
Nk = 1 # for simplicity, let Nk = 1 so that PV = T
gamma = 5/3
dV = 0.1
# Starting points defined below.
Pa = 20 # pressure at the initial state a.
Va = 10
 # volume at a.
Vb = 20
 # volume at b.
Vc = 40
 # volume at c.
Vd = 20
 # volume at d.
V_ab = np.arange(Va,Vb,dV)
V_bc = np.arange(Vb,Vc,dV)
V_cd = np.arange(Vc,Vd,-dV)
V_da = np.arange(Vd,Va,-dV)
# Along isotherm (a->b and c->d): P = T/V
# Along adiabat (b->c and d->a): P*V**gamma = constant = k
#(Note that P*V**gamma = T*V**(gamma-1) since P = T/V)
T_high = Va*Pa # high T
Pa = T_high/Va
P_ab = T_high/V_ab # isothermal process
Pb = T_high/Vb
kb = T_high*Vb**(gamma-1) # constant along adiabat
P_bc = kb/V_bc**(gamma) # adiabatic process
Pc = kb/Vc**(gamma)
T_low = Vc*Pc # low T
P_cd = T_low/V_cd # isothermal process
Pd = T_low/Vd
kd = T_low*Vd**(gamma-1) # constant along adiabat
P_da = kd/V_da**(gamma) # adiabatic process
plt.plot(V_ab,P_ab,color='gray',linestyle='solid')
plt.plot(V_bc,P_bc,color='black',linestyle='dotted')
plt.plot(V_cd,P_cd,color='gray',linestyle='solid')
plt.plot(V_da,P_da,color='black',linestyle='dotted')
plt.legend(('a->b: isothermal','b->c: adiabatic',
            'c->d: isothermal','d->a: adiabatic'),framealpha=1)
spacing = 1
plt.text(Va+spacing,Pa,'a')
plt.text(Vb+spacing,Pb,'b')
plt.text(Vc+spacing,Pc,'c')
plt.text(Vd+spacing,Pd,'d')
plt.text((Va+Vb)/2+spacing,Pa-6,'high T')
plt.text((Vc+Vd)/2-spacing,Pd-4,'low T')
plt.xlim((0,50))
plt.ylim((0,30))
plt.xlabel('V (m$^3$)')
plt.ylabel('P (pascal)')
plt.show()
# Calculate the efficiency of a Carnot cycle.
# total amount of work from numerical integration.
W_ab = np.sum(P_ab)*dV
W_bc = np.sum(P_bc)*dV
W_cd = -np.sum(P_cd)*dV
W_da = -np.sum(P_da)*dV
W_total = W_ab+W_bc+W_cd+W_da
# Q_in is equal to the total mechanical work during a->b, because
# b->c and d->a: adiabatic process, so no added heat.
# c->d: isothermal compression, so heat goes out, not in.
# a->b: isothermal expansion, so internal energy does not change.
# The added heat must match the mechanical work by the gas.
Q_in = W_ab
eta_measure = W_total/Q_in
eta_theory = 1 - T_low/T_high
print("Efficiency of an example Carnot Cycle:")
print(" %4.3f (calculated by numerical integration)"%eta_measure)
print(" %4.3f (according to the theory)"%eta_theory)
print("Percent Difference = %3.2f perc with dV = %4.3f"
      %((1-eta_measure/eta_theory)*100,dV))
print("Smaller dV would make percent difference smaller.")
