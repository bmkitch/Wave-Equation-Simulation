This is a Python script that solves the wave equation in two dimensions:\
>$$\frac{\partial^2 u}{\partial t^2} = c^2(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2})$$\
Where `c` is a user defined field. This allows for fast simulations of waves passing through different mediums.

The second file, waveTest.py, is an example of the simulation being used and displayed. It contains four different parts:
  1. Defining the wave propagation field (c^2 in the equation above). This field could represent any zone where wave speed slows down or speeds up. One example is light passing through glass.
  2. Initialization of the propagation field, simulation, and visualization tools.
  3. Iteration of the simulation and saving specified frames for visualization later.
  4. Displaying the saved simulation frames in an animation.

Boundary conditions for three edges are set to be perfectly reflective. The fourth (top) edge is set to create a wave and then become reflective. These conditions can be modified in the iterate() function in the waveEquation.py file. A future update is planned to make the boundary conditions part of the initialization of the simulation. This will allow for more general use of the simulation without needing to modify the simulation's core.
