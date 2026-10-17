"""Microfab Lab 5 postlab: schematic cross-sections (not to scale)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch

C = {"Si": "#9e9e9e", "SiO2": "#8ecae6", "Al": "#e5e5e5", "Al_edge": "#555555", "PR": "#e76f51"}


def layer(ax, xs, bottom, top, color, edge="none", lw=0.8):
    pts = list(zip(xs, top)) + list(zip(xs[::-1], bottom[::-1]))
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=edge, lw=lw))


def device_profile(x):
    """Surface height of Si + patterned SiO2 (a raised oxide region with an opening)."""
    oxide = np.where((x > 2.0) & (x < 8.0), 0.0, 1.0)  # opening (window) in the middle
    return 2.0 + oxide  # Si top at 2.0, oxide 1.0 thick


x = np.linspace(0, 10, 2001)
si_top = np.full_like(x, 2.0)
ox_top = device_profile(x)

# Al follows the surface (line-of-sight evaporation: thinner on vertical sidewalls).
al_t = 0.25
al_top = ox_top + al_t

# PR planarizes: thicker in the recessed window, thinner over the raised oxide.
def smooth(y, w):
    k = np.ones(w) / w
    return np.convolve(np.pad(y, w, mode="edge"), k, mode="same")[w:-w]

pr_level = smooth(al_top, 301) * 0.35 + 0.65 * al_top.mean() + 1.4
pr_top = np.maximum(pr_level, al_top + 0.6)

fig, axes = plt.subplots(3, 1, figsize=(9, 10))

titles = ["(a) Before this lab: Si wafer with patterned SiO$_2$ from earlier labs",
          "(b) After Al thermal evaporation (blanket ~46 nm Al, thin on sidewalls)",
          "(c) After SPR220 spin-coat (2000 rpm, 60 s) + soft bake: ready for Lab 6 lithography"]
for i, ax in enumerate(axes):
    layer(ax, x, np.zeros_like(x), si_top, C["Si"])
    layer(ax, x, si_top, ox_top, C["SiO2"])
    if i >= 1:
        layer(ax, x, ox_top, al_top, C["Al"], edge=C["Al_edge"])
    if i >= 2:
        layer(ax, x, al_top, pr_top, C["PR"])
        ax.annotate("PR thickest in\nrecessed window", (5, pr_top[1000]), (5, 6.0), ha="center",
                    arrowprops=dict(arrowstyle="->"), fontsize=9)
        ax.annotate("PR thinner over\nraised features", (1.0, pr_top[200]), (1.2, 6.0), ha="center",
                    arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(titles[i], fontsize=10, loc="left")
    ax.set_xticks([]); ax.set_yticks([])

axes[0].legend(handles=[Patch(color=C["Si"], label="Si substrate"),
                        Patch(color=C["SiO2"], label="SiO$_2$"),
                        Patch(facecolor=C["Al"], edgecolor=C["Al_edge"], label="Al (~46 nm)"),
                        Patch(color=C["PR"], label="SPR220 photoresist (~3.2 µm)")],
               loc="upper right", fontsize=8, ncol=2)
fig.suptitle("Q5: Device cross-sections through the electrode area (not to scale)", fontsize=12)
fig.tight_layout()
fig.savefig("q5_device_cross_sections.png", dpi=140)

# ---------- Q4: thickness variation across the whole wafer ----------
fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7))
r = np.linspace(-50, 50, 2001)  # 100 mm wafer, mm
wafer_top = np.full_like(r, 1.0)
pr = 3.2 + 0.03 * (r / 50) ** 2                       # nearly flat in the centre
edge = np.exp(-(50 - np.abs(r)) / 1.2)                 # edge bead within ~1-3 mm of the rim
pr_profile = pr + 6.0 * edge
scale = 0.25
layer(ax1, r, np.zeros_like(r), wafer_top, C["Si"])
layer(ax1, r, wafer_top, wafer_top + 0.05, C["Al"], edge=C["Al_edge"])
layer(ax1, r, wafer_top + 0.05, wafer_top + 0.05 + scale * pr_profile, C["PR"])
ax1.annotate("edge bead\n(thickest PR)", (48.5, 1.05 + scale * pr_profile[-30]), (35, 4.3),
             arrowprops=dict(arrowstyle="->"), fontsize=9)
ax1.annotate("edge bead", (-48.5, 1.05 + scale * pr_profile[30]), (-45, 4.3),
             arrowprops=dict(arrowstyle="->"), fontsize=9)
ax1.text(0, 2.3, "uniform ~3.2 µm across the centre", ha="center", fontsize=9)
ax1.set_xlim(-52, 52); ax1.set_ylim(0, 5)
ax1.set_xlabel("position across wafer (mm)")
ax1.set_yticks([])
ax1.set_title("(a) Whole wafer: photoresist is thickest at the rim (edge bead); vertical scale exaggerated",
              fontsize=10, loc="left")

layer(ax2, x, np.zeros_like(x), si_top, C["Si"])
layer(ax2, x, si_top, ox_top, C["SiO2"])
layer(ax2, x, ox_top, al_top, C["Al"], edge=C["Al_edge"])
layer(ax2, x, al_top, pr_top, C["PR"])
i_win, i_top = 1000, 200
ax2.annotate("", (5, al_top[i_win]), (5, pr_top[i_win]), arrowprops=dict(arrowstyle="<->"))
ax2.text(5.15, (al_top[i_win] + pr_top[i_win]) / 2, "thicker", fontsize=9)
ax2.annotate("", (1, al_top[i_top]), (1, pr_top[i_top]), arrowprops=dict(arrowstyle="<->"))
ax2.text(1.15, (al_top[i_top] + pr_top[i_top]) / 2, "thinner", fontsize=9)
ax2.set_xlim(0, 10); ax2.set_ylim(0, 6.5)
ax2.set_xticks([]); ax2.set_yticks([])
ax2.set_title("(b) Over device topography: resist levels out, so it is thicker in recessed areas",
              fontsize=10, loc="left")
fig2.suptitle("Q4: Photoresist thickness is not uniform (not to scale)", fontsize=12)
fig2.tight_layout()
fig2.savefig("q4_photoresist_thickness.png", dpi=140)
