#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Decimal to binary(method 1)
def decimal_to_binary(num):

    if(num>1):
        decimal_to_binary(num//2)

    
    print(num%2 , end="")

num= int(input("Enter a decimal number: "))
print(f"Binary of {num} is:-")
decimal_to_binary(num)


# In[ ]:




