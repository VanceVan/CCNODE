"""ICM HW6, Question 5: smooth a noisy sine with the Green's kernel of
A = -d^3/dx^3 - d^2/dx^2 + d/dx + 1 = (1 + d/dx)^2 (1 - d/dx).

From Question 4, A k = delta is solved by
    k(x) = (e^{-x} u(x)) * (e^{-|x|} / 2)
         = (2x + 1) e^{-x} / 4   for x >= 0
         = e^{x} / 4             for x <  0
"""
import numpy as np
import matplotlib.pyplot as plt


def greens_kernel(x):
    return np.where(x >= 0, (2 * x + 1) * np.exp(-x) / 4, np.exp(x) / 4)


rng = np.random.default_rng(seed=0)  # fixed seed so the figure is reproducible

N = 2001
x = np.linspace(-2 * np.pi, 2 * np.pi, N)
dx = x[1] - x[0]

clean = np.sin(x)
noise = rng.uniform(0, 1, N)          # random values in [0, 1]
noisy = clean + noise

# v(x) = (k * p)(x) = integral k(x - y) p(y) dy, approximated by a Riemann sum
# over the samples in [-2pi, 2pi] (the signal is taken to be 0 outside).
K = greens_kernel(x[:, None] - x[None, :])
smoothed = K @ noisy * dx

# Prediction for the interior (far from the edges): k has area 1, so the
# mean noise level 0.5 passes through unchanged, and sin(x) is multiplied by
# 1 / A(i) = 1 / (2 + 2i) = (1 - i) / 4, giving (sin x - cos x) / 4.
predicted = 0.5 + (np.sin(x) - np.cos(x)) / 4

print(f"kernel area (should be 1): {np.sum(greens_kernel(np.arange(-40, 40, dx))) * dx:.4f}")
print(f"noise std before: {np.std(noisy - clean - 0.5):.3f}")
interior = np.abs(x) < np.pi
print(f"max |smoothed - predicted| for |x| < pi: {np.max(np.abs(smoothed - predicted)[interior]):.3f}")

fig, axes = plt.subplots(3, 1, figsize=(9, 11))

kx = np.linspace(-6, 6, 1201)
axes[0].plot(kx, greens_kernel(kx), color="tab:purple")
axes[0].set_title("Green's kernel k(x) for A = -D³ - D² + D + 1")
axes[0].set_xlabel("x")
axes[0].grid(alpha=0.3)

axes[1].plot(x, noisy, color="tab:gray", lw=0.8, label="sin(x) + U[0,1] noise")
axes[1].plot(x, clean, color="tab:blue", lw=2, label="sin(x)")
axes[1].set_title("Noisy sine on [-2π, 2π]")
axes[1].set_xlabel("x")
axes[1].legend(loc="upper right")
axes[1].grid(alpha=0.3)

axes[2].plot(x, smoothed, color="tab:orange", lw=2, label="k * (noisy signal)")
axes[2].plot(x, predicted, "k--", lw=1, label="prediction 0.5 + (sin x - cos x)/4")
axes[2].plot(x, clean, color="tab:blue", lw=1, alpha=0.5, label="sin(x)")
axes[2].set_title("After convolving with the Green's kernel")
axes[2].set_xlabel("x")
axes[2].legend(loc="upper right", fontsize=8)
axes[2].grid(alpha=0.3)

fig.tight_layout()
fig.savefig("q5_result.png", dpi=130)
plt.show()
