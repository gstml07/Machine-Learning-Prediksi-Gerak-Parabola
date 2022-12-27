import numpy as np
import matplotlib.pyplot as plt


def PosisiParabolaKetikaT(t):
    h0 = 23
    alpha = np.radians(135)
    g = 9.8
    v0 = 3

    v0x = v0*np.cos(alpha)
    v0y = v0*np.sin(alpha)

    X = ((v0**2)*np.sin(2*alpha))/(2*g)
    Y = ((v0**2)*(np.sin(alpha)**2))/(2*g)
    T = (2*v0*np.sin(alpha))/g     

    y = h0 + v0y*t - 0.5*g*t**2
    x = v0x*t

    print(t,',',round(x,2),',',round(y,2))
print( 't , x , y')
for i in range(0,25):
    t = 0.1*i
    PosisiParabolaKetikaT(round(t,2))
