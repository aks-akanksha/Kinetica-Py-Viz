import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Iterated Function System (IFS) for the fern ---
# Each function is a transformation [a, b, c, d, e, f] and a probability p
# New (x, y) = (ax + by + e, cx + dy + f)
functions = [
    (0, 0, 0, 0.16, 0, 0, 0.01),          # Stem
    (0.85, 0.04, -0.04, 0.85, 0, 1.6, 0.85), # Successive leaflets
    (0.2, -0.26, 0.23, 0.22, 0, 1.6, 0.07), # Left leaflet
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07) # Right leaflet
]

# --- Setup ---
NUM_POINTS_PER_FRAME = 25
points = np.zeros((1, 2))
x, y = 0, 0

fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(0, 10)
fig.tight_layout()

scatter = ax.scatter([], [], s=0.5, c='green', alpha=0.8)

# --- Animation ---
def update(frame):
    global x, y, points
    for _ in range(NUM_POINTS_PER_FRAME):
        # Choose a function based on probability
        p = np.random.rand()
        cumulative_p = 0
        for a, b, c, d, e, f, prob in functions:
            cumulative_p += prob
            if p <= cumulative_p:
                x_new = a * x + b * y + e
                y_new = c * x + d * y + f
                x, y = x_new, y_new
                points = np.vstack((points, [x, y]))
                break
    
    scatter.set_offsets(points)
    return scatter,

ani = FuncAnimation(fig, update, frames=1000, interval=10, blit=True, repeat=False)

plt.show()
