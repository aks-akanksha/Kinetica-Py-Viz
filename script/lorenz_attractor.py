import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Lorenz System Constants ---
SIGMA = 10.0
RHO = 28.0
BETA = 8.0 / 3.0
DT = 0.01
NUM_STEPS = 4000

# --- Pre-calculate the points ---
def lorenz_system(x, y, z):
    dx_dt = SIGMA * (y - x)
    dy_dt = x * (RHO - z) - y
    dz_dt = x * y - BETA * z
    return dx_dt, dy_dt, dz_dt

points = np.zeros((NUM_STEPS, 3))
points[0] = [0.1, 0., 20.] # Initial point

for i in range(NUM_STEPS - 1):
    x, y, z = points[i]
    dx_dt, dy_dt, dz_dt = lorenz_system(x, y, z)
    points[i+1] = [x + dx_dt * DT, y + dy_dt * DT, z + dz_dt * DT]

# --- Set up the plot ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.set_facecolor('black')

# Set fixed axis limits to contain the entire attractor
ax.set_xlim(points[:, 0].min() - 2, points[:, 0].max() + 2)
ax.set_ylim(points[:, 1].min() - 2, points[:, 1].max() + 2)
ax.set_zlim(points[:, 2].min() - 2, points[:, 2].max() + 2)
ax.set_axis_off()

line, = ax.plot([], [], [], lw=0.7, color='cyan')

# --- Animation Logic ---
def update(frame):
    # Draw the line up to the current frame
    line.set_data(points[:frame, 0], points[:frame, 1])
    line.set_3d_properties(points[:frame, 2])
    # Slowly rotate the camera angle
    ax.view_init(elev=30., azim=frame * 0.25)
    return line,

# --- Run the Animation ---
ani = FuncAnimation(fig, update, frames=NUM_STEPS, interval=5, blit=True, repeat=False)

plt.show()

