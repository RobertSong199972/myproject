#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xgboost as xgb
import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv(r'data-nhc.csv')
newAdd = data['新增确诊病例-全国（不含港澳台）']
newDead = data['新增死亡病例-全国（不含港澳台）']
newSus = data['新增疑似病例-全国（不含港澳台）']
sumTotal = data['累计确诊病例-全国（不含港澳台）']
nowICU = data['现有重症病例-全国（不含港澳台）']
sumDead = data['累计死亡病例-全国（不含港澳台）']
nowSus = data['现有疑似病例-全国（不含港澳台）']
newCure = data['新增治愈出院-全国（不含港澳台）']


# In[3]:


newAdd = newAdd[1:-1]
newDead = newDead[1:-1]
newSus = newSus[1:-1]
sumTotal = sumTotal[1:-1]
sumDead = sumDead[1:-1]
nowICU = nowICU[1:-1]
nowSus = nowSus[1:-1]
newCure = newCure[1:-1]


# In[4]:


import matplotlib.pyplot as plt
from sklearn import preprocessing
from xgboost import plot_importance
from sklearn.preprocessing import Imputer


# In[5]:


def feartureSet():
    xList = []
    yList = []
    for i in range(len(newAdd)):
        xList.append([newAdd.iloc[i],newDead.iloc[i],newSus.iloc[i],
                     sumDead.iloc[i],nowICU.iloc[i],nowSus.iloc[i],newCure.iloc[i]])
        yList.append(sumTotal.iloc[i])
    return xList,yList


# In[6]:


def Train(x_Train,y_Train):
    model = xgb.XGBRegressor(max_depth=6,learning_rate=0.05,n_estimators=500,silent=False,objective='reg:gamma')
    model.fit(x_Train,y_Train)
    return model


# In[7]:


x_train,y_train = feartureSet()


# In[8]:


model = Train(x_train,y_train)


# In[9]:


plot_importance(model)
plt.show()


# In[11]:


ans = model.predict([20,0,12,4644,100,12,45])  #输入格式[新增确诊，新增死亡，新增疑似，总死亡，现ICU，现疑似，新增治愈]


# In[12]:


ans


# In[ ]:




