#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Calculating factors of a number using 'RECURSION'


def factors(n,i):


    if i>n:
        return 0
    if i<=n:
        if n%i == 0:
            print(i, end=" ")
    
    factors(n, i+1)



n=int(input("Enter a number to find it's factors "))
print(f"Factors of {n} is:")
factors(n,1)


# In[ ]:




