#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data=pd.DataFrame({
    'age':[30,2,12,4,32,33,69],'color':['blue','green','red','white','gray','black','red'],'food':['steak','lamb','mango','apple','cheese','melon','beans'],'height':[165,70,120,80,180,172,150],'score':[4.6,8.3,9.0,3.3,1.8,9.5,2.2],'state':['NY','TX','FL','AL','AK','TX','TX']},index=["Jane","Nick","Aron","Penelope","Dean","Christina","Cornelia"])
data


# In[5]:


# Selecting column Penelope

data.loc['Penelope']


# In[7]:


#columns from Aron to Dean

data.loc['Aron':'Dean']


# In[15]:


# selecting columns jane,dean,cornelia
data.loc[["Jane","Dean","Cornelia"]]


# In[18]:


#selecting 4th index column
data.iloc[4]


# In[ ]:




