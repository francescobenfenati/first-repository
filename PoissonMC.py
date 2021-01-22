
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:52:00 2021

@author: francescobenfenati
"""
%matplotlib qt5

'''
Generate events in a fixed time interval: the number of events for each timeline
will depend on the frequency
'''

import numpy as np
import random
import math
import statistics
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


_lambda = 5
_num_events = 100
_event_num = []
_event_num_2 = []
_event_num_3 = []
_inter_event_times = []
_inter_event_times_2 = []
_inter_event_times_3 = []

_event_time = 0
_event_times = []

_event_time_2 = 0
_event_times_2 = []

_event_time_3 = 0
_event_times_3 = []

'''
rate t_1 e t_2 = 10 kHz -> 10 hits/us
consider a timeframe of 1000 us ---> average of 10000 hits
rate t_3 = 100 Hz -> 0.1 hits/us ---> average of 100 hits in the timeframe
'''
#------------------------Generate Poissonian events---------------------------#

event = 0
while _event_time < 1e6:    #1e6 microseconds time interval
    _inter_event_time = np.random.exponential(100,1)
    if _event_time+_inter_event_time[0] < 1e6:
        _inter_event_times.append(_inter_event_time[0])
        _event_time = _event_time + _inter_event_time[0]
        _event_times.append(_event_time)
        _event_num.append(event)
        event +=1
    else:
        break
    
event2 = 0
while _event_time_2 < 1e6:  
    _inter_event_time_2 = np.random.exponential(100,1)
    if _event_time_2+_inter_event_time_2[0] > 1e6:
        break
    _inter_event_times_2.append(_inter_event_time_2[0])
    _event_time_2 = _event_time_2 + _inter_event_time_2[0]
    _event_times_2.append(_event_time_2)
    _event_num_2.append(event2)
    event2 +=1


event3 = 0
while _event_time_3 < 1e6:
    _inter_event_time_3 = np.random.exponential(10000,1) 
    if _event_time_3+_inter_event_time_3[0] > 1e6:
        break
    _inter_event_times_3.append(_inter_event_time_3[0])
    _event_time_3 = _event_time_3 + _inter_event_time_3[0]
    _event_times_3.append(_event_time_3)
    _event_num_3.append(event3)
    event3 +=1

#--------------------------Calculate Delta-t_i,j------------------------------#
'''
delayed_event = []
delayed_event_2 = []

Deltat = []
for i in range(event):
    for j in range(event2):
        Deltat.append(_event_times[i]-_event_times_2[j])

xmin=-0.01
xmax=0.01
        
fig = plt.figure()
x_entries, binning, _ = plt.hist(Deltat, bins=20, range=[xmin,xmax], density=0, alpha=0.5)
plt.xlabel('time ($\mu$s)')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t_{i,j}$')
plt.show()

#insert the spurious hits of t_3 in the two timelines t_1 and t_2

for i in (_event_times_3):
    delay = random.gauss(0, 0.002) #2 ns <--- 1 unit is 1 us
    delay_2 = random.gauss(0, 0.002) 
    delayed_event.append(i+delay)
    delayed_event_2.append(i+delay_2)
    _event_times.append(i+delay)
    _event_times_2.append(i+delay_2)
    _event_times.sort()
    _event_times_2.sort()
    event += 1
    event2 += 1

Deltat.clear()
#Deltat = []
for i in range(event):
    for j in range(event2):
        Deltat.append(_event_times[i]-_event_times_2[j])

fig = plt.figure()
x_entries, binning, _ = plt.hist(Deltat, bins=100, density=0, alpha=0.5)
plt.xlabel('time ($\mu$s)')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t_{i,j}$ with Gaussian delay')
plt.show()


fig = plt.figure()
x_entries, binning, _ = plt.hist(Deltat, bins=20, range=[xmin,xmax], density=0, alpha=0.5)
plt.xlabel('time ($\mu$s)')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t_{i,j}$ with Gaussian delay')
plt.show()

'''
#-----------------------Generate deterministic events-------------------------#

frequency = 0.005
delta = 0.002 #2 ns constant delay
deterministic_events = []
deterministic_events_2 = []
deterministic_event = 0
deterministic_event_2 = 0+delta
while deterministic_event < 1e6:
    deterministic_events.append(deterministic_event)
    deterministic_events_2.append(deterministic_event_2)
    deterministic_event += 200
    deterministic_event_2 += 200+delta

#------------------Plot histo of Delta t for determ.events--------------------#
Deltat = []
xmin=-0.01
xmax=0.01

for i in range(len(deterministic_events)):
    for j in range(len(deterministic_events_2)):
        Deltat.append(deterministic_events[i]-deterministic_events_2[j])

fig = plt.figure()
x_entries, binning, _ = plt.hist(Deltat, bins=100, density=0, alpha=0.5)
plt.xlabel('time ($\mu$s)')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t_{i,j}$ for deterministic events')
plt.show()

fig = plt.figure()
x_entries, binning, _ = plt.hist(Deltat, bins=20, range=[xmin,xmax], density=0, alpha=0.5)
plt.xlabel('time ($\mu$s)')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t_{i,j}$ for deterministic events')
plt.show()

'''
Generate a fixed number of events for the two timelines

_event_times = np.zeros(100)
_event_times_2 = np.zeros(100)


#-------------------Generate exponentially distributed dt---------------------#
#1/b exp(-x/b)
#lambda = 1/b 

_inter_event_times = np.random.exponential(0.2,100)
_inter_event_times_2 = np.random.exponential(0.2,100)

for i in range(_num_events):
    _event_num.append(i)
    _event_times[i] = _event_times[i-1]+_inter_event_times[i]
    _event_times_2[i] = _event_times_2[i-1]+_inter_event_times_2[i]

'''
#-------------------Generate dt with inverse CDF technique--------------------#
'''
Generate inter-event times via the inverse CDF technique -> exp distribution

_event_times = []
_event_times_2 = []
_event_time = 0
_event_time_2 = 0

for i in range(_num_events):
    _event_num.append(i)
    #Get a random probability value from the uniform distribution's PDF
    n = random.random()
    n2 = random.random()

	#Generate the inter-event time from the exponential distribution's CDF using the Inverse-CDF technique
    _inter_event_time = -math.log(1.0 - n) / _lambda
    _inter_event_times.append(_inter_event_time)

	#Add the inter-event time to the running sum to get the next absolute event time
    _event_time = _event_time + _inter_event_time
    _event_times.append(_event_time)

     #For 2nd timeline
    _inter_event_time_2 = -math.log(1.0 - n2) / _lambda
    _inter_event_times_2.append(_inter_event_time_2)
     
    _event_time_2 = _event_time_2 + _inter_event_time_2
    _event_times_2.append(_event_time_2)
'''

#-------------------------- Plot inter-event times----------------------------#
'''
fig = plt.figure()
fig.suptitle('Times between consecutive events in a simulated Poisson process')
plot, = plt.plot(_event_num, _inter_event_times, 'bo-', label='Inter-event time')
plt.legend(handles=[plot])
plt.grid(True)
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()
'''

#-------------------- Plot inter-event distribution + fit---------------------#
'''
fig = plt.figure()
x_entries, binning, _ = plt.hist(_inter_event_times, bins=20, density=0, alpha=0.5 )
plt.xlabel('Inter-event time')
plt.ylabel('Occurrence')
plt.suptitle('$\Delta t$ distribution')


#fit function
def exponential_function(x,a,b):
    return a*np.exp(-x*b)

   
#find bin centres
binscentres = np.array([0.5 * (binning[i] + binning[i+1]) 
                        for i in range(len(binning)-1)])
          
# curve fit
popt, _ = curve_fit(exponential_function, binscentres, x_entries)


# summarize the parameter values
l = popt[1]
print('\nlambda =',l)

# Generate enough x values to make the curves look smooth.
fit2_bins = np.linspace(min(_inter_event_times), max(_inter_event_times), 1000)

# Plot the fitted function.
plt.plot(fit2_bins, exponential_function(fit2_bins, *popt), color='red', linewidth=2.5,
                                                label=r'Fitted function')

plt.show()
#------------------------- Plot absolute event times -------------------------#

fig = plt.figure()
fig.suptitle('Absolute times of consecutive events in a simulated Poisson process')
plt.scatter(_event_num, _event_times, marker=".",s=20,label="event")
plt.legend(loc='best', labelspacing=2)
plt.grid(True)
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()

'''
#------------------------- Plot hit sequence in time -------------------------#
'''
sequence = [_event_times, _event_times_2, _event_times_3, delayed_event , delayed_event_2]
color = ['blue','orange','red','red','red']
label = ['t_1','t_2','t_3']


fig = plt.figure()
fig.suptitle("Event sequences in time")

# set different line properties for each set of positions
lineoffsets1 = np.array([10,2,6,10,2])
linelengths1 = [2,2,2,2,2]

plt.eventplot(sequence,colors = color,lineoffsets = lineoffsets1,linelengths=linelengths1)
plt.legend(loc='best', labelspacing=2)
plt.xlabel("Time")
ax = plt.gca()
ax.axes.yaxis.set_visible(False)
plt.legend(label,loc='upper left')
plt.show()
'''

sequence = [deterministic_events,deterministic_events_2]
color = ['navy','brown']
label = ['t_1','t_2']

fig = plt.figure()
fig.suptitle("Deterministic events")

lineoffsets1 = np.array([10,2])
linelengths1 = [2,2]

plt.eventplot(sequence,colors = color,lineoffsets = lineoffsets1,linelengths=linelengths1)
plt.legend(loc='best', labelspacing=2)
plt.xlabel("Time")
ax = plt.gca()
ax.axes.yaxis.set_visible(False)
plt.legend(label,loc='upper left')
plt.show()

#------------------------ Plot # events in each interval ---------------------#
'''
Calculate and plot the number of event in each time interval (unit time)
'''
'''
_interval_nums = []
_num_events_in_interval = []
_interval_num = 1
_num_events = 0


for i in range(len(_event_times)):
	_event_time = _event_times[i]
	if _event_time <= _interval_num:
		_num_events += 1
	else:
		_interval_nums.append(_interval_num)
		_num_events_in_interval.append(_num_events)

	#	print(str(_interval_num) +',' + str(_num_events))

		_interval_num += 1

		_num_events = 1

#print the mean number of events per unit time
print(statistics.mean(_num_events_in_interval))

#plot the number of events in consecutive intervals
fig = plt.figure()
fig.suptitle('Number of events occurring in consecutive intervals in a simulated Poisson process')
plt.bar(_interval_nums, _num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()
'''