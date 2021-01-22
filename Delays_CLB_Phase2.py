#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:42:02 2020

@author: francescobenfenati
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fig_1, axs_1 = plt.subplots(2,2)  #divide the canvas in subplots
fig_2, axs_2 = plt.subplots(2,2)

CLBs = [2,3,4,5,7,8,9,10]

df_1_collection = [] #create array of DataFrames, one DF (1 row) per each CLB

column = ['CLB','Mean','Max','Min','Var','Sigma','Measures']

axs_1 = axs_1.ravel() #need to do this to make it a np.array? not a ndarray..!
axs_2 = axs_2.ravel() #need to do this to make it a np.array? not a ndarray..!

colors = ['blue','red','green','navy']

fig_1.suptitle('CLB Delays')
fig_2.suptitle('CLB Delays')

for i in range(2,11):
    
    arr = [] 
    
    
    if i == 6:
        continue

    with open(f"/Users/francescobenfenati/BCI_Oscilloscope_old/MeasurementCLB{i}.Wfm.csv") as f:
        for line in f:
            arr.append(float(line))
            
    x = np.array(arr)
   
#------------------------------- Statistics ----------------------------------#
    
    #Mean value
    mean = np.mean(x)

    #MAX value
    xmax = np.amax(x)

    #MIN value
    xmin = np.amin(x)

    #Variance
    var = np.var(x)

    #Standard deviation
    sigma = np.std(x)
      
    #Mean error
    #mean_error = sigma/np.sqrt(len(x)))
    
    #create array of statistics for the current iesima-CLB
    stat_i = [i,mean,xmax,xmin,var,sigma,len(x)]

    if i in range(2,6):
        
        #add DataFrame of the current CLB to the DF array
        df_1_collection.append(pd.DataFrame([stat_i], columns =column))
       
        #empty the statistics array for next iteration 
        stat_i.clear()
    
        #create histogram
        x_entries, bins, _ = axs_1[i-2].hist(x, bins = np.linspace(np.amin(x),
                    np.amax(x),50),density=0, alpha=0.5, color=colors[i-2] )

        axs_1[i-2].set_xlabel('seconds')
        axs_1[i-2].set_ylabel('entries')
        axs_1[i-2].set_title(f'CLB {i}')

    if i in range(7,11):
             
       df_1_collection.append(pd.DataFrame([stat_i],columns=column))
       
       stat_i.clear()

       x_entries, bins, _ = axs_2[i-7].hist(x, bins = np.linspace(np.amin(x),
                    np.amax(x),50),density=0, alpha=0.5, color=colors[i-7] )

       axs_2[i-7].set_xlabel('seconds')
       axs_2[i-7].set_ylabel('entries')
       axs_2[i-7].set_title(f'CLB {i}')
    
#----------------------------- Create Histogram ------------------------------#


fig_1.tight_layout() #makes canvas look tight
fig_2.tight_layout() #makes canvas look tight

#concatenate the CLBs DF into one single table
df_1 = pd.concat([df_1_collection[i] for i in range(len(df_1_collection))])

#save DF to csv file
df_1.to_csv('/Users/francescobenfenati/CLBdelays.csv',index=0)
