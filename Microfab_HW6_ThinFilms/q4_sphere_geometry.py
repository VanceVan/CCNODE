"""HW6 Thin Films, Q4: geometry of a source and wafer on the inside of a sphere."""
import numpy as np
import matplotlib.pyplot as plt

r0 = 1.0
fig, ax = plt.subplots(figsize=(5.5, 5.5))
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(r0 * np.cos(t), r0 * np.sin(t), color="0.3", lw=1.5)

C = np.array([0.0, 0.0])
S = np.array([0.0, -r0])                       # source at the bottom, facing the centre
phi = np.deg2rad(55)                            # wafer position on the sphere
Wf = np.array([r0 * np.sin(phi), r0 * np.cos(phi)])

ax.plot(*zip(C, S), "k-", lw=1.2)
ax.plot(*zip(C, Wf), "k-", lw=1.2)
ax.plot(*zip(S, Wf), color="tab:orange", lw=2)
ax.plot(*C, "ko", ms=4)

# source and wafer as short plates tangent to the sphere
ax.plot([-0.12, 0.12], [-r0, -r0], color="tab:blue", lw=5)
tang = np.array([np.cos(phi), -np.sin(phi)])
ax.plot(*zip(Wf - 0.12 * tang, Wf + 0.12 * tang), color="tab:blue", lw=5)

ax.text(-0.13, -0.5, "r₀", fontsize=13)
ax.text(Wf[0] / 2 - 0.13, Wf[1] / 2 + 0.03, "r₀", fontsize=13)
mid = (S + Wf) / 2
ax.text(mid[0] + 0.05, mid[1] - 0.05, "r = 2r₀ cos θ", fontsize=12, color="tab:orange")
ax.text(0.03, -0.78, "θᵢ", fontsize=13)
ax.text(Wf[0] - 0.22, Wf[1] - 0.25, "θₖ", fontsize=13)
ax.text(S[0] - 0.18, S[1] - 0.13, "Source", fontsize=11)
ax.text(Wf[0] + 0.06, Wf[1] + 0.05, "Wafer", fontsize=11)
ax.text(0.05, 0.05, "centre", fontsize=9)
ax.set_title("Isosceles triangle: θᵢ = θₖ = θ, so r = 2r₀ cos θ", fontsize=11)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig("q4_sphere_geometry.png", dpi=150)
