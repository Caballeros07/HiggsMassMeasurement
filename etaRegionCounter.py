#standard imports
from ROOT import * 

#---------------
###MAIN
#--------------

#file opening resources
f = TFile.Open("/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root")
mytree = f.Get("passedEvents")

#The definition of the ECAL eta regions 
LargeRegion0 = 0
subRegion1 = 0.8
LargeRegion1 = 1 
subRegion2 = 1.2
subRegion3 = 1.44
subRegion4 = 1.57
subRegion5 = 2
LargeRegion2 = 2.5

#definition of relative pT regions
barrelrelpT = 0.03
endcapsrelpT = 0.07

#Barrel Regions inside relative pT
bcut1 = mytree.GetEntries("abs(eta1) > 0 && abs(eta1) < 0.8 && abs(eta2) > 0 && abs(eta2) < 0.8 && pterr1/pT1 < 0.03 && pterr2/pT2 < 0.03 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")
bcut2 = mytree.GetEntries("abs(eta1) > 0.8 && abs(eta1) < 1 && abs(eta2) > 0.8 && abs(eta2) < 1 && pterr1/pT1 < 0.03 && pterr2/pT2 < 0.03 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")

#Barrel Regions outside relative pT
bcut3 = mytree.GetEntries("abs(eta1) > 0 && abs(eta1) < 1 && abs(eta2) > 0 && abs(eta2) < 1 && pterr1/pT1 > 0.03 && pterr2/pT2 > 0.03 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")

#Endcap Regions inside relative pT
ecut1 = mytree.GetEntries("abs(eta1) > 1 && abs(eta1) < 1.2 && abs(eta2) > 1 && abs(eta2) < 1.2 && pterr1/pT1 < 0.07 && pterr2/pT2 < 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")
ecut2 = mytree.GetEntries("abs(eta1) > 1.2 && abs(eta1) < 1.44 && abs(eta2) > 1.2 && abs(eta2) < 1.44 && pterr1/pT1 < 0.07 && pterr2/pT2 < 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven . 0.5")
ecut3 = mytree.GetEntries("abs(eta1) > 1.44 && abs(eta1) < 1.57 && abs(eta2) > 1.44 && abs(eta2) < 1.57 && pterr1/pT1 < 0.07 && pterr2/pT2 < 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")
ecut4 = mytree.GetEntries("abs(eta1) > 1.57 && abs(eta1) < 2 && abs(eta2) > 1.57 && abs(eta2) < 2 && pterr1/pT1 < 0.07 && pterr2/pT2 < 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")
ecut5 = mytree.GetEntries("abs(eta1) > 2 && abs(eta1) < 2.5 && abs(eta2) > 2 && abs(eta2) < 2.5 && pterr1/pT1 < 0.07 && pterr2/pT2 < 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")

#Endcap Regions outside relative pT
ecut6 = mytree.GetEntries("abs(eta1) > 1 && abs(eta1) < 2.5 && abs(eta2) > 1 && abs(eta2) < 2.5 && pterr1/pT1 > 0.07 && pterr2/pT2 > 0.07 && lep1_ecalDriven > 0.5 && lep2_ecalDriven > 0.5")
 
#Stuff to output by region:
print("ECAL electrons")
print("eta region 1")
print "[" + str(LargeRegion0) + "," + str(subRegion1) + "]:" + str(bcut1) + " given relative pT <" + str(barrelrelpT)  

print("eta region 2")
print "[" + str(subRegion1) + "," + str(LargeRegion1) + "]:" + str(bcut2) + " given relative pT <" + str(barrelrelpT)  

print("eta region 3")
print "[" + str(LargeRegion0) + "," + str(LargeRegion1) + "]:" + str(bcut3) + " given relative pT >" + str(barrelrelpT)  

print("eta region 4")
print "[" + str(LargeRegion1) + "," + str(subRegion2) +  "]:" +  str(ecut1) +  " given relative pT <" + str(endcapsrelpT) 

print("eta region 5")
print "[" + str(subRegion2) + "," + str(subRegion3) + "]:" + str(ecut2) + " given relative pT <" +  str(endcapsrelpT)  

print("eta region 6")
print "[" + str(subRegion3) + "," + str(subRegion4) + "]:" + str(ecut3) + " given relative pT <" + str(endcapsrelpT) 

print("eta region 7")
print "[" + str(subRegion4) + "," + str(subRegion5) + "]:" + str(ecut4) + " given relative pT <" + str(endcapsrelpT) 

print("eta region 8")
print "[" + str( subRegion5) + "," + str(LargeRegion2) + "]:" + str(ecut5) + " given relative pT <" +  str(barrelrelpT)

print("eta region 9")
print "[" + str(LargeRegion1) + "," + str(LargeRegion2) + "]:" + str(ecut6) + " given relative pT >" + str(barrelrelpT) 

#definitions for the reginos in the Tracker Electrons
teregion0 = 0
teregion1 = 1.44
teregion2 = 1.6
teregion3 = 2
teregion4 = 2.5

#cuts for the Tracker Electrons
tcut1 = mytree.GetEntries("abs(eta1) > 0 && abs(eta1) < 1.44 && abs(eta2) > 0 && abs(eta2) < 1.44 && lep1_ecalDriven < 0.5 && lep2_ecalDriven < 0.5")
tcut2 = mytree.GetEntries("abs(eta1) > 1.44 && abs(eta1) < 1.6 && abs(eta2) > 1.44 && abs(eta2) < 1.6 && lep1_ecalDriven < 0.5 && lep2_ecalDriven < 0.5")
tcut3 = mytree.GetEntries("abs(eta1) > 1.6 && abs(eta1) < 2 && abs(eta2) > 1.6 && abs(eta2) < 2 && lep1_ecalDriven < 0.5 && lep2_ecalDriven < 0.5")
tcut4 = mytree.GetEntries("abs(eta1) > 2 && abs(eta1) < 2.5 && abs(eta2) > 2 && abs(eta2) < 2.5 && lep1_ecalDriven < 0.5 && lep2_ecalDriven < 0.5")

#statements to print the Tracker Electrons
print("Tracker electrons")
print("eta region 1")
print "[" + str(teregion0) + "," + str(teregion1) + "]:" + str(tcut1) 

print("eta region 2")
print "[" + str(teregion1) + "," + str(teregion2) + "]:" + str(tcut2) 

print("eta region 3")
print "[" + str(teregion2) + "," + str(teregion3) + "]:" + str(tcut3) 

print("eta region 4")
print "[" + str(teregion3) + "," + str(teregion4) + "]:" + str(tcut4) 



''' FOR LATER
#definition of the file
path = "/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root"

#leave values being pulled from the NTuple
eta1 = root2array(path,"passedEvents","eta1")
eta2 = root2array(path,"passedEvents","eta2")
eta1 = root2array(path,"passedEvents","eta1")
eta1 = root2array(path,"passedEvents","eta1")
'''

