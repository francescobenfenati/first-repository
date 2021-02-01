#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:42:02 2020

@author: francescobenfenati
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def fit_function(x,B,a,b):
    return (B * np.exp(-((x-a)**2)/(2*b**2)))

#Reduced CHI square: takes observed val.,expected val.,constraints array-like
#chi square on a non-normalized hist. different after normalization??
def chi_square(obs,exp,constr):
    diff = [(obs[i] - exp[i])**2/exp[i] for i in range(1,len(obs))]
    dof = (len(obs)-len(constr))
    return sum(diff)/dof


fig, axs = plt.subplots(1,1)

CLB = '6-3'

fig.suptitle('CLB Delays')

#Read data as DataFrame with column named "values"
data = pd.read_csv(f"/Users/francescobenfenati/Phase2_Oscilloscope/Measurement_Clb{CLB}.Wfm.csv",names=['values'])
    
column = ['CLB','Mean','Max','Min','Var','Sigma','Measures','Fit mean','Fit sigma','Reduced chi^2']
x= np.array(data['values']*1e10)  


x_entries, binning, _ = axs.hist(x, bins=1000, density=0, alpha=0.5 )

#find bin centres
binscentres = np.array([0.5 * (binning[i] + binning[i+1]) 
                                for i in range(len(binning)-1)])
#curve fit
popt, _ = curve_fit(fit_function, binscentres, x_entries)

# summarize the parameter values
B, a, b = popt

# Generate enough x values to make the curves look smooth.
fit2_bins = np.linspace(np.amin(x), np.amax(x), 1000)

#expected events from fit curve
expected_events = fit_function(binscentres, *popt)

#Plot the fitted function.
#axs.plot(fit2_bins,fit_function(fit2_bins, *popt), color='red', linewidth=2.5,
#                                              label=r'Fitted function')

chi = chi_square(x_entries,expected_events,popt)
#print('reduced chi value =',chi,'\n')
#print(chisquare(f_obs=x_entries, f_exp=expected_events,ddof=len(x_entries)-2))

#Make the plot nicer.
axs.set_xlabel('time [$10^{-10}$ s]',fontsize=13)
axs.set_ylabel('Entries',fontsize=13)
axs.set_title(f'CLB {CLB}',fontsize=14)

#round with 2 decimals and get back to the 1e-10 array to put it in the df
stat = [x[i]*1e-10 for i in range(len(x))] 
statx = np.array(stat)

#------------------------------- Statistics ----------------------------------#
#Mean value
mean = np.mean(statx)
    
#MAX value
xmax = np.amax(statx)

#MIN value
xmin = np.amin(statx)

#Variance
var = np.var(statx)

#Standard deviation
sigma = np.std(statx)

#Mean error
#mean_error = sigma/np.sqrt(len(x)))

df = pd.DataFrame([[f'{CLB}',mean,xmax,xmin,var,sigma,len(x),a*1e-10,b*1e-10,chi]],columns=column)


