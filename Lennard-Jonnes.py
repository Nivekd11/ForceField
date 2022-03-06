
import matplotlib.pyplot as plt 
import numpy as np 
import math
lenardJones = np.linspace(3.5, 8, 100)
epsi = -0.070000 
epsj = -0.070000
Rmini = 1.992400
Rminj = 2.000000

def v(lj):
    return Eps()*((Rmin()/lj)**12 - 2*(Rmin()/lj)**6)
    #return math.sqrt(epsi*epsj)*((Rmini+Rminj/lenardJones)**12 - 2*(Rmini+Rminj/lenardJones)**6)
def Eps():
    return math.sqrt(epsi*epsj)

def Rmin():
    return Rmini+Rminj

# plt.plot(x, y, marker=".")
plt.plot(lenardJones,v(lenardJones),marker=".",color="m")
plt.xlabel("Lennard-Jones")
plt.ylabel("V(Lennard-Jones)")
plt.title("Lennard-Jones CA CC",color="blue")
plt.show()