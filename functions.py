#file to define all functions for deltamZ calculations
#------------------------------------------------------------------------------------------

import math as m

#definition to the entire calculation for the invariant mass
def InvariantMass(pt1,pt2,phi1,phi2,eta1,eta2):
    mass = m.sqrt(2*pt1*pt2*(-m.cos(phi2-phi1)+m.cosh(eta2-eta1)))
    return mass
def Quad(a,b):
    return m.sqrt(a**2+b**2)





'''
#TO TEST THE FUNCIONS:
pT1 = (1,2,3,4)
pT2 = (1,2,3,4)
phi1= (4,2,3,3)
phi2= (8,6,3,4)
eta1= (9,2,3,4)
eta2= (3,2,7,4)

i = 0


print(InvariantMass(pT1[i],pT2[i],phi1[i],phi2[i],eta1[i],eta2[i]))
'''
