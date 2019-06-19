#Standard imports
from root_numpy import root2array
import matplotlib.pyplot as plt
import numpy as np

#macros that I pull from my functions.py
from functions import * 

#definition of the file
path = "/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root"

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

#global lists being defined to be filled on a per event basis
mZHist = []
deltamZHist = []
closure = []

#loop to set the do the calculations on a per event level. i is set as the number of events
for i in range(10):
	mZ = InvariantMass(pT1[i],pT2[i],phi1[i],phi2[i],eta1[i],eta2[i])
	mZHist.append(mZ)
	#closure test for massZ vs. mZ
	close = mZ/massZ[i]
	closure.append(close)
	#calculation for deltamZ changing only the pT of the first lepton, pT1
	mZprime1 = InvariantMass(pT1[i]+pterr1[i],pT2[i],phi1[i],phi2[i],eta1[i],eta2[i])	
	deltamZ1 = mZprime1 - mZ
	#calculation for deltamZ changing only the pT of the second lepton, pT2
	mZprime2 = InvariantMass(pT1[i],pT2[i]+pterr2[i],phi1[i],phi2[i],eta1[i],eta2[i])	
	deltamZ2 = mZprime2 - mZ
	#calculation for the total mZ for the entire event
	mass_2l = Quad(deltamZ,deltamZ2)
	deltamZHist.append(mass_2l)	


#histograms of the mass of the Z boson, both calculated and branch
fig2, cx = plt.subplots()
cx.hist(massZ[0:10], bins=10, color='red', fill=False) 
#cx.hist(mZHist, bins=30, color='green', fill=False) 
cx.set_title("Invariant mass of the 2 leptons with delta pT smearing")
cx.set_ylabel("Counts")
cx.set_xlabel("mass_2l (GeV)")
fig2.savefig('../../public_html/MC_massZ_histo.png')



'''
#histogram of the delta mZ values against the original values 
fig1, bx = plt.subplots()
bx.hist(massZ[0:1000], bins=30, color='red', fill=False)
bx.hist(deltamZHist, bins=30, color='blue', fill=False)
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












'''
#plots of the delta mZ values when only changing the pT of the first lepton, pT1 
x = range(1,100000001) 

fig, ax = plt.subplots()
ax.scatter(x,y)
fig.savefig('../../public_html/MC_deltamZ_varying_pT1.png')
'''




  
