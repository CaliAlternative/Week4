#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
from pprint import pprint
import pandas as pd


# In[3]:


GetWebsiteURL = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"
WR = requests.get(GetWebsiteURL)
x = WR.json()
pprint(x)


# In[4]:


states = []
i = 0
while i < 51:
    i = i+1
    y = x['data'][i]['State']
    states.append(y)
    #print(x['data'][i]['State']) 
print(states)


# In[5]:


population = []
i = 0
while i < 51:
    i = i+1
    yy = x['data'][i]['Population']
    population.append(yy)
print(population)


# In[6]:


mydata = {
    "states": states,
    "population": population
}

mydata = pd.DataFrame(mydata)
mydata.head(10)


# In[ ]:




