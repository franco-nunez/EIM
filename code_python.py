# -*- coding: utf-8 -*-
"""
Created on Sun May 8 14:00:51 2022

@author: Franco
"""

"""
# Universidad de San Andrés
# Economía Internacional Monetaria
# Fall 2022
# Professors: Damian Pierri - Franco Nuñez

This code is a guide to solve exercise 7, of Guide 3 (2nd part). It is a Python adaptation of the original "code.m", made in Matlab. The idea is to simulate equations 35 and 37 from Chapter 2 of Obstfeld and Rogoff's book.

Note: since this is a "translation" from Matlab, it's not the most efficient way to do it in Python. For example, a possible improvement may be to work with a more vectorized approach.

Version in Google Collab: https://colab.research.google.com/drive/1zpV6vDKWA9cGAR4cZm6vbBmf7Gis_czY#scrollTo=hdyCOxkIwg7J
"""

# Import
import numpy as np # For matrix
import matplotlib.pyplot as plt # For graphs


# In[]:
# Intermediate: Simulations of Y with loop (Obstfeld Rogoff, Chap 1, equation 33)

# Define
l=np.ones((20,3))
r=3*l
x=2.5
i=0 # In Python, things "start at 0", not at 1 as Matlab
np.random.seed(501) # Set the seed: we want to replicate the results

# Loop
while i<=2:
    j=1
    while j<=19: # 19 because lenght is 20 (remember: starts at 0)
        a=np.random.rand(1) # Generate a random integer from 0 to 1
        r[j,i]=0.4*r[j-1,i]-0.4*x+x+a
        j=j+1
    i=i+1  

###
# Graph: simple/manual way
###
plt.figure()
x = range(0, len(r[:,1]))
y_1 = r[:,0]
y_2 = r[:,1]
y_3 = r[:,2]
plt.plot(x, y_1, label = "Simulation 1")
plt.plot(x, y_2, label = "Simulation 2")
plt.plot(x, y_3, label = "Simulation 3")
plt.legend()
plt.show()

###
# Graph: general way
###
import pandas as pd

# First, transform to DataFrame and rename
data_simulated = pd.DataFrame(r)


# Graph
data_simulated.plot()
plt.legend(loc='lower right')
plt.xlabel("Time")
plt.ylabel("Simulations")
plt.show()

# In[]:
# Function: simulations of Y (OR, Chap 2, equation 33)

def simulations_of_y(n_sim = 3, t_horizon = 20, level_y = 3, 
                rho = 0.4, variance_shock = 1, y_hat = 2.5):
    
    # Starting: matrix
    y = np.ones((t_horizon,n_sim))
    y = level_y * y
    
    # Loop
    i=0
    while i <= n_sim-1:
        t=1
        while t<= len(y)-1:
            e = np.random.normal(0, variance_shock)
            y[t,i] = rho*y[t-1,i] - rho*y_hat + y_hat + e
            t = t+1
        i=i+1
    
    # "Save" result
    return y

simulations_y = simulations_of_y(n_sim = 3, t_horizon = 20, level_y = 3, 
                rho = 0.4, variance_shock = 1, y_hat = 2.5)
    
# In[]:
# Function: simple simulations of C, without dynamic change of B (OR, Chap 2, equation 35).
# Note: this is not a complete or valid answer, only a guide.
    
def simple_simulations_of_c(y_simulated, level_c =2, param_1 = 0.4, param_2 = 8):
    
    # Recovering dimensions
    #print(simulations_y)
    n_sim = len(y_simulated[0])
    t_horizon = len(y_simulated)
    # Make matrix
    c = level_c * np.ones((t_horizon,n_sim))
    
    #Loop
    i=0
    while i <= n_sim-1:
        t=1
        while t<= t_horizon-1:
            c[t,i] = param_2 + param_1*y_simulated[t,i]
            t = t+1
        i=i+1
    
    # "Save" result
    return c

simulations_c = simple_simulations_of_c(y_simulated=simulations_y, level_c =2, param_1 = 4, param_2 = 5)

# In[]:
# Function: a guide to simulations of C, (OR, Chap 2, equation 35).
# Note: this is not a complete or valid answer, only a guide.

def simulations_of_c(y_simulated, level_c =2, b = 0, ca = 0, param_1 = 0.4, param_2 = 8):
    
    # Recovering dimensions
    #print(simulations_y)
    n_sim = len(y_simulated[0])
    t_horizon = len(y_simulated)
    # Make matrix
    c = level_c * np.ones((t_horizon,n_sim))
    
    #Loop
    i=0
    while i <= n_sim-1:
        t=1
        while t<= t_horizon-1:
            c[t,i] = param_2 + param_1*y_simulated[t,i] + b
            # Adding b as a difference of results
            b = c[t,i] - c[t-1,i]
            # Print if you want to see results
            #print("C for sim", i, "and t", t, "is", round(c[t,i],1))
            #print("b for sim", i, "and t", t, "is", round(b,1))
            t = t+1
        i=i+1
    
    # "Save" result
    return c

simulations_c2 = simulations_of_c(y_simulated=simulations_y, level_c =2, param_1 = 4, param_2 = 5)

