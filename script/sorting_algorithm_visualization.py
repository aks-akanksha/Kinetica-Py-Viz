import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configuration ---
NUM_ELEMENTS = 75
ALGORITHM = "Bubble Sort"

# --- Setup ---
data = np.arange(1, NUM_ELEMENTS + 1)
np.random.shuffle(data)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(ALGORITHM)
ax.set_xticks([])
ax.set_yticks([])
container = ax.bar(np.arange(NUM_ELEMENTS), data, color='#0077b6')
fig.tight_layout()

# --- Sorting Logic (Generator) ---
def bubble_sort(arr):
    n = len(arr)
    colors = ['#0077b6'] * n
    for i in range(n):
        swapped_in_pass = False
        for j in range(0, n - i - 1):
            colors[j] = '#fb8500'
            colors[j+1] = '#fb8500'
            yield arr, colors
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped_in_pass = True
                colors[j] = '#d00000'
                colors[j+1] = '#d00000'
                yield arr, colors
            colors[j] = '#0077b6'
            colors[j+1] = '#0077b6'
        colors[n - 1 - i] = '#8ac926'
        if not swapped_in_pass:
            for k in range(n-i-1): colors[k] = '#8ac926'
            break
    yield arr, ['#8ac926'] * n

sort_generator = bubble_sort(data.copy())

# --- Animation ---
def update(frame):
    try:
        arr, new_colors = next(sort_generator)
        for bar, h, c in zip(container.patches, arr, new_colors):
            bar.set_height(h)
            bar.set_color(c)
    except StopIteration:
        ani.event_source.stop()
    return list(container)

ani = FuncAnimation(fig, update, interval=1, blit=True, cache_frame_data=False, repeat=False)

plt.show()

