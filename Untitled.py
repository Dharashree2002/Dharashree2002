#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Qno- TO check whether it is armstrong number or not

num=int(input("Enter any number:"))
sum=0
temp=num
while num!=0:
    rem = num%10
    sum+= rem**3
    num = num//10
if temp==sum:
    print(temp ,'is an armstrong number')
else:
    print(temp ,'is not an armstrong number')


# In[ ]:




