La méthode de Newmark peut être étendue à des systèmes à plusieurs degrés de liberté (DOF) en utilisant des matrices de masse, de raideur et de damping.

Pour résoudre un problème de dynamique des structures à plusieurs DOF avec la méthode de Newmark, il faut d'abord écrire les équations de mouvement du système sous forme matricielle. Ces équations sont données par :

M * a + C * v + K * u = f

où M est la matrice de masse, a est le vecteur des accélérations, C est la matrice de damping, v est le vecteur des vitesses, K est la matrice de raideur et u est le vecteur des déplacements. f est le vecteur des forces appliquées sur le système.

Pour résoudre ce système d'équations à chaque pas de temps, on peut utiliser la méthode de Newmark avec des combinaisons linéaires des valeurs de u, v et a aux pas de temps précédents pour prédire les valeurs aux pas de temps suivants.

Voici un exemple de code Python qui illustre comment résoudre un problème de dynamique des structures à 2 DOF avec la méthode de Newmark :

```python
import numpy as np

# Constants
dt = 0.01  # Time step
T = 10  # Total simulation time
beta = 1/4  # Newmark coefficient
gamma = 1/2  # Newmark coefficient

# Mass, damping and stiffness matrices
M = np.array([[1, 0], [0, 1]])
C = np.array([[1, 0], [0, 1]])
K = np.array([[1, 0], [0, 1]])

# Initial conditions
u0 = np.array([0, 0])  # Displacements
v0 = np.array([0, 0])  # Velocities
a0 = np.array([0, 0])  # Accelerations

# External forces
f = np.array([0, 0])

# Initialize arrays for storing results
time = np.zeros(int(T/dt)+1)
u = np.zeros((int(T/dt)+1, 2))
v = np.zeros((int(T/dt)+1,2))
a = np.zeros((int(T/dt)+1, 2))

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

#Print results
print("Displacements: ", u)
print("Velocities: ", v)
print("Accelerations: ", a)

```
