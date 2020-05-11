#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F


# In[2]:


lr = 0.001


# In[3]:


import pandas as pd
data = pd.read_csv(r"data-nhc.csv")


# In[4]:


data = data['累计确诊病例-全国（不含港澳台）']
x_data = []
y_data = []
for i,num in enumerate(data):
    x_data.append([i+1])
    y_data.append([num])


# In[5]:


class virusNet(nn.Module):
    def __init__(self):
        super(virusNet,self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(1,10),nn.Tanh())
        self.layer2 = nn.Sequential(nn.Linear(10,20),nn.ReLU())
        self.layer3 = nn.Sequential(nn.Linear(20,10),nn.ReLU())
        self.fc = nn.Sequential(nn.Linear(10,1))
    
    def forward(self,x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.fc(x)
        return x


# In[6]:


x = torch.tensor(x_data).float()


# In[7]:


y = torch.tensor(y_data).float()


# In[8]:


model = virusNet()
lossfunc = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=lr)
num_epoch = 100000


# In[49]:


plt.ion()
plt.show()
for epoch in range(num_epoch):
    model.train()
    optimizer.zero_grad()
    result = model(x)
    loss = lossfunc(result,y)
    loss.backward()
    optimizer.step()
    if epoch % 10000 ==0 :
        print("epoch:{} loss:{}".format(epoch,loss.item()))
        plt.cla()
        plt.scatter(x.data.numpy(),y.data.numpy())
        plt.plot(x.data.numpy(),result.data.numpy(),'r-',lw=5)
        plt.text(0.5,0,'Loss=%.4f'%loss.data.numpy(),fontdict={'size':20,'color':'red'})
        plt.pause(0.1)


# In[50]:


r = model.forward(torch.tensor([[110]]).float())
r


# ##### 

# In[ ]:




