#!/usr/bin/env python
# coding: utf-8

# In[24]:


import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F
import numpy as np
from torch.autograd import Variable


# In[25]:


class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(7,512),
                                    nn.Tanh())
        self.layer2 = nn.Sequential(nn.Linear(512,200),
                                    nn.ReLU())
        self.layer3 = nn.Sequential(nn.Linear(200,10),
                                    nn.ReLU())
        self.fc = nn.Sequential(nn.Linear(10,1))
    def forward(self,x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.fc(x)
        return x


# In[26]:


import pandas as pd
data = pd.read_csv(r'data-nhc.csv')
newAdd = data['新增确诊病例-全国（不含港澳台）']
newDead = data['新增死亡病例-全国（不含港澳台）']
newSus = data['新增疑似病例-全国（不含港澳台）']
sumTotal = data['累计确诊病例-全国（不含港澳台）']
nowICU = data['现有重症病例-全国（不含港澳台）']
sumDead = data['累计死亡病例-全国（不含港澳台）']
nowSus = data['现有疑似病例-全国（不含港澳台）']
newCure = data['新增治愈出院-全国（不含港澳台）']
newAdd = newAdd[1:-1]
newDead = newDead[1:-1]
newSus = newSus[1:-1]
sumTotal = sumTotal[1:-1]
sumDead = sumDead[1:-1]
nowICU = nowICU[1:-1]
nowSus = nowSus[1:-1]
newCure = newCure[1:-1]


# In[27]:


def feartureSet():
    xList = []
    yList = []
    for i in range(len(newAdd)):
        xList.append([newAdd.iloc[i],newDead.iloc[i],newSus.iloc[i],
                     sumDead.iloc[i],nowICU.iloc[i],nowSus.iloc[i],newCure.iloc[i]])
        yList.append([sumTotal.iloc[i]])
    return xList,yList


# In[32]:


x_train,y_train = feartureSet()
model = Net()
model = model.cuda()
lossfunc = nn.MSELoss().cuda()
#optimizer = torch.optim.Adam(model.parameters(),lr=0.001,weight_decay=1e-4)
optimizer = torch.optim.SGD(model.parameters(),lr=0.001,weight_decay=1e-4,momentum=0.9)
num_epoch = 50000


# In[34]:


x_train = torch.tensor(x_train).float()
y_train = torch.tensor(y_train).float()

x_train = Variable(x_train.cuda())
y_train = Variable(y_train.cuda())


# In[35]:


plt.ion()
plt.show()
x = [i for i in range(1,71)]
x = np.array(x)
for epoch in range(num_epoch):
    model.train()
    optimizer.zero_grad()
    result = model(x_train)
    loss = lossfunc(result,y_train)
    loss.backward()
    optimizer.step()
    if epoch % 1000 ==0 :
        print("epoch:{} loss:{}".format(epoch,loss.item()))
        plt.cla()
        plt.scatter(x,y_train.cpu().data.numpy())
        plt.plot(x,result.cpu().data.numpy(),'r-',lw=5)
        plt.text(0.5,0,'Loss=%.4f'%loss.cpu().data.numpy(),fontdict={'size':20,'color':'red'})
        plt.pause(0.1)


# In[ ]:




