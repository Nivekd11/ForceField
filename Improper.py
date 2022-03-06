
import matplotlib.pyplot as plt 
import numpy as np 
psi = np.linspace(3.5, 50, 200)
Kpsi = 1
psi0 = 0



def v(psi):
    return Kpsi*(psi-psi0)**2

# plt.plot(x, y, marker=".")
plt.plot(psi,v(psi),marker=".",color="m")
plt.xlabel("improper")
plt.ylabel("V(improper)")
plt.title("Improper HR3 CPH1 NR3 CPH1",color="blue")
plt.show()