import numpy as np
import time
#creo 2 array (uno sono le x e uno le y) ciascuno ha N righe (N punti) per N_runs colonne
#li sommo termine a termine e conto gli hit (contare nella direzione dei runs è invariante, sono tutti random uguali)
N = 100000
N_run = 100

start_time=time.time()

pi = 4*np.sum(np.where(pow(np.random.rand(N,N_run),2)+pow(np.random.rand(N,N_run),2)<1,1,0))/(N*N_run)

run_time = time.time()

print('pi with ', N_run, "runs for ", N, "tosses each is: ",pi, "in ",run_time-start_time,"sec." )
print("Precision computation : ", np.abs(pi-np.pi))
