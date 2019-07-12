from root_numpy import root2array
from matplotlib import colors
from ROOT import TFile
import matplotlib.pyplot as plt

#code to get the number of events in the NTuple
f = TFile.Open("/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root")
t = f.Get("passedEvents")
n = t.GetEntries()

#definition of the file
path = "/raid/raid8/ferrico/HZZ4l/CMSSW_10_2_5/src/leptonPtErrorCorrector/makeSlimTree/output/DY_2018/DYJetsToLL_M-50_kalman_v4_m2e_v2.root"

#leaf values being pulled from the NTuple
eta1 = root2array(path,"passedEvents","eta1")
eta2 = root2array(path,"passedEvents","eta2")
pterr1 = root2array(path,"passedEvents","pterr1")
pterr2 = root2array(path,"passedEvents","pterr2")
pt1 = root2array(path,"passedEvents","pT1")
pt2 = root2array(path,"passedEvents","pT2")

#define the lists
x = []
y = []
#define the variables actually being plotted
for i in range(n):
    x1 = x.append(eta1[i])
    x2 = x.append(eta2[i])
    y1 = y.append(pterr1[i]/(pt1[i]))
    y2 = y.append(pterr2[i]/(pt2[i]))

#histogram of leptons in the geometry of CMS
fig, ax = plt.subplots()

h = ax.hist2d(x,y,bins=(120,80),range=([-2,2],[0,0.1]),cmap='Blues',normed=True)
plt.colorbar(h[3], ax=ax)
plt.title('Distribution of leptons in CMS')
plt.xlabel('eta regions')
plt.ylabel('relative pT')
fig.savefig('../../public_html/MC_2DHisto_nocuts.png')