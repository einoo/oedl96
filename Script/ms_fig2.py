import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.size"] = 8
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Arial"

J = 40
M = 40
L = 360  # transient period

dataD = np.load("../Data/Lorenz96_maxPb_Dopt.npy")
dataA = np.load("../Data/Lorenz96_maxPb_Topt.npy")
dataE = np.load("../Data/Lorenz96_maxPb_Eopt.npy")
OED = [
    "(a) maxHPbH (D-criterion)",
    "(b) maxHPbH (A-criterion)",
    "(c) maxHPbH (E-criterion)",
]

rmse = np.zeros((M + 1, J, 3), dtype=int)

for i in range(M + 1):
    rmse[i, :, 0] = np.sqrt(np.mean(dataD[:, L:, i], axis=1))
    rmse[i, :, 1] = np.sqrt(np.mean(dataA[:, L:, i], axis=1))
    rmse[i, :, 2] = np.sqrt(np.mean(dataE[:, L:, i], axis=1))

# plot the figure
fig = plt.figure(constrained_layout=True, figsize=(6, 2), dpi=200)

x = np.linspace(1, 40, num=J)
y = np.linspace(0, 10, num=M + 1)
X, Y = np.meshgrid(x, y)

k = 1
for i in range(3):
    ax = fig.add_subplot(1, 3, k)
    c = ax.pcolormesh(
        X,
        Y,
        np.round(rmse[:, :, i]),
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
    ax.set_title("%s" % OED[i])
    k += 1

fig.colorbar(c, ax=ax)

plt.savefig("../Figure/Lorenz96_maxPb.png")
plt.show()
