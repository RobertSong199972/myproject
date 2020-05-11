#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from scipy.optimize import curve_fit


# In[44]:


def logistic_increase_function(t,K,P0,r):
    t0=20
    exp_value = np.exp(r*(t-t0))
    return (K*exp_value*P0)/(K+(exp_value-1)*P0)


# In[52]:


data = pd.read_csv(r"data-nhc.csv")
data = data['累计确诊病例-全国（不含港澳台）']
data


# In[7]:


t = []
P = []
for i,num in enumerate(data):
    t.append(i+20)
    P.append(num)
t = np.array(t)
P = np.array(P)


# In[53]:


popt, pcov = curve_fit(logistic_increase_function,t,P)
print("K:capacity  P0:initial_value  r:increase_rate   t:time")
print(popt)
P_predict = logistic_increase_function(t,popt[0],popt[1],popt[2])
future = [i for i in range(20,90)]
future = np.array(future)
future_predict = logistic_increase_function(future,popt[0],popt[1],popt[2])

plot1 = plt.plot(t,P,'s',label="confirmed")
plot2 = plt.plot(t,P_predict,'r',label="predict")
plt.legend(loc=0)
plt.show()



# In[56]:


future_predict[30]


# In[ ]:




