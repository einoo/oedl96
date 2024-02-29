from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from string import ascii_lowercase as alc

plt.rcParams["font.size"] = 8
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Arial"

J = 40
M = 40
L = 360  # transient period

dataD = np.load("../Data/Lorenz96_letkf_maxPb_Dopt.npy")
dataA = np.load("../Data/Lorenz96_letkf_maxPb_Topt.npy")
dataE = np.load("../Data/Lorenz96_letkf_maxPb_Eopt.npy")
SEL = ["maxHPbH", "minPa", "minF"]
OED = ["D-criterion", "A-criterion", "E-criterion"]
oed = ["Dopt", "Topt", "Eopt"]

rmse = np.zeros((M + 1, J, len(OED), len(SEL)))

for i in range(M + 1):
    rmse[i, :, 0, 0] = np.sqrt(np.mean(dataD[:, L:, i], axis=1))
    rmse[i, :, 1, 0] = np.sqrt(np.mean(dataA[:, L:, i], axis=1))
    rmse[i, :, 2, 0] = np.sqrt(np.mean(dataE[:, L:, i], axis=1))
    for j in range(len(OED)):
        filename = "../Data/Lorenz96_letkf_minPa_%s.npy" % oed[j]
        data = np.load(filename)
        rmseind = np.sqrt(np.mean(data[:, L:, i], axis=1))
        rmse[i, :, j, 1] = rmseind.astype(int)

rmse[:, :, 0, 2] = rmse[:, :, 0, 1]  # Dopt is the same for minPa and minF
rmse[:, :, 1, 2] = np.load('../Data/rmse_letkf_maxDeltaF_Topt.npy')
rmse[:, :, 2, 2] = np.load('../Data/rmse_letkf_maxDeltaF_Eopt.npy')

# plot the figure
fig = plt.figure(constrained_layout=True, figsize=(6, 6), dpi=150)

x = np.linspace(1, 40, num=J)
y = np.linspace(0, 10, num=M + 1)
X, Y = np.meshgrid(x, y)

k = 1
for i, j in product(range(3), range(3)):
    ax = fig.add_subplot(3, 3, k)
    c = ax.pcolormesh(
        X,
        Y,
        np.round(rmse[:, :, j, i]),
        edgecolors="none",
        lw=0.0,
        cmap="RdBu",
        rasterized=True,
        vmin=0,
        vmax=6,
    )

    ax.set_ylim(10.125, -0.125)
    ax.set_xticks([1, 10, 20, 30, 40], ["1", "10", "20", "30", "40"])
    ax.set_xlabel("Site")
    ax.set_ylabel("Forecast range (days)")
    ax.set_title("(%s) %s (%s)" % (alc[k-1], SEL[i], OED[j]))
    k += 1
    if j == 2:
        fig.colorbar(c, ax=ax)

plt.savefig("../Figure/Lorenz96_comparison.png")
plt.show()
