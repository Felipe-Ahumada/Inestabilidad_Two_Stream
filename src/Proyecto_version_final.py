import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
from matplotlib.animation import FuncAnimation 
plt.style.use('bmh')



L = 50 #longitud de la línea, L no puede ser m'as pequeño que Dx
Dx = 0.125 #largo de cada intervalo, por tanto L / Dx casillas
Np = 40000 #número de cargas
Nc = int(L / Dx) #número de celdas
A = 0.1 # amplitud de perturbacion de velocidad

#genera una posición (es necesaria multiplicarla por L) aleatoria de cada partícula
x = np.random.rand(Np) * L
v = np.random.randn(Np) + 3
#x0.sort() #para ordenar la lista

v[Np//2:] *= -1 #Esto divide la corriente en 2

v *= (1 + A*np.sin(2*np.pi*x/L)) # Esto es una función sinusoidal agregada, para que
#la corriente
linea = np.zeros(len(x))


#------------------------------------------------------------------------------------------------

#Condiguración del tiempo
tmax = 100.0

h = 1.0

t = np.arange(0, tmax, h) 

def cond_borde(x, L):
    for i in range(len(x)):
        #así se soluciona el problema de que estén afuera de la línea
        if x[i] > L:
            x[i] -= L #si se sale por L, entonces aparece en 0
            
        if x[i] < 0:            
            x[i] += L #si se sale por 0, entonces aparece en L
            
def n(x, Dx, Nc):
    
    n0 = np.floor(x / Dx).astype(int)
    
    rho = np.zeros(Nc) # densidad de cargas por celda

    #aquí contamos cuántos electrones hay en cada celda
    #for s in range(Np):
    #    rho[int(n0[s])] += 1
     
    for s in n0:
        rho[s] += 1
        
    return 1 - rho * ( Nc / len(x) ) #Nc cantidad de celdas, len(x) = Np; con esto se normaliza la densidad

def E(rho, Dx):
    
    e = Dx * np.cumsum(rho)
    
    return e - np.mean(e) #Este es el campo menos su promedio, porque?

#Particle pusher, basicamente empuja las partículas
def push(x, v, Et, Dt, Dx):
    
    c = np.floor(x / Dx).astype(int)
    
    v = v - Dt * Et[c]
    
    #print(c)
    
    
    x = x + Dt * v
    
    return x, v

#------------------------------------------------------------------------------------------------

xx = np.empty((t.size, Np))
vv = np.empty((t.size, Np))

#------------------------------------------------------------------------------------------------

for tau in trange(t.size):
        
    #Condiciones iniciales
    cond_borde(x, L)
    
    RHO = n(x, Dx, Nc)
    
    #array del campo electrico
    Et = E(RHO, Dx)
    
    #guarda las nuevas posiciones y velocidades
    xx[tau] = x
    vv[tau] = v
    
    #actualiza las posiciones y velocidades
    x, v = push(x, v, Et, h, Dx)
                
    
#animación
fig = plt.figure() 
# marking the x-axis and y-axis
axis = plt.axes(xlim =(0,L), 
                ylim =(-6, 6)) 
  
# initializing a line variable
line, = axis.plot([],[], lw = 3) 

def init(): 
    line.set_data([],[])
    return line,

def animate(i):
    plt.hist2d(xx[i], vv[i], bins=100)
    plt.xlabel('x')
    plt.ylabel('v')
    plt.title('Inestabilidad two-stream')
    return line,

anim = FuncAnimation(fig, animate, init_func = init,
                     frames = 100, interval = 20, blit = True)
  
   
anim.save('two_stream_instability.gif', 
          writer = 'ffmpeg', fps = 30)