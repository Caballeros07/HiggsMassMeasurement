#file to define all functions for deltamZ calculations
#------------------------------------------------------------------------------------------

import math as m

#definition for the dot product between two vectors in 3-space:
def DotProduct(pT1,pT2,phi1,phi2,eta1,eta2):
    return pT1*pT2*(m.cos(phi1-phi2)+m.sinh(eta1)*m.sinh(eta2))
    
#definition for the magnitude of a vector:
def Mag(pT,phi,eta):
    return m.sqrt((pT*m.cos(phi))**2+(pT*m.sin(phi))**2+(pT*m.sinh(eta))**2)

#defintion for the invariant of two 4-vectors:
def Inv(a,b):
    return m.sqrt(2*(a-b))

#definition for adding in quadrature:
def Quad(a,b):
	return m.sqrt(a**2+b**2)



#definition to the entire calculation for the invariant mass
def InvariantMass(pt1,pt2,phi1,phi2,eta1,eta2):
	p1 = Mag(pt1,phi1,eta1)
	p2 = Mag(pt2,phi2,eta2)
	p1p2 = DotProduct(pt1,pt2,phi2,phi2,eta1,eta2)
	mass = Inv(p1*p2, p1p2)
	return mass






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
