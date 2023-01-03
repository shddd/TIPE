import numpy as np
import matplotlib.pyplot as plt

def newmark_method(M, C, K, F, u0, v0, dt, n_steps):
    # Initialize arrays to store the solutions
    u_newmark = np.zeros(n_steps+1)
    v_newmark = np.zeros(n_steps+1)
    a_newmark = np.zeros(n_steps+1)
    u_newmark[0] = u0
    v_newmark[0] = v0
    a_newmark[0] = (F[0] - C.dot(v0) - K.dot(u0)) / M
    # Loop over the time steps
    for i in range(1, n_steps+1):
        u_newmark[i] = u_newmark[i-1] + dt*v_newmark[i-1] + (dt**2/2)*(1-2*beta)*a_newmark[i-1]
        v_newmark[i] = v_newmark[i-1] + dt*((1-gamma)*a_newmark[i-1] + gamma*a_newmark[i])
        a_newmark[i] = (F[i] - C.dot(v_newmark[i]) - K.dot(u_newmark[i])) / M
    return u_newmark, v_newmark, a_newmark

def runge_kutta_method(M, C, K, F, u0, v0, dt, n_steps):
    # Initialize arrays to store the solutions
    u_rk[0] = u0
    v_rk[0] = v0
    a_rk[0] = (F[0] - C.dot(v0) - K.dot(u0)) / M
    # Loop over the time steps
    for i in range(1, n_steps+1):
        k1 = dt*v_rk[i-1]
        l1 = dt*a_rk[i-1]
        k2 = dt*(v_rk[i-1] + l1/2)
        l2 = dt*(a_rk[i-1] + (F[i] - C.dot(v_rk[i-1] + l1/2) - K.dot(u_rk[i-1] + k1/2)) / M)
        k3 = dt*(v_rk[i-1] + l2/2)
        l3 = dt*(a_rk[i-1] + (F[i] - C.dot(v_rk[i-1] + l2/2) - K.dot(u_rk[i-1] + k2/2)) / M)
        k4 = dt*(v_rk[i-1] + l3)
        l4 = dt*(a_rk[i-1] + (F[i] - C.dot(v_rk[i-1] + l3) - K.dot(u_rk[i-1] + k3)) / M)
        u_rk[i] = u_rk[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        v_rk[i] = v_rk[i-1] + (l1 + 2*l2 + 2*l3 + l4) / 6
        a_rk[i] = (F[i] - C.dot(v_rk[i]) - K.dot(u_rk[i])) / M
    return u_rk, v_rk, a_rk

def explicit_euler_method(M, C, K, F, u0, v0, dt, n_steps):
    # Initialize arrays to store the solutions
    u_ee = np.zeros(n_steps+1)
    v_ee = np.zeros(n_steps+1)
    a_ee = np.zeros(n_steps+1)
    u_ee[0] = u0
    v_ee[0] = v0
    a_ee[0] = (F[0] - C.dot(v0) - K.dot(u0)) / M
    # Loop over the time steps
    for i in range(1, n_steps+1):
        v_ee[i] = v_ee[i-1] + dt*a_ee[i-1]
        u_ee[i] = u_ee[i-1] + dt*v_ee[i]
        a_ee[i] = (F[i] - C.dot(v_ee[i]) - K.dot(u_ee[i])) / M
    return u_ee, v_ee, a_ee

def verlet_method(M, C, K, F, u0, v0, dt, n_steps):
    # Initialize arrays to store the solutions
    u_verlet = np.zeros(n_steps+1)
    v_verlet = np.zeros(n_steps+1)
    a_verlet = np.zeros(n_steps+1)
    u_verlet[0] = u0
    v_verlet[0] = v0
    a_verlet[0] = (F[0] - C.dot(v0) - K.dot(u0)) / M
    # Loop over the time steps
    for i in range(1, n_steps+1):
        u_verlet[i] = 2*u_verlet[i-1] - u_verlet[i-2] + dt**2*a_verlet[i]
        v_verlet[i] = (u_verlet[i] - u_verlet[i-2]) / (2*dt)
        a_verlet[i] = (F[i] - C.dot(v_verlet[i]) - K.dot(u_verlet[i])) / M
    return u_verlet, v_verlet, a_verlet

#Define the mass, damping, and stiffness matrices
M = np.array([[2, 0], [0, 1]])
C = np.array([[0, 0], [0, 0]])
K = np.array([[1, -1], [-1, 2]])

#Define the load vector and the initial displacement and velocity
F = np.zeros((2, n_steps+1))
F[0, :] = 1
u0 = np.array([0, 0])
v0 = np.array([0, 0])

#Set the time step and the number of time steps
dt = 0.1
n_steps = 10

#Set the Newmark method parameters
beta = 1/4
gamma = 1/2

#Solve the problem using the Newmark method
u_newmark, v_newmark, a_newmark = newmark_method(M, C, K, F, u0, v0, dt, n_steps)

#Solve the problem using the Runge-Kutta method
u_rk, v_rk, a_rk = runge_kutta_method(M, C, K, F, u0, v0, dt, n_steps)

# Solve the problem using the explicit Euler method
u_ee, v_ee, a_ee = explicit_euler_method(M, C, K, F, u0, v0, dt, n_steps)

# Solve the problem using the Verlet method
u_verlet, v_verlet, a_verlet = verlet_method(M, C, K, F, u0, v0, dt, n_steps)

#Compare the solutions
print("Displacement (Newmark):", u_newmark)
print("Displacement (Runge-Kutta):", u_rk)
print("Displacement (Explicit Euler):", u_ee)
print("Displacement (Verlet):", u_verlet) 

print("Velocity (Newmark):", v_newmark)
print("Velocity (Runge-Kutta):", v_rk)
print("Velocity (Explicit Euler):", v_ee)
print("Velocity (Verlet):", v_verlet)

print("Acceleration (Newmark):", a_newmark)
print("Acceleration (Runge-Kutta):", a_rk)
print("Acceleration (Explicit Euler):", a_ee)
print("Acceleration (Verlet):", a_verlet)

# Plot the solutions
plt.figure()
plt.plot(u_newmark[:, 0], label="Newmark (displacement)")
plt.plot(u_rk[:, 0], label="Runge-Kutta (displacement)")
plt.plot(u_ee[:, 0], label="Explicit Euler (displacement)")
plt.plot(u_verlet[:, 0], label="Verlet (displacement)")
plt.legend()
plt.xlabel("Time step")
plt.ylabel("Displacement")

plt.figure()
plt.plot(v_newmark[:, 0], label="Newmark (velocity)")
plt.plot(v_rk[:, 0], label="Runge-Kutta (velocity)")
plt.plot(v_ee[:, 0], label="Explicit Euler (velocity)")
plt.plot(v_verlet[:, 0], label="Verlet (velocity)")
plt.legend()
plt.xlabel("Time step")
plt.ylabel("Velocity")

plt.figure()
plt.plot(a_newmark[:, 0], label="Newmark (acceleration)")
plt.plot(a_rk[:, 0], label="Runge-Kutta (acceleration)")
plt.plot(a_ee[:, 0], label="Explicit Euler (acceleration)")
plt.plot(a_verlet[:, 0], label="Verlet (acceleration)")
plt.legend()
plt.xlabel("Time step")
plt.ylabel("Acceleration")

plt.show()
