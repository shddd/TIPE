import numpy as np

def verlet_method(M, F, u0, v0, dt, n_steps):
    u = np.zeros(n_steps+1)
    v = np.zeros(n_steps+1)
    u[0] = u0
    v[0] = v0
    a = (F/M)
    for i in range(1, n_steps+1):
        u[i] = 2*u[i-1] - u[i-2] + a*(dt**2)
        v[i] = (u[i]-u[i-2])/(2*dt)
    return v, u
