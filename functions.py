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




