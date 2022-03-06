
import matplotlib.pyplot as plt 
import numpy as np 
chi = np.linspace(3.5, 100, 100)
Kchi = 6.5
n = 2
delta = 180



def v(chi):
    return Kchi*(1 + np.cos(n*(chi)-delta))

# plt.plot(x, y, marker=".")
plt.plot(chi,v(chi),marker=".",color="gray")
plt.xlabel("dihedral")
plt.ylabel("V(dihedral)")
plt.title("Dihedral CPT CPT NY CA",color="blue")
plt.show()