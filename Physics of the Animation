A Deeper Look: The Physics and Mathematics of the Animations
This document explains the scientific and mathematical principles behind some of the more complex animations in this collection.

1. Black Hole Accretion Disk
Core Concept: Newtonian Gravity and Orbital Mechanics. While a real black hole requires General Relativity, this simulation provides a compelling visual using classical physics.

Formulation:
The primary force is Newton's Law of Universal Gravitation, simplified for our simulation where the black hole's mass and the particle's mass are absorbed into a single constant, G':
$$ F = \frac{G'}{r^2} $$
Where F is the force magnitude and r is the distance from the particle to the center. Since F=ma and we assume particle mass m=1, the acceleration is a=F. This acceleration vector always points towards the center.

To create the swirl, a tangential velocity is added. This prevents particles from falling straight in and forces them into an orbit. The combination of the inward pull and the sideways velocity creates the elliptical/spiral paths. The relativistic jets are a visual addition inspired by astrophysics, where powerful jets of plasma are ejected from the poles of rotating black holes.

2. Double Pendulum
Core Concept: Classical Mechanics and Chaos Theory. The double pendulum is a canonical example of a chaotic system. Its motion is completely determined by its starting conditions, but an infinitesimally small change in those conditions will lead to a wildly different outcome over time.

Formulation:
The equations of motion are too complex to derive here, but they are found using the Lagrangian formulation of classical mechanics. The Lagrangian L is the difference between the kinetic energy (T) and potential energy (V) of the system:
$$ \mathcal{L} = T - V $$
For the double pendulum, this involves the angles (θ 
1
​
 ,θ 
2
​
 ) and angular velocities ( 
θ
˙
  
1
​
 , 
θ
˙
  
2
​
 ) of both masses. The equations of motion are then found by solving the Euler-Lagrange equations:
$$ \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\theta}_i} \right) - \frac{\partial \mathcal{L}}{\partial \theta_i} = 0 \quad \text{for } i=1,2 $$
The script does not derive these, but implements their final form in the double_pendulum_deriv function, which is then solved numerically.

3. Lorenz Attractor
Core Concept: Dynamical Systems and Chaos Theory. The Lorenz system is a simplified mathematical model for atmospheric convection. The resulting "attractor" is a set of points in 3D space towards which the system evolves. It's a "strange attractor" because it has a fractal structure.

Formulation: The system is governed by three coupled, non-linear ordinary differential equations:

dt
dx
​
 
dt
dy
​
 
dt
dz
​
 
​
  
=σ(y−x)
=x(ρ−z)−y
=xy−βz
​
 
Here, x,y,z represent the state of the system (e.g., convection intensity, temperature differences), and σ,ρ,β are system parameters. The script numerically integrates these equations step-by-step using a simple method (Euler integration) to trace the path of the system through phase space.

4. Wave Interference
Core Concept: The Principle of Superposition. This principle states that for linear systems, the net response at a given place and time caused by two or more stimuli is the sum of the responses that would have been caused by each stimulus individually.

Formulation: A simple harmonic wave emanating from a source can be described by:
$$ A(r, t) = \sin(k \cdot r - \omega \cdot t) $$
Where A is the amplitude, r is the distance from the source, t is time, k is the wave number (2π/λ), and ω is the angular frequency (2π⋅f).

In the simulation, we have two waves, A 
1
​
  and A 
2
​
 . The interference pattern is simply their sum at every point in the grid:
$$ A_{\text{total}}(x, y, t) = A_1(r_1, t) + A_2(r_2, t) $$
Where r 
1
​
  and r 
2
​
  are the distances from point (x,y) to each source.

5. Reaction-Diffusion
Core Concept: Turing Patterns and Morphogenesis. This simulates the Gray-Scott model, which describes how two chemical substances (U and V) can spread (diffuse) and react with each other to form stable, complex patterns from a nearly uniform state. It's a proposed mechanism for how patterns on animal coats (e.g., zebra stripes) form.

Formulation: The system is described by a pair of partial differential equations:

∂t
∂U
​
 
∂t
∂V
​
 
​
  
=D 
u
​
 ∇ 
2
 U−UV 
2
 +f(1−U)
=D 
v
​
 ∇ 
2
 V+UV 
2
 −(k+f)V
​
 
D 
u
​
 ,D 
v
​
  are the diffusion rates of the two chemicals.

∇ 
2
  is the Laplacian operator, which represents diffusion (the script approximates this with a convolution).

f is the "feed rate" of chemical U, and k is the "kill rate" of chemical V. These two parameters are critical. The entire landscape of possible patterns is determined by their values.

The script is now tuned with f=0.0367 and k=0.0649. This specific combination creates a mesmerizing "mitotic" pattern, where spots grow, stretch, and divide in a process that looks strikingly similar to cell division.