import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configuration ---
GRID_RES = 10
GRID_SIZE = 100
NUM_PARTICLES = 500
TIME_STEP = 0.1

# --- Flow Field Setup ---
# Create a low-resolution grid of random angles
low_res_angles = np.random.uniform(0, 2 * np.pi, (GRID_RES, GRID_RES))
# Create high-resolution grid by scaling up
angles = np.kron(low_res_angles, np.ones((GRID_SIZE//GRID_RES, GRID_SIZE//GRID_RES)))
flow_field_x = np.cos(angles)
flow_field_y = np.sin(angles)

# --- Particle Setup ---
particles = np.random.rand(NUM_PARTICLES, 2) * GRID_SIZE
particle_colors = np.random.rand(NUM_PARTICLES)

# --- Plotting Setup ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('black')
ax.set_xlim(0, GRID_SIZE)
ax.set_ylim(0, GRID_SIZE)
ax.set_xticks([])
ax.set_yticks([])
scatter = ax.scatter(particles[:, 0], particles[:, 1], c=particle_colors, cmap='cool', s=2, alpha=0.7)

# --- Animation ---
def update(frame):
    # Get grid indices for each particle
    ix = np.floor(particles[:, 0]).astype(int)
    iy = np.floor(particles[:, 1]).astype(int)

    # Handle particles that go out of bounds
    ix = np.clip(ix, 0, GRID_SIZE - 1)
    iy = np.clip(iy, 0, GRID_SIZE - 1)
    
    # Update particle positions based on flow field
    particles[:, 0] += flow_field_x[iy, ix] * TIME_STEP
    particles[:, 1] += flow_field_y[iy, ix] * TIME_STEP

    # Periodic boundary conditions (wrap around)
    particles[:, 0] = particles[:, 0] % GRID_SIZE
    particles[:, 1] = particles[:, 1] % GRID_SIZE
    
    scatter.set_offsets(particles)
    return scatter,

ani = FuncAnimation(fig, update, frames=500, interval=10, blit=True)
plt.show()
