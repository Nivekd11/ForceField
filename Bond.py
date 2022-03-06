
import matplotlib.pyplot as plt 
import numpy as np 



b = np.linspace(0, 10, 100)
listaB = []
Kb = 334.300
b0 = 1.4110


def v(bond):
    return Kb*(bond-b0)**2

# plt.plot(x, y, marker=".")
plt.plot(b,v(b),marker=".",color="orange")
plt.xlabel("bond")
plt.ylabel("V(bond)")
plt.title("Bond OH1 CA",color="g")
plt.show()