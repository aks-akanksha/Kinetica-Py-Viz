import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d

# --- Configuration ---
GRID_SIZE = 200
# Diffusion rates, feed/kill rates for "mitotic" pattern
Du, Dv = 0.16, 0.08
f, k = 0.0367, 0.0649

# --- Setup ---
U = np.ones((GRID_SIZE, GRID_SIZE))
V = np.zeros((GRID_SIZE, GRID_SIZE))

# Add a small seed area to start the reaction
seed_size = 25
mid = GRID_SIZE // 2
U[mid-seed_size//2:mid+seed_size//2, mid-seed_size//2:mid+seed_size//2] = 0.50
V[mid-seed_size//2:mid+seed_size//2, mid-seed_size//2:mid+seed_size//2] = 0.25
U += 0.02 * np.random.rand(GRID_SIZE, GRID_SIZE)
V += 0.02 * np.random.rand(GRID_SIZE, GRID_SIZE)

fig, ax = plt.subplots(figsize=(10, 10))
# Using a different colormap for a new look
img = ax.imshow(V, cmap='twilight_shifted', interpolation='bicubic')
ax.axis('off')

# Laplacian kernel
laplacian_kernel = np.array([[0.05, 0.2, 0.05],
                           [0.2, -1, 0.2],
                           [0.05, 0.2, 0.05]])

# --- Animation ---
def update(frame):
    global U, V
    # Run multiple simulation steps per frame for speed
    for _ in range(10):
        lap_U = convolve2d(U, laplacian_kernel, mode='same', boundary='wrap')
        lap_V = convolve2d(V, laplacian_kernel, mode='same', boundary='wrap')
        
        uvv = U * V * V
        
        U += Du * lap_U - uvv + f * (1 - U)
        V += Dv * lap_V + uvv - (k + f) * V
        
    img.set_array(V)
    img.set_clim(V.min(), V.max()) # Auto-adjust color scale
    return img,

ani = FuncAnimation(fig, update, interval=10, blit=True)
plt.show()

