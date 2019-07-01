#Standard imports
from root_numpy import root2array
from ROOT import TFile
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


#code to get the number of events in the NTuple
f = TFile.Open("/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root")
t = f.Get("passedEvents")
n = t.GetEntries()
print(n)

#global lists being defined to be filled on a per event basis
mZHist = []
deltamZHist = []
deltamZ = []
closure = []
n = 1000

#loop to set the do the calculations on a per event level. i is set as the number of events
for i in range(n):
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
    mass_2l = Quad(deltamZ1,deltamZ2)+massZ[i]
    deltamass_2l = Quad(deltamZ1,deltamZ2)
    deltamZ.append(deltamass_2l)    
    deltamZHist.append(mass_2l)


#constants being used
x = range(1,n+1) 
l = np.linspace(0,130,130)
lshiftup = 1.1*l
lshiftdown = 0.9*l
horiz_line_data = np.array([1 for i in xrange(len(x))])

#scatterplot doing the closure test
fig, ax = plt.subplots()
ax.set_xlim(0,120)
ax.set_ylim(0,120)
ax.scatter(mZHist,massZ[0:n],color='blue',s=7,alpha=.8)
ax.plot(l,l,'--',color='black')
ax.plot(l,lshiftup,'--',color='black')
ax.plot(l,lshiftdown,'--',color='black')
#lableling
ax.set_title('Closure Test')
ax.set_ylabel("NTuple Mass(GeV)")
ax.set_xlabel('Calculated Mass(GeV)')
fig.savefig('../../public_html/MC_MassZ_closure_test.png')



#histograms for the variation of the pT
fig1, bx = plt.subplots()
bx.hist(massZ[0:n], bins=100, edgecolor='red',range=[0,200], fill=False, histtype="step")
bx.hist(deltamZHist, bins=100, edgecolor='blue', range=[0,200], fill=False, histtype="step")
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


#histograms of the mass of the Z boson, both calculated and branch
fig2, cx = plt.subplots()
cx.set_xlim(0,200)
cx.hist(massZ[0:n], bins=100, edgecolor='red', fill=False, histtype="step") 
cx.hist(mZHist, bins=100, edgecolor='blue', fill=False, histtype="step") 
cx.set_title("Invariant mass of the 2 leptons with delta pT smearing")
cx.set_ylabel("Counts")
cx.set_xlabel("mass_2l (GeV)")
plt.show()
fig2.savefig('../../public_html/MC_massZ_combined_histo.png')

#scatterplot doing the variance
fig3, ax2 = plt.subplots()
ax2.set_xlim(0,n)
ax2.plot(x,horiz_line_data,color='red')
ax2.scatter(x,deltamZ,color='blue',s=0.5,alpha=.8)
#lableling
ax2.set_title('Mass Variance')
ax2.set_ylabel("Mass(Gev)")
ax2.set_xlabel('Event Number')
fig3.savefig('../../public_html/MC_MassZ_variance.png')














  
