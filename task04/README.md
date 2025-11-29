# Research Report
## Particle Swarm Optimization (PSO)

### Technical Summary
Abstract: This report details a manual simulation of the Particle Swarm Optimization (PSO) algorithm. It visualizes the movement of particles within a 2D search space aiming to converge on a target (global optimum). The study analyzes the velocity update vectors, breaking down the influence of Inertia, the Cognitive Component (pBest), and the Social Component (gBest). The simulation highlights how swarm intelligence emerges from the interaction between individual agents and collective memory.

**Key Concepts**: Swarm Intelligence, Velocity Vectors, Inertia, Personal Best (pBest), Global Best (gBest).

## Particle Swarm Optimization (PSO) Simulation: 2D Search Dynamics
**Task Description**: Simulate the movement of a swarm of particles in a 2D search space to find a global optimum (target), demonstrating the principles of Swarm Intelligence.

### Technical Requirements:

1. Environment Setup:

    - Define a 2D grid representing the Search Space.

    - Mark a specific point as the Global Optimum (Target).

    - Initialize 3 particles (A, B, C) at random positions.

2. Velocity Update Simulation:

    - For the first iteration, calculate and visualize the velocity vectors based on the standard PSO equation:

        - Inertia Component ($w$): The tendency to maintain current direction.

        - Cognitive Component ($pBest$): The attraction towards the particle's own best known position.

        - Social Component ($gBest$): The attraction towards the swarm's best known position (the target).

3. Position Update:

    - Update the position of the particles based on the resultant velocity vector.

4. Report Deliverables:

    - Visual Grid: A diagram showing the particles, the target, and the vector components (arrows).

    - Vector Analysis: An explanation of how Inertia, Cognitive, and Social factors influenced the new position of the particles.