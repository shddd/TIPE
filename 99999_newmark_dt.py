import numpy as np
import matplotlib.pyplot as plt
import scipy as sy
import scipy.fftpack as syfp

uInitial=0     #CI
udInitial=1    

#paramètres
omega=5         #pulsation
m=1000000       #masse
t=np.array([0.1,0.5,1,5])      # tableau des dt
dT=np.zeros(int(np.shape(t)[0]))
tArray=np.zeros(int(np.shape(t)[0]))
gamma=0.25   # paramètre
beta=0.5
fig,ax=plt.subplots(int(np.shape(t)[0]),1)

for j in range(0,len(t)) :
    N=t[j]         #intervalle d'intégration
    T=2*np.pi/omega # Période
    multiple=100
    drange=np.arange(0,multiple*T,N) 
    umax=pow(pow(uInitial,2)+pow(udInitial/omega,2),0.5)
    uExact=umax*np.sin(omega*drange)    # solution exacte

    
    # initialisation
    u=np.zeros(drange.size)
    ud=np.zeros(drange.size)
    udd=np.zeros(drange.size)
    
    # Méthode de Newmark
    u[0]=uInitial
    ud[0]=udInitial
    for i in range(0,drange.size-1):
        C1=u[i]+N*ud[i]+0.5*np.power(N,2)*(1-2*beta)*udd[i]
        C2=ud[i]+N*(1-gamma)*udd[i]
        
        udd[i+1]=-np.power(omega,2)*C1/(1+beta*np.power(omega,2)*np.power(N,2))
        ud[i+1]=ud[i]+N*((1-gamma)*udd[i]+gamma*udd[i+1])
        u[i+1]=u[i]+N*ud[i]+0.5*np.power(N,2)*((1-2*beta)*udd[i]+2*beta*udd[i+1])
        
    #afficher la solution numérique
    #ax[j].plot(drange,u,linestyle='solid') 
    #ax[j].title.set_text(r'$\Delta t=$'+str(N))
    
    ax[j].plot(drange,(uExact-u),linestyle='solid') 
    ax[j].title.set_text(r'Différence ' r'$\Delta t=$'+str(N))

    
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
fig.text(0.5, 0.02, 'Période d\'intégration', ha='center')
