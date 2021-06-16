#!/usr/bin/env python
# coding: utf-8

# In[1]:


# WAP to print factorial of a number, where number is entered by user

num=int(input("Enter a number: "))
fac=1
for i in range(1,num+1):
 fac=fac*i
print(f"Factorial of {num}: " ,fac)


# In[ ]:




