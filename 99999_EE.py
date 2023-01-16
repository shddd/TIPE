import numpy as np

def explicit_euler_method(M, C, K, F, u0, v0, dt, n_steps):
    u = np.zeros(n_steps+1)
    v = np.zeros(n_steps+1)
    u[0] = u0
    v[0] = v0
    for i in range(1, n_steps+1):
        a = (F - C*v[i-1] - K*u[i-1])/M
        v[i] = v[i-1] + dt*a
        u[i] = u[i-1] + dt*v[i-1]
    return v, u
