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

h = ax.hist2d(x,y,bins=(120,80),range=([-2.5,2.5],[0,0.1]),cmap='Blues')
plt.colorbar(h[3], ax=ax)
plt.title('Distribution of leptons in CMS')
plt.xlabel('eta regions')
plt.ylabel('relative pT')

ax.annotate("R1b", xy=(-0.9, 0.02), xytext=(-0.8, 0.032),arrowprops=dict(arrowstyle="->"))

ax.annotate("R3a", xy=(1.1, 0.032), xytext=(0, 0.032),arrowprops=dict(arrowstyle="->"))
ax.annotate("R3b", xy=(1.3, 0.038), xytext=(0, 0.038),arrowprops=dict(arrowstyle="->"))
ax.annotate("R3c", xy=(1.5, 0.044), xytext=(0, 0.044),arrowprops=dict(arrowstyle="->"))
ax.annotate("R3d", xy=(1.75, 0.05), xytext=(0, 0.05),arrowprops=dict(arrowstyle="->"))
ax.annotate("R3e", xy=(2.25, 0.056), xytext=(0, 0.056),arrowprops=dict(arrowstyle="->"))

ax.text(x=-0.5,y=0.02,s='R1a')

ax.text(x=-1.75,y=0.09,s='R4')
ax.text(x=1.75,y=0.09,s='R4')
ax.text(x=-0.2,y=0.09,s='R2')

ax.axvline(x=0,ymin=0,ymax=0.3,color='m',lw=0.8)
ax.axvline(x=0.8,ymin=0,ymax=0.3,color='m',lw=0.8)
ax.axvline(x=-0.8,ymin=0,ymax=0.3,color='m',lw=0.8)
ax.axvline(x=1,ymin=0,ymax=1,color='r',lw=1.4)
ax.axvline(x=-1,ymin=0,ymax=1,color='r',lw=1.4)
ax.axvline(x=1.2,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=1.4,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=1.6,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=2,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=-1.2,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=-1.4,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=-1.6,ymin=0,ymax=0.7,color='m',lw=0.8)
ax.axvline(x=-2,ymin=0,ymax=0.7,color='m',lw=0.8)

ax.axhline(y=0.03,xmin=0.3,xmax=0.7,color='r',lw=1.4)
ax.axhline(y=0.07,xmin=0,xmax=0.3,color='r',lw=1.4)
ax.axhline(y=0.07,xmin=0.7,xmax=1,color='r',lw=1.4)

plt.savefig('../../public_html/MC_2DHisto_nocuts_updated.png')