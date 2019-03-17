import numpy as np
import time

N_run= 100
N = 100000 # number of MC events
start_time = time.time()

punti = np.array([np.random.rand(2) for i in range(N)])
array_products = np.array([np.dot(punti[i],punti[i]) for i in range(len(punti))])
pi = np.array([4*len(array_products[array_products<1])/N for j in range(N_run)])
pi_mean = np.mean(pi)
run_time = time.time()

print('pi with ', N_run, "runs for ", N, "tosses each is: ",pi_mean, "in ",run_time-start_time,"sec." )
print("Precision computation : ", np.abs(pi_mean-np.pi))
