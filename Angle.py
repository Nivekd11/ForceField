
import matplotlib.pyplot as plt 
import numpy as np 
Theta = np.linspace(3.5, 100, 1000)
Ktheta = 67.700
Theta0 = 110.00



def v(angle):
    return Ktheta*(angle-Theta0)**2

# plt.plot(x, y, marker=".")
plt.plot(Theta,v(Theta),marker=".",color="m")
plt.xlabel("angle")
plt.ylabel("V(angle)")
plt.title("Angle NH2 CT1 CT1",color="blue")
plt.show()