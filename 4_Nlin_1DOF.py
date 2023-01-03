#Résolution d'un problème de dynamique des structures non linéaire à 1 DOF avec la méthode de Newmark 
#un modèle constitutif non linéaire pour la matrice de raideur :

import numpy as np

# Constants
dt = 0.01  # Time step
T = 10  # Total simulation time
beta = 1/4  # Newmark coefficient
gamma = 1/2  # Newmark coefficient

# Mass and damping matrices
M = np.array([[1]])
C = np.array([[1]])

# Initial conditions
u0 = np.array([0])  # Displacements
v0 = np.array([0])  # Velocities
a0 = np.array([0])  # Accelerations

# External forces
f = np.array([0])

# Initialize arrays for storing results
time = np.zeros(int(T/dt)+1)
u = np.zeros((int(T/dt)+1, 1))
v = np.zeros((int(T/dt)+1, 1))
a = np.zeros((int(T/dt)+1, 1))

# Set initial conditions
u[0] = u0
v[0] = v0
a[0] = a0

# Loop over time steps
for i in range(int(T/dt)):
    # Predictor step
    u_pred = u[i] + dt * v[i] + (dt**2)
 # Compute nonlinear stiffness matrix
    K = np.array([[np.sin(u_pred)]])
    
    # Corrector step
    u[i+1] = u[i] + dt * (v[i] + v_pred) / 2
    v[i+1] = v[i] + dt * (a[i] + a_pred) / 2
    a[i+1] = np.linalg.solve(M, f - C.dot(v[i+1]) - K.dot(u[i+1]))
    
    # Store time and update time step
    time[i+1] = time[i] + dt

# Print results
print("Displacements: ", u)
print("Velocities: ", v)
print("Accelerations: ", a)
