import numpy as np

def newmark_method(M, C, K, F, u0, v0, dt, n_steps, beta, gamma):
    a0 = F/M
    u = np.zeros(n_steps+1)
    v = np.zeros(n_steps+1)
    a = np.zeros(n_steps+1)
    u[0] = u0
    v[0] = v0
    a[0] = a0
    for i in range(1, n_steps+1):
        a_i = (F - C*v[i-1] - K*u[i-1])/M
        v_i = v[i-1] + (1-gamma)*dt*a[i-1] + gamma*dt*a_i
        u_i = u[i-1] + dt*v[i-1] + (dt**2)*(0.5-beta)*a[i-1] + (dt**2)*beta*a_i
        a[i] = a_i
        v[i] = v_i
        u[i] = u_i
    return a, v, u
