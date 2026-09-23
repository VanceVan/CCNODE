"""ICM HW3, Question 2(v): apply T(x, y) = (x + 3y, 2x + y) to the square
with vertices [0,0], [3,0], [3,3], [0,3] and plot the result."""
import numpy as np
import matplotlib.pyplot as plt

# Transformation matrix (also the Jacobian from part ii)
T = np.array([[1, 3],
              [2, 1]])

# Square vertices as columns; repeat the first vertex to close the polygon
square = np.array([[0, 3, 3, 0, 0],
                   [0, 0, 3, 3, 0]])

transformed = T @ square


def shoelace_area(pts):
    x, y = pts[0, :-1], pts[1, :-1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


print("Original vertices:\n", square[:, :-1].T)
print("Transformed vertices:\n", transformed[:, :-1].T)
print("det(T) =", round(np.linalg.det(T), 6))
print("Original area    =", shoelace_area(square))
print("Transformed area =", shoelace_area(transformed))

fig, ax = plt.subplots(figsize=(7, 7))
ax.fill(square[0], square[1], alpha=0.3, color="tab:blue", label="Original square")
ax.plot(square[0], square[1], "o-", color="tab:blue")
ax.fill(transformed[0], transformed[1], alpha=0.3, color="tab:orange",
        label="Transformed: (x + 3y, 2x + y)")
ax.plot(transformed[0], transformed[1], "o-", color="tab:orange")

for (x0, y0), (x1, y1) in zip(square[:, :-1].T, transformed[:, :-1].T):
    ax.annotate(f"({x0},{y0})", (x0, y0), textcoords="offset points", xytext=(-30, -12), color="tab:blue")
    ax.annotate(f"({x1},{y1})", (x1, y1), textcoords="offset points", xytext=(5, 5), color="tab:orange")

ax.set_title("Linear transformation of the square  (det J = -5, area 9 -> 45)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axhline(0, color="gray", lw=0.8)
ax.axvline(0, color="gray", lw=0.8)
ax.set_aspect("equal")
ax.grid(True, alpha=0.4)
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("q2v_result.png", dpi=150)
plt.show()
