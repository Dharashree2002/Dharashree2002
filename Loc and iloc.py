#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing pandas and numpy
import pandas as pd
import numpy as np

# crete a sample dataframe
data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']
})

# view the data
data


# In[5]:


data.loc[2:4,['age','city']]


# In[6]:


data.iloc[2:4,[0,2]]


# In[7]:


data.loc[data.age >= 15]


# In[8]:


# select with multiple conditions
data.loc[(data.age >= 12) & (data.gender == 'M')]


# In[6]:


#slice
data.loc[1:3]


# In[7]:


# select few columns with a condition
data.loc[(data.age >= 12), ['city', 'gender']]


# In[8]:


# update a column with condition
data.loc[(data.age >= 12), ['section']] = 'M'
data


# In[9]:


# update multiple columns with condition
data.loc[(data.age >= 20), ['section', 'city']] = ['S','Pune']
data


# In[9]:


# select rows with indexes
data.iloc[[0,2]]


# In[10]:


# select rows with particular indexes and particular columns
data.iloc[[0,2]]


# In[11]:


# select a range of rows
data.iloc[1:3]


# In[13]:


# select a range of rows and columns
data.iloc[1:3,2:4]


# In[14]:


# importing the module 
import pandas as pd


# In[15]:


# creating a sample dataframe 
data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai', 'Tata', 
                                'Mahindra', 'Maruti', 'Hyundai', 
                                'Renault', 'Tata', 'Maruti'], 
                     'Year' : [2012, 2014, 2011, 2015, 2012,  
                               2016, 2014, 2018, 2019], 
                     'Kms Driven' : [50000, 30000, 60000,  
                                     25000, 10000, 46000,  
                                     31000, 15000, 12000], 
                     'City' : ['Gurgaon', 'Delhi', 'Mumbai',  
                               'Delhi', 'Mumbai', 'Delhi',  
                               'Mumbai','Chennai',  'Ghaziabad'], 
                     'Mileage' :  [28, 27, 25, 26, 28,  
                                   29, 24, 21, 24]}) 
   
# displaying the DataFrame 
display(data) 


# In[16]:


# selecting cars with brand 'Maruti' and Mileage > 25 
display(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)]) 


# In[17]:


# selecting range of rows from 2 to 5 
display(data.loc[2 : 5]) 


# In[18]:


# updating values of Mileage if Year < 2015 
data.loc[(data.Year < 2015), ['Mileage']] = 22
display(data) 


# In[19]:


# selecting 0th, 2th, 4th, and 7th index rows 
display(data.iloc[[0, 2, 4, 7]]) 


# In[20]:


# selecting rows from 1 to 4 and columns from 2 to 4 
display(data.iloc[1 : 5, 2 : 5]) 


# In[21]:


s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])


# In[22]:


s


# In[23]:


s.iloc[:3]


# In[24]:


s.loc[:3]


# In[25]:


s.iloc[:6]


# In[26]:


df = pd.DataFrame({'age':[30, 2, 12, 4, 32, 33, 69],
                   'color':['blue', 'green', 'red', 'white', 'gray', 'black', 'red'],
                   'food':['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
                   'height':[165, 70, 120, 80, 180, 172, 150],
                   'score':[4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'state':['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])


# In[27]:


df.loc['Penelope']


# In[28]:


df.loc[['Cornelia', 'Jane', 'Dean']]


# In[29]:


df.loc['Aaron':'Dean']


# In[30]:


df.iloc[4]


# In[31]:


df.iloc[[2, -2]]


# In[32]:


df.iloc[:5:3]


# In[33]:


df.loc[['Jane', 'Dean'], 'height':]


# In[34]:


df.iloc[[1,4], 2]


# In[35]:


df.loc[:, 'color':'score':2]


# In[36]:


labels = ['Nick', 'Cornelia']
index_ints = [df.index.get_loc(label) for label in labels]
df.iloc[index_ints, [2, 4]]


# In[37]:


df.loc[df['age'] > 30, ['food', 'score']] 


# In[38]:


df.iloc[(df['age'] > 30).values, [2, 4]] 


# In[39]:


df.loc[:, 'color':'score':2]


# In[40]:


df['food']


# In[41]:


df[['food', 'score']]


# In[42]:


df['Penelope':'Christina'] # slice rows by label


# In[43]:


df[2:6:2] # slice rows by integer location


# In[ ]:




