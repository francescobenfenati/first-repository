#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:17:47 2020

@author: francescobenfenati
"""

#provaaaaaa
#%matplotlib qt5

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm, chisquare
from scipy.optimize import curve_fit

fig, axs = plt.subplots(3,3)
fig2, axs2 = plt.subplots(3,3)
axs = axs.ravel()
axs2 = axs2.ravel()

clbs = [0,2,3,4,5,6,7,8,9,10,12]
df_collection = []

def fit_function(x,B,a,b):
    return (B * np.exp(-((x-a)**2)/(2*b**2)))

#Reduced CHI square: takes observed val.,expected val.,constraints array-like
#chi square on a non-normalized hist. different after normalization??
def chi_square(obs,exp,constr):
    diff = [(obs[i] - exp[i])**2/exp[i] for i in range(1,len(obs))]
    dof = (len(obs)-len(constr))
    return sum(diff)/dof
    
for i in clbs:
    
#Read data as DataFrame with column named "values"
    data = pd.read_csv(f"/Users/francescobenfenati/Phase2_Oscilloscope/Measurement_Clb{i}.Wfm.csv",names=['values'])
    
    column = ['CLB','Mean','Max','Min','Var','Sigma','Measures','Fit mean','Fit sigma','Reduced chi^2']

#need to multiply by 1e10 otherwise values are too low for fitting...     
    x= np.array(data['values']*1e10)     
    if i == 6:
        x = np.delete(x,np.where(x==np.amin(x)))
#x = np.array(arr)

#----------------------------- 2nd Fit Method --------------------------------#
#DOES NOT WORK WITH A NON-NORMALIZED HIST. -> ONE MUST FIT ALSO PARAM. B 
#def fit_function(x,a,b):
 #   return (1/(b*(np.sqrt(2*np.pi)))) * np.exp(-((x-a)**2)/(2*b**2))

    if i<10:
        x_entries, binning, _ = axs[clbs.index(i)].hist(x, bins=30, density=0, alpha=0.5 )

        #find bin centres
        binscentres = np.array([0.5 * (binning[i] + binning[i+1]) 
                                for i in range(len(binning)-1)])
        # curve fit
        popt, _ = curve_fit(fit_function, binscentres, x_entries)

        # summarize the parameter values
        B, a, b = popt
        #print('B= ',B)
        #print('\nmean =',a,'1e-10 s\n')
        # rint('sigma =',b,'1e-10 s\n')

        # Generate enough x values to make the curves look smooth.
        fit2_bins = np.linspace(np.amin(x), np.amax(x), 1000)

        #expected events from fit curve
        expected_events = fit_function(binscentres, *popt)

        #Plot the fitted function.
        axs[clbs.index(i)].plot(fit2_bins,fit_function(fit2_bins, *popt), color='red', linewidth=2.5,
                                                label=r'Fitted function')

        chi = chi_square(x_entries,expected_events,popt)
        #print('reduced chi value =',chi,'\n')
        #print(chisquare(f_obs=x_entries, f_exp=expected_events,ddof=len(x_entries)-2))

        #Make the plot nicer.
        axs[clbs.index(i)].set_xlabel('time [$10^{-10}$ s]')
        axs[clbs.index(i)].set_ylabel('Entries')
        axs[clbs.index(i)].set_title(f'CLB {i}')
        #axs[clbs.index(i)].legend()
        #axs[i].show()
        fig.tight_layout()

        #round with 2 decimals and get back to the 1e-10 array to put it in the df
        stat = [x[i]*1e-10 for i in range(len(x))] 
        statx = np.array(stat)
        #plt.xlabel('seconds x e-10')
        #plt.ylabel('f(x)')
        #plt.title('Delays')

    else:
        x_entries, binning, _ = axs2[clbs.index(i)-9].hist(x, bins=30, density=0, alpha=0.5 )
       
        binscentres = np.array([0.5 * (binning[i] + binning[i+1]) 
                                for i in range(len(binning)-1)])
        
        popt, _ = curve_fit(fit_function, binscentres, x_entries)

        B, a, b = popt
        #print('B= ',B)
        #print('\nmean =',a,'1e-10 s\n')
        #print('sigma =',b,'1e-10 s\n')

        fit2_bins = np.linspace(np.amin(x), np.amax(x), 1000)
        expected_events = fit_function(binscentres, *popt)
        axs2[clbs.index(i)-9].plot(fit2_bins,fit_function(fit2_bins, *popt), color='red', linewidth=2.5,
                                                label=r'Fitted function')
        chi = chi_square(x_entries,expected_events,popt)
        #print('reduced chi value =',chi,'\n')
        #print(chisquare(f_obs=x_entries, f_exp=expected_events,ddof=len(x_entries)-2))
        
        axs2[clbs.index(i)-9].set_xlabel('time [$10^{-10}$ s]')
        axs2[clbs.index(i)-9].set_ylabel('Entries')
        axs2[clbs.index(i)-9].set_title(f'CLB {i}')
        fig2.tight_layout()

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

#create array of statistics for the current iesima-CLB
    stat_i = [f'{i}',mean,xmax,xmin,var,sigma,len(x),a*1e-10,b*1e-10,chi]

#add DataFrame of the current CLB to the array of dataframes
    df_collection.append(pd.DataFrame([stat_i], columns =column))



#concatenate the CLBs DF into one single table
df_1 = pd.concat(df_collection[i] for i in range(len(clbs)))

#save DF to csv file
df_1.to_csv('/Users/francescobenfenati/CLBdelays.csv',index=0)
#------------------------------- 1st Fit Method ------------------------------#
'''
#ONLY FOR A NORMALIZED HIST.
#add a 'best fit' line
mu, sigma = norm.fit(x)


fit_bins = np.linspace(xmin,xmax,100)

fit_func = norm.pdf(fit_bins, mu, sigma)

plt.plot(fit_bins, fit_func)

print('mu =',mu, '1e-10 s')
print('sigma =',sigma,'1e-10 s')
'''
