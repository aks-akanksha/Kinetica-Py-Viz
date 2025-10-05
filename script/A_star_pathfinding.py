import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import heapq

# --- Grid and Obstacles Setup ---
GRID_SIZE = (30, 40)
START_NODE = (5, 5)
GOAL_NODE = (25, 35)
OBSTACLE_PROB = 0.3

grid = np.zeros(GRID_SIZE)
grid[START_NODE] = 0.8
grid[GOAL_NODE] = 0.9

# Generate obstacles
obstacles = np.random.rand(*GRID_SIZE) < OBSTACLE_PROB
grid[obstacles] = 1.0
grid[START_NODE] = 0.8
grid[GOAL_NODE] = 0.9

# --- A* Algorithm Logic (Generator) ---
def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in np.ndindex(grid.shape)}
    g_score[start] = 0
    f_score = {node: float('inf') for node in np.ndindex(grid.shape)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            yield {'path': path[::-1]}
            return
        yield {'closed': current}
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1] and grid[neighbor] != 1:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        yield {'open': neighbor}
    yield {}

# --- Animation Setup ---
fig, ax = plt.subplots(figsize=(10, 8))
img = ax.imshow(grid, cmap='terrain_r', vmin=0, vmax=1)
ax.axis('off')
status_text = ax.text(0.02, 0.95, "Searching...", transform=ax.transAxes, color='white', fontsize=14, bbox=dict(facecolor='black', alpha=0.5))
path_generator = a_star(grid, START_NODE, GOAL_NODE)

def update(frame):
    try:
        for _ in range(5): # Run 5 steps of the algorithm per frame
            update_info = next(path_generator)
            if 'open' in update_info and grid[update_info['open']] == 0:
                grid[update_info['open']] = 0.3
            if 'closed' in update_info and grid[update_info['closed']] != 0.8:
                grid[update_info['closed']] = 0.5
            if 'path' in update_info:
                for node in update_info['path']:
                    if grid[node] != 0.8 and grid[node] != 0.9:
                        grid[node] = 0.7
                status_text.set_text("Path Found!")
                ani.event_source.stop()
                break # Exit the inner loop
        img.set_array(grid)
    except StopIteration:
        status_text.set_text("No Path Found!")
        ani.event_source.stop()
    return [img]

ani = FuncAnimation(fig, update, interval=1, blit=True, repeat=False)

plt.show()