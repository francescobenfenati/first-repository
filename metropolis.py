import numpy as np
import time
N_run= 100
N = 100000 # number of MC events
pi = np.zeros(N_run)
start_time = time.time()

for j in range(N_run):
    
    a = pow( np.array([np.random.rand(N),np.random.rand(N)]),2)
    pi[j]+=4*(np.sum(np.where(a[0]+a[1]<1,1,0)))/N

pi_mean = np.mean(pi)
run_time = time.time()

print('pi with ', N_run, "runs for ", N, "tosses each is: ",pi_mean, "in ",run_time-start_time,"sec." )
print("Precision computation : ", np.abs(pi_mean-np.pi))
