import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configuration ---
NUM_PARTICLES = 2000
GRAVITATIONAL_CONSTANT = 1200.0
EVENT_HORIZON_RADIUS = 20.0
JET_THRESHOLD_RADIUS = 25.0
JET_SPEED = 8.0

# --- Set up the plot ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('black')
ax.set_xlim(-500, 500)
ax.set_ylim(-500, 500)
ax.set_xticks([])
ax.set_yticks([])
fig.tight_layout()

# The central black hole "event horizon"
ax.add_patch(plt.Circle((0, 0), EVENT_HORIZON_RADIUS, color='black', zorder=10))
# A faint glow representing the photon sphere
ax.add_patch(plt.Circle((0, 0), EVENT_HORIZON_RADIUS * 1.5, color='cyan', alpha=0.3, zorder=9))


# --- Particle Initialization ---
positions = np.random.randn(NUM_PARTICLES, 2) * 200
velocities = np.zeros((NUM_PARTICLES, 2))
states = np.zeros(NUM_PARTICLES, dtype=int) # 0: in disk, 1: in jet
colors = np.zeros((NUM_PARTICLES, 4))
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=10, alpha=0.8)

# --- Animation Logic ---
def update(frame):
    global positions, velocities, states

    distances = np.sqrt(positions[:, 0]**2 + positions[:, 1]**2)
    
    # --- Reset particles that are too far away or fell in ---
    reset_mask = (distances > 500) | (distances < EVENT_HORIZON_RADIUS)
    num_to_reset = np.sum(reset_mask)
    if num_to_reset > 0:
        angle = np.random.uniform(0, 2 * np.pi, num_to_reset)
        radius = np.random.uniform(450, 500, num_to_reset)
        positions[reset_mask] = np.array([radius * np.cos(angle), radius * np.sin(angle)]).T
        velocities[reset_mask] = 0
        states[reset_mask] = 0

    # --- Find particles to be ejected in jets ---
    jet_mask = (distances < JET_THRESHOLD_RADIUS) & (states == 0)
    num_jets = np.sum(jet_mask)
    if num_jets > 0:
        states[jet_mask] = 1
        velocities[jet_mask, 0] = np.random.uniform(-0.5, 0.5, num_jets)
        velocities[jet_mask, 1] = np.sign(np.random.uniform(-1, 1, num_jets)) * JET_SPEED

    # --- Physics for particles in the accretion disk ---
    disk_mask = (states == 0)
    disk_distances = distances[disk_mask]
    disk_positions = positions[disk_mask]
    
    force_magnitude = GRAVITATIONAL_CONSTANT / (disk_distances**2)
    force_direction = -disk_positions / disk_distances[:, np.newaxis]
    acceleration = force_magnitude[:, np.newaxis] * force_direction
    
    orbital_velocity = np.zeros_like(disk_positions)
    orbital_velocity[:, 0] = -disk_positions[:, 1] / disk_distances
    orbital_velocity[:, 1] = disk_positions[:, 0] / disk_distances
    
    velocities[disk_mask] += acceleration + orbital_velocity * np.sqrt(force_magnitude)[:, np.newaxis] * 0.15

    # --- Update all positions ---
    positions += velocities * 0.1

    # --- Update colors and sizes ---
    # Disk particles get colored by distance (hotter closer)
    norm_dist = np.clip(distances[disk_mask] / 400, 0, 1)
    colors[disk_mask] = plt.get_cmap('hot')(norm_dist)
    
    # Jet particles are bright cyan
    colors[states == 1] = [0.7, 0.9, 1.0, 0.9]

    sizes = np.clip(1000 / distances, 0.1, 20)
    
    scatter.set_offsets(positions)
    scatter.set_facecolors(colors)
    scatter.set_sizes(sizes)

    return scatter,

ani = FuncAnimation(fig, update, frames=200, interval=20, blit=True, repeat=False)

plt.show()

