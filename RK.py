import numpy as np

def runge_kutta_method(M, C, K, F, u0, v0, dt, n_steps):
    u = np.zeros(n_steps+1)
    v = np.zeros(n_steps+1)
    u[0] = u0
    v[0] = v0
    for i in range(1, n_steps+1):
        k1 = dt*v[i-1]
        l1 = dt*(-np.dot(K,u[i-1])-np.dot(C,v[i-1])+F)/M
        k2 = dt*(v[i-1]+l1/2)
        l2 = dt*(-np.dot(K,(u[i-1]+k1/2))-np.dot(C,(v[i-1]+l1/2))+F)/M
        k3 = dt*(v[i-1]+l2/2)
        l3 = dt*(-np.dot(K,(u[i-1]+k2/2))-np.dot(C,(v[i-1]+l2/2))+F)/M
        k4 = dt*(v[i-1]+l3)
        l4 = dt*(-np.dot(K,(u[i-1]+k3))-np.dot(C,(v[i-1]+l3))+F)/M

        v[i] = v[i-1] + (1/6)*(l1 + 2*l2 + 2*l3 + l4)
        u[i] = u[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return v, u
