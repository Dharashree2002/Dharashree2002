#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = -3

if x > 0:
    print("Value is positive")

elif x < 0:
    print("Value is negative")

else:
    print("Value is zero")


# In[1]:


name = "luttapi"
mark = 30

if mark < 45:
    print(name, "has failed in the exam")
        
elif geneExpression > 0:
    print(name, "has passed in the exam")
        
else:
    pass


# In[3]:


x = 11

if x < 10:
    s = "Yes"
else:
    s = "No"
print(s)

# Could also be written onto one line
s = "Yes" if x < 10 else "No"
print(s)


# With conditional execution the question naturally arises as to which expressions are deemed to be true and which false. For the python boolean values <tt>True</tt> and <tt>False</tt> the answer is (hopefully) obvious. Also, the logical states of truth and falsehood that result from conditional checks like “Is x greater than 5?” or “Is y in this list?” are also clear. When comparing values Python has the standard comparison (or relational) operators, some of which we have already seen:
# 
# |Operator |	Description |	Example |
# |---------|-------------|-----------|
# |`==`  |	    equality |	1 == 2 # False |
# |`!=`  |	    non equality |	1 != 2 # True |
# | `<`  |	    less than |	1 < 2 # True |
# | `<=` |	    equal or less than |	2 <= 2 # True |
# | `>`  |	    greater then |	1 > 2 # False |
# | `>=` |	    equal or greater than |	1 >= 1 # True |
# 
# It is notable that comparison operations can be combined, for example to check if a value is within a range.

# In[7]:


x = 5

#if x > 0 and x < 10:
if 0 < x < 10: #is also possible
    print("In range A")
else:
    print("Not in range")
    
#elif x < 0 or x > 10:
#    print("In range B")


# In[ ]:


x = [123, 54, 92, 87, 33]
y = x[:] # y is a copy of x
z = x
print(x)
print("Are values of y and x the same?", y == x)
print("Are objects y and x the same?", y is x)
print("Are values of z and x the same?", z == x)
print("Are objects z and x the same?", z is x)
# Let's change x
x[1] = 23
print(x)
print("Are values of y and x the same?", y == x)
print("Are objects y and x the same?", y is x)
print("Are values of z and x the same?", z == x)
print("Are objects z and x the same?", z is x)


# In Python even expressions that do not involve an obvious boolean value can be assigned a status of "truthfulness";  the value of an item itself can be forced to be considered as either True or False inside an if statement. For the Python built-in types discussed in this chapter the following are deemed to be False in such a context:
# 
# | False value | Description | 
# |-------------|-------------|
# | `None` |	numeric equality |
# | `False` |	False boolean |
# | `0`	| 0 integer |
# | `0.0` |	0.0 floating point |
# | `""` |	empty string |
# | `()` |	empty tuple |
# | `[]` |	empty list |
# | `{}` |	empty dictonary |
# | `set()` |	empty set |
# 
# And everything else is deemed to be True in a conditional context.

# In[2]:


x = ''      # An empty string
y = ['a']   # A list with one item

if x:
    print("x is true")
else: 
    print("x is false")     

if y:
    print("y is true")
else:
    print("y is false")


# In[ ]:




