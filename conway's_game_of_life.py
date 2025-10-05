import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configuration ---
GRID_SIZE = 120
UPDATE_INTERVAL = 20  # milliseconds

# --- Pattern Definitions ---
def add_pattern(grid, pattern, x, y):
    h, w = pattern.shape
    grid[x:x+h, y:y+w] = pattern

glider_gun = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

pulsar = np.array([
    [0,0,1,1,1,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [0,0,1,1,1,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,1,1,1,0,0],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,1,1,1,0,0]])

# --- Game Logic ---
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            total = int((grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                         grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                         grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                         grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]))
            if grid[i, j] == 1:
                if (total < 2) or (total > 3): new_grid[i, j] = 0
            elif total == 3: new_grid[i, j] = 1
    return new_grid

# --- Setup ---
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
add_pattern(grid, glider_gun, 10, 10)
add_pattern(grid, pulsar, 60, 60)
add_pattern(grid, np.flip(pulsar), 20, 80) # Flipped pulsar

fig, ax = plt.subplots(figsize=(10, 10))
img = ax.imshow(grid, interpolation='nearest', cmap='magma')
ax.axis('off')

# --- Animation ---
def animate(frame):
    global grid
    grid = update_grid(grid)
    img.set_array(grid)
    return img,

ani = FuncAnimation(fig, animate, interval=UPDATE_INTERVAL, blit=True)
plt.show()

