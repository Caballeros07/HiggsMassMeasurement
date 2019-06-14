#Standard imports
from root_numpy import root2array
import matplotlib.pyplot as plt
import numpy as np

#macros that I pull from my functions.py
from functions import DotProduct, Mag, Inv


#definition of the file
path = "/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root"

#defintion of the bin size, to cut the histo
binedgeMass = [60,65,70,75,80,85,90,95,100,105,110,115,120]


#---------------------------------------------------------------------------------
#branches being pulled and that will be operated on
#Need massZ, massZErr, pT1, pterr1 pT2, pterr2, eta1, and eta2 from passedEvents TTree
#----------------------------------------------------------------------------------
massZ = root2array(path,"passedEvents","massZ")
massZErr = root2array(path,"passedEvents","massZErr")
pT1 = root2array(path,"passedEvents","pT1")
pterr1 = root2array(path,"passedEvents","pterr1")  
pT2 = root2array(path,"passedEvents","pT2")  
pterr2 = root2array(path,"passedEvents","pterr2")  
eta1 = root2array(path,"passedEvents","eta1")  
eta2 = root2array(path,"passedEvents","eta2")  
phi1 = root2array(path,"passedEvents","phi1")  
phi2 = root2array(path,"passedEvents","phi2")  

mZHist = []
y=[]
y2=[]
closure = []
#testing invariant masses for first 10 entries
for i in range(1000):
	p1 = Mag(pT1[i],phi1[i],eta1[i])
	p2 = Mag(pT2[i],phi2[i],eta2[i])
	
	p1p2 = DotProduct(pT1[i],pT2[i],phi1[i],phi2[i],eta1[i],eta2[i])
	
	mZ = Inv(p1*p2, p1p2)
	mZHist.append(mZ)
	#closure test for massZ vs. mZ
	close = mZ/massZ[i]
	closure.append(close)

	#calculation for deltamZ changing only the pT of the first lepton, pT1
	p1prime = Mag(pT1[i]+pterr1[i],phi1[i],eta1[i])

	p1p2prime = DotProduct(pT1[i]+pterr1[i],pT2[i],phi1[i],phi2[i],eta1[i],eta2[i])
	
	mZprime = Inv(p1prime*p2, p1p2prime)		
	
	deltamZ = mZprime - mZ
	
	y.append(deltamZ)

	#calculation for deltamZ changing only the pT of the second lepton, pT2
	p2prime = Mag(pT2[i]+pterr2[i],phi2[i],eta2[i])
	
	p1p2prime2 = DotProduct(pT1[i],pT2[i]+pterr2[i],phi1[i],phi2[i],eta1[i],eta2[i])

	mZprime2 = Inv(p2prime*p1, p1p2prime2)		
	
	deltamZ2 = mZprime2 - mZ
	
	y2.append(deltamZ)


#histograms of the mass of the Z boson, both calculated and branch
fig2, cx = plt.subplots()
cx.hist(massZ[0:1000], bins=30, color='red', fill=False) 
cx.hist(mZHist, bins=30, color='green', fill=False) 
cx.set_title("Invariant mass of the 2 leptons with delta pT smearing")
cx.set_ylabel("Counts")
cx.set_xlabel("mass 2l (GeV)")
fig2.savefig('../../public_html/MC_massZ_histo.png')




#histogram of the delta mZ values when only changing the pT of the first lepton, pT1
fig1, bx = plt.subplots()
bx.hist(y, binedgeMass, color='red', fill=False)
bx.hist(y2, binedgeMass, color='blue', fill=False)
bx.set_title("Invariant mass of the 2 leptons with delta pT smearing")
bx.set_ylabel("Counts")
bx.set_xlabel("mass 2l (GeV)")
fig1.savefig('../../public_html/MC_deltamZ_varying_pT_histo.png')


#scatterplot doing the closure test
x = range(1,1001) 

fig, ax = plt.subplots()
ax.set_title('Branch mass compared to calulated Mass')
ax.set_ylabel("massZ_NTuple / massZ_calculated")
ax.set_xlabel('Event Number')
ax.scatter(x,closure)
fig.savefig('../../public_html/MC_MassZ_closure_test.png')













'''
#plots of the delta mZ values when only changing the pT of the first lepton, pT1 
x = range(1,100000001) 

fig, ax = plt.subplots()
ax.scatter(x,y)
fig.savefig('../../public_html/MC_deltamZ_varying_pT1.png')
'''




  
