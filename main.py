import numpy as np

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
    u_rk = np.zeros
