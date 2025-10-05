import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# --- Simulation Constants ---
G = 9.81  # Acceleration due to gravity (m/s^2)
L1, L2 = 1.0, 1.0  # Length of pendulums (m)
M1, M2 = 1.0, 1.0  # Mass of pendulums (kg)
THETA1_0, THETA2_0 = np.pi / 2, np.pi  # Initial angles (rad)
W1_0, W2_0 = 0.0, 0.0  # Initial angular velocities (rad/s)

# --- Equations of Motion ---
def double_pendulum_deriv(t, y):
    theta1, w1, theta2, w2 = y
    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    theta1_dot = w1
    w1_dot = (M2*G*np.sin(theta2)*c - M2*s*(L1*w1**2*c + L2*w2**2) - (M1+M2)*G*np.sin(theta1)) / (L1 * (M1 + M2*s**2))
    theta2_dot = w2
    w2_dot = ((M1+M2)*(L1*w1**2*s - G*np.sin(theta2) + G*np.sin(theta1)*c) + M2*L2*w2**2*s*c) / (L2 * (M1 + M2*s**2))
    
    return theta1_dot, w1_dot, theta2_dot, w2_dot

# --- Solve the ODE ---
t_span = [0, 40]
dt = 0.025
t_eval = np.arange(t_span[0], t_span[1], dt)
y0 = [THETA1_0, W1_0, THETA2_0, W2_0]
sol = solve_ivp(double_pendulum_deriv, t_span, y0, t_eval=t_eval, dense_output=True)
theta1, theta2 = sol.y[0, :], sol.y[2, :]

# Convert to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# --- Plotting ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-L1-L2-0.5, L1+L2+0.5)
ax.set_ylim(-L1-L2-0.5, L1+L2+0.5)
ax.set_aspect('equal')
ax.axis('off')

line, = ax.plot([], [], 'o-', lw=2, color='cyan')
trace, = ax.plot([], [], '-', lw=0.5, color='red', alpha=0.7)

# --- Animation ---
def animate(i):
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    trace.set_data(x2[:i], y2[:i])
    return line, trace

ani = FuncAnimation(fig, animate, frames=len(t_eval), interval=dt*1000, blit=True)
plt.show()
