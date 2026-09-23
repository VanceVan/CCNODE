"""ICM HW3, Bonus Question 6: visualize the convolution of
f(x) = 1 for |x| <= 1 and g(x) = x for 0 <= x <= 1."""
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.where(np.abs(x) <= 1, 1.0, 0.0)
g = lambda x: np.where((x >= 0) & (x <= 1), x, 0.0)


def conv_exact(x):
    x = np.asarray(x, dtype=float)
    return np.select(
        [(x >= -1) & (x < 0), (x >= 0) & (x < 1), (x >= 1) & (x <= 2)],
        [(x + 1) ** 2 / 2, 0.5 * np.ones_like(x), (1 - (x - 1) ** 2) / 2],
        default=0.0)


t = np.linspace(-3, 4, 7001)
dt = t[1] - t[0]
shifts = [-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5]

fig, axes = plt.subplots(3, 3, figsize=(12, 9), sharex=True, sharey=True)
for ax, x in zip(axes.flat, shifts):
    prod = f(t) * g(x - t)
    ax.plot(t, f(t), color="tab:blue", label="f(t)")
    ax.plot(t, g(x - t), color="tab:orange", label="g(x - t)")
    ax.fill_between(t, prod, color="tab:green", alpha=0.4, label="overlap f(t)g(x-t)")
    ax.set_title(f"x = {x}:  area = {np.sum(prod) * dt:.2f}  (exact {conv_exact(x):.3f})")
    ax.set_xlim(-2.5, 3.5)
    ax.set_ylim(-0.1, 1.3)
    ax.grid(True, alpha=0.3)
axes[0, 0].legend(loc="upper left", fontsize=8)
fig.suptitle("Q6(a): g(x - t) sweeping across f(t)")
fig.tight_layout()
fig.savefig("q6a_sweep.png", dpi=130)

# (c) domain in the (x, t) plane where f(t) g(x - t) != 0
fig2, ax2 = plt.subplots(figsize=(6, 5))
X, Tt = np.meshgrid(np.linspace(-2, 3, 600), np.linspace(-2, 2, 600))
ax2.contourf(X, Tt, (f(Tt) * g(X - Tt)) > 0, levels=[0.5, 1.5], colors=["tab:green"], alpha=0.5)
xs = np.linspace(-2, 3, 10)
ax2.plot(xs, xs, "k--", label="t = x")
ax2.plot(xs, xs - 1, "k:", label="t = x - 1")
ax2.axhline(1, color="tab:blue", label="t = +/-1")
ax2.axhline(-1, color="tab:blue")
for xv in (-1, 0, 1, 2):
    ax2.axvline(xv, color="gray", lw=0.8)
ax2.set_xlabel("x")
ax2.set_ylabel("t")
ax2.set_title("Q6(c): region where f(t) g(x - t) is non-zero")
ax2.legend(loc="lower right", fontsize=8)
fig2.tight_layout()
fig2.savefig("q6c_domain.png", dpi=130)

# (f) numerical convolution vs. exact piecewise result
fig3, ax3 = plt.subplots(figsize=(7, 4))
xg = np.linspace(-2, 3, 501)
numeric = [np.sum(f(t) * g(x - t)) * dt for x in xg]
ax3.plot(xg, conv_exact(xg), lw=3, label="exact (f*g)(x)")
ax3.plot(xg, numeric, "--", label="numerical overlap area")
ax3.scatter(shifts, conv_exact(np.array(shifts)), color="red", zorder=5,
            label="areas from panels in (a)")
ax3.set_xlabel("x")
ax3.set_title("Q6(f): convolution = overlap area")
ax3.grid(True, alpha=0.3)
ax3.legend()
fig3.tight_layout()
fig3.savefig("q6f_convolution.png", dpi=130)
plt.show()
