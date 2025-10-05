import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.fft import fft

# --- Signal (Shape to Draw - Letter 'G') ---
path_g = [
    3.7+1j, 3+1j, 2+1j, 1.5+1.5j, 1+2j, 1+3j, 1+4j, 1.5+4.5j, 2+5j, 3+5j, 3.7+5j,
    3.7+4j, 3+4j, 2.5+4j, 2.5+3j, 3.5+3j, 3.5+2j, 3.7+2j, 3.7+1j
]
# Interpolate to create more points for a smoother shape
t = np.linspace(0, 1, 500)
signal = np.interp(t, np.linspace(0, 1, len(path_g)), np.array(path_g))

# --- Fourier Transform ---
NUM_COEFFS = 100 # Use fewer coefficients for better performance
fourier_coeffs = fft(signal)
freqs = np.fft.fftfreq(len(signal), d=t[1]-t[0])
sorted_indices = np.argsort(np.abs(freqs))
sorted_coeffs = fourier_coeffs[sorted_indices][:NUM_COEFFS]
sorted_freqs = freqs[sorted_indices][:NUM_COEFFS]

# --- Setup Plot ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 7)
ax.axis('off')
ax.set_facecolor('black')

circles = [ax.plot([], [], 'r-', lw=0.5, alpha=0.3)[0] for _ in range(NUM_COEFFS)]
vectors = [ax.plot([], [], 'w-', lw=0.8)[0] for _ in range(NUM_COEFFS)]
drawing_line, = ax.plot([], [], 'c-', lw=2)
path_x, path_y = [], []

# --- Animation ---
def animate(i):
    global path_x, path_y
    time = t[i]
    center = 0 + 0j
    
    for k in range(NUM_COEFFS):
        coeff = sorted_coeffs[k] / len(signal)
        freq = sorted_freqs[k]
        radius = np.abs(coeff)
        
        circle_points = np.exp(1j * np.linspace(0, 2*np.pi, 50)) * radius + center
        circles[k].set_data(circle_points.real, circle_points.imag)

        new_center = center + coeff * np.exp(2 * np.pi * 1j * freq * time)
        vectors[k].set_data([center.real, new_center.real], [center.imag, new_center.imag])
        center = new_center

    path_x.append(center.real)
    path_y.append(center.imag)
    drawing_line.set_data(path_x, path_y)

    if i == len(t) - 1:
        path_x, path_y = [], []

    return circles + vectors + [drawing_line]

ani = FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)
plt.show()

