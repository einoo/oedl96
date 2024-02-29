from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams["font.size"] = 8
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Arial"

SEL = ["maxPb", "minPa"]
OED = ["Dopt", "Topt", "Eopt"]

data_maxpb = np.load("../Data/rmse_maxPb.npy")
data_minpa = np.load("../Data/rmse_minPa.npy")
data_minf = np.load("../Data/rmse_minF.npy")

# plot the figure
fig = plt.figure(constrained_layout=True, figsize=(6, 4), dpi=150)

k = 1
cls = ["C0", "C1", "C4"]
lstyle = [":", "--", "-"]
titles = ["(a)", "(b)", "(c)", "(d)"]
line1 = [Line2D([0], [0], marker="s", ms=4, mec=c,
                mfc=c, color=c, ls="") for c in cls]
line2 = [Line2D([0], [0], color="k", lw=1, ls=c) for c in lstyle]
lines = line2 + line1
label1 = ["D-criterion", "A-criterion", "E-criterion"]
label2 = ["maxHPbH", "minPa", "minF"]
labels = ["maxHPbH", "minPa", "minF",
          "D-criterion", "A-criterion", "E-criterion"]
for z in [0, 8, 24, 40]:
    ax = fig.add_subplot(2, 2, k)
    for i, j in product(SEL, OED):
        ax.plot(
            np.sort(data_maxpb[z, :, OED.index(j)])[::-1],
            ":",
            color=cls[OED.index(j)],
            marker="s",
            ms=2.0,
            lw=1.0,
        )
        ax.plot(
            data_minpa[z, :, OED.index(j)],
            "--",
            color=cls[OED.index(j)],
            marker="s",
            ms=2.0,
            lw=1.0,
        )
        ax.plot(
            np.sort(data_minf[z, :, OED.index(j)])[::-1],
            "-",
            color=cls[OED.index(j)],
            marker="s",
            ms=2.0,
            lw=1.0,
        )
    ytop = np.max(data_maxpb[z, :, OED.index(j)]) + 17
    ybot = np.min(data_minf[z, :, :]) - 2
    ax.set_ylim(ybot, ytop)
    ax.set_xticks([0, 1, 2, 3, 4], ["1", "2", "3", "4", "5"])
    ax.set_xlabel("Number of supplementary observations")
    ax.set_ylabel("Reduction of rmse (%)")
    day = int(z / 4.0)
    ax.set_title("%s Forecast range of %d day(s)" % (titles[k - 1], day))
    leg1 = ax.legend(line1, label1, loc=2, fontsize=6)
    leg2 = ax.legend(line2, label2, fontsize=6)
    ax.add_artist(leg1)
    k += 1

plt.savefig("../Figure/Lorenz96_letkf_multiobs.png")
plt.show()
