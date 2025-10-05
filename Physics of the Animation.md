## 📚 A Deeper Look: Physics & Math Behind the Animations

### 1) Black Hole Accretion Disk (Newtonian toy model)

**Core concept:** Central inverse-square force + initial tangential velocity.

**Force law (simplified):**
[
F = \frac{G'}{r^2}, \qquad \vec a = -,\frac{G'}{r^2},\hat{\mathbf r}
]
We add an initial tangential speed to avoid radial infall and produce spiral/elliptic orbits. “Jets” are a visual flourish inspired by real systems.

---

### 2) Double Pendulum (chaos)

**Core concept:** Lagrangian mechanics and sensitive dependence on initial conditions.

**Lagrangian:**
[
\mathcal L = T - V
]
with generalized coordinates (\theta_1,\theta_2). Equations of motion follow from the Euler–Lagrange equations:
[
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot\theta_i}\right)

* \frac{\partial \mathcal L}{\partial \theta_i} = 0,\quad i=1,2.
  ]
  The code integrates the standard closed-form equations for a double pendulum.

---

### 3) Lorenz Attractor (chaotic flow)

**Core concept:** Nonlinear ODEs exhibiting a strange attractor.

[
\begin{aligned}
\dot x &= \sigma (y - x),\
\dot y &= x(\rho - z) - y,\
\dot z &= x y - \beta z,
\end{aligned}
]
with parameters (\sigma,\rho,\beta). The trajectory is obtained by numerically integrating these ODEs.

---

### 4) Wave Interference (superposition)

A harmonic wave from a point source:
[
A(r,t) = \sin(k r - \omega t), \quad k=\tfrac{2\pi}{\lambda},\ \omega=2\pi f.
]
For two sources at distances (r_1, r_2):
[
A_{\text{total}}(x,y,t) = A_1(r_1,t) + A_2(r_2,t).
]

---

### 5) Reaction–Diffusion (Gray–Scott)

**Core concept:** Diffusion + nonlinear reaction yields Turing-like patterns.

[
\begin{aligned}
\frac{\partial u}{\partial t} &= D_u \nabla^2 u - u v^2 + F(1-u),\
\frac{\partial v}{\partial t} &= D_v \nabla^2 v + u v^2 - (F+k),v,
\end{aligned}
]
where (D_u, D_v) are diffusion rates, (F) is the feed rate, and (k) is the kill rate. Discrete convolution approximates (\nabla^2). Specific ((F,k)) pairs yield “mitotic” spot-splitting patterns.
