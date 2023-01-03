# Utilisation de la bibliothèque SciPy pour stocker et manipuler une matrice de raideur sparse dans un problème de dynamique des structures à 3 DOF

import numpy as np
from scipy import sparse

# Constants
dt = 0.01  # Time step
T = 10  # Total simulation time
beta = 1/4  # Newmark coefficient
gamma = 1/2  # Newmark coefficient

# Mass, damping and stiffness matrices
M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
C = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
K = sparse.csc_matrix(([1, 1, 1], ([0, 1, 2], [0, 1, 2])), shape=(3, 3))

# Initial conditions
u0 = np.array([0, 0, 0])  # Displacements
v0 = np.array([0, 0, 0])  # Velocities
a0 = np.array([0, 0, 0])  # Accelerations

# External forces
f = np.array([0, 0, 0])

# Initialize arrays for storing results
time = np.zeros(int(T/dt)+1)
u = np.zeros((int(T/dt)+1, 3))
v = np.zeros((int(T/dt)+1, 3))
a = np.zeros((int(T/dt)+1, 3))

# Set initial conditions
u[0] = u0
v[0] = v0
a[0] = a0

# Loop over time steps
for i in range(int(T/dt)):
    # Predictor step
    u_pred = u[i] + dt * v[i] + (dt**2) * (1-2*beta) * a[i]
    v_pred = v[i] + dt * (1-gamma) * a[i]
    a_pred = np.linalg.solve(M, f - C.dot(v_pred) - K.dot(u_pred))
    
    # Corrector step
    u[i+1] = u[i] + dt * (v[i] + v_pred) / 2
    v[i+1] = v[i] + dt * (a[i] + a_pred) / 2
    a[i+1] = a_pred
    
    # Store time and update time step
    time[i+1] = time[i] + dt

# Print results
print("Displacements: ", u)
print("Velocities: ", v)
print("Accelerations: ", a)
