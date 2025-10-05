import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm

# --- Setup ---
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.set_facecolor('black')
ax.set_axis_off()

# Create the meshgrid
x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# --- Animation ---
def update(frame):
    ax.clear() # Clear the previous frame
    ax.set_axis_off()
    ax.set_zlim(-1.5, 1.5)

    # Calculate Z based on distance from center and time
    Z = np.sin(R - frame * 0.1)
    
    # Plot the surface
    surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, rstride=1, cstride=1, antialiased=False)
    
    # Rotate view
    ax.view_init(elev=40., azim=frame * 0.5)
    return surf,

ani = FuncAnimation(fig, update, frames=300, interval=20, blit=False)
plt.show()
