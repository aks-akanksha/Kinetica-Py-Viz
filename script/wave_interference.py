import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configuration ---
GRID_SIZE = 300
WAVELENGTH = 25.0
FREQUENCY = 0.1
SOURCE1_POS = (GRID_SIZE // 4, GRID_SIZE // 2)
SOURCE2_POS = (3 * GRID_SIZE // 4, GRID_SIZE // 2)

# --- Setup ---
x = np.arange(0, GRID_SIZE)
y = np.arange(0, GRID_SIZE)
X, Y = np.meshgrid(x, y)

dist1 = np.sqrt((X - SOURCE1_POS[0])**2 + (Y - SOURCE1_POS[1])**2)
dist2 = np.sqrt((X - SOURCE2_POS[0])**2 + (Y - SOURCE2_POS[1])**2)

fig, ax = plt.subplots(figsize=(10, 10))
img = ax.imshow(np.zeros((GRID_SIZE, GRID_SIZE)), cmap='ocean', vmin=-2, vmax=2)
ax.axis('off')
ax.set_title("Wave Interference", color='white', fontsize=16)
fig.set_facecolor('black')

# --- Animation ---
def update(frame):
    k = 2 * np.pi / WAVELENGTH
    wave1 = np.sin(k * dist1 - FREQUENCY * frame)
    wave2 = np.sin(k * dist2 - FREQUENCY * frame)
    interference_pattern = wave1 + wave2
    
    img.set_array(interference_pattern)
    return img,

ani = FuncAnimation(fig, update, frames=300, interval=20, blit=True, repeat=False)

plt.show()

