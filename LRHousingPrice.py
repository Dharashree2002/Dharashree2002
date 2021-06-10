#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[3]:


USAhousing = pd.read_csv('USA_Housing.csv')
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 1)


# In[3]:


lm = LinearRegression()
lm= lm.fit(X_train,y_train)
predictions = lm.predict(X_test)
accuracy = lm.score(X_test,y_test)
print(accuracy*100,'%')

