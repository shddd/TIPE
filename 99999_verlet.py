import numpy as np

def verlet_method(M, F, u0, v0, dt, n_steps):
    u = np.zeros(n_steps+1)
    v = np.zeros(n_steps+1)
    a = np.zeros(n_steps+1)
    u[0] = u0
    v[0] = v0
    a[0] = F/M
    for i in range(1, n_steps):
        u[i] = 2*u[i-1] - u[i-2] + a[i-1]*(dt**2)
        v[i] = (u[i]-u[i-2])/(2*dt)
        a[i] = (u[i]-2*u[i-1]+u[i-2])/(dt**2)
    return a, v, u


import matplotlib.pyplot as plt

beta_values = np.linspace(0, 1, 50)
gamma_values = np.linspace(0, 1, 50)

for beta in beta_values:
    for gamma in gamma_values:
        _, _, u = newmark_method(M, C, K, F, u0, v0, dt, n_steps, beta, gamma)
        plt.plot(u, label='beta={:.2f}, gamma={:.2f}'.format(beta, gamma))

plt.title("Position en fonction de beta et gamma")
plt.legend()
plt.show()
