#!/usr/bin/env python
# coding: utf-8

# # Sets
# 

# In[1]:


set1 = {"apple", "banana", "cherry"}
print(set1)


# Set:-
# *Sets are used to store multiple items in a single variable.
# *Set is a collection which is both unordered and unindexed.
# *Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# *Sets are unchangeable, as we cannot change the items after the set has been created.
# *Sets cannot have two items with the same value.

# In[2]:


print(len(set1))


# In[3]:


set1 = {"abc", 34, True, 40, "male"}


# In[5]:


#Using the set() constructor to make a set
set2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set2)
print(type(set2))


# In[6]:


#Access Items from a set
set = {"apple", "banana", "cherry"}

for x in set:
    print(x)

#Checking items present in a set
print("\n")
print("banana" in set)


# In[7]:


#Add Items in a set using add() method
set.add("orange")
print(set)

print('\n')
#Add Items in a set using update() method
set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

set.update(tropical)
print(set)
print("\n")
#Adding items from list,tuple & dictionary
set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thistuple = ("kiwi", "orange") #tuple
thisdict = {"papaya":5, "watermelon":2}
set.update(mylist,thistuple,thisdict)

print(set)


# In[8]:


#Remove an item from a set using remove() method
set = {'banana', 'cherry', 'papaya', 'kiwi', 'apple', 'watermelon', 'orange'}
set.remove("cherry")

print(set)
print("\n")
#Remove an item from a set using discard() method
set.discard("banana")
print(set)
print("\n")
#Remove an item from a set using pop() method
set.pop()
print(set)


# In[9]:


#Clearing a set using clear() method
set = {"apple", "banana", "cherry"}
set.clear()

print(set)
print("\n")
#Delete the set completely
del set

print(set)


# In[10]:


#Joining of two set union() method

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print("\n")
#Joining of two sets using update() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# In[11]:


#intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana"}

x.intersection_update(y)
print(x)
print("\n")
#intersection() method will return a new set, that only contains the items that are present in both sets
z = x.intersection(y)

print(z)


# In[14]:


#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana"}

x.symmetric_difference_update(y)

print(x)
print('\n')


# In[15]:


#symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana"}

z = x.symmetric_difference(y)

print(z)


# # Dictionary

# Dictionary:-
# *Dictionaries are used to store data values in key:value pairs.
# *Dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# *Dictionary items are ordered, changeable, and does not allow duplicates.
# *Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# *Dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# *Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# *Dictionaries cannot have two items with the same key.

# In[16]:


d = {'key1':'item1','key2':'item2'}
print(d)
print(d["key1"])


# In[17]:


#String, int, boolean, and list data types in dictionary
dict = {"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]}
print(dict)


# In[18]:


#Accessing Items:You can access the items of a dictionary by referring to its key name
print(dict["year"])
#Accessing items using get() method
print(dict.get("colors"))


# In[19]:


#Get Keys:The keys() method will return a list of all the keys in the dictionary.
x = dict.keys()
print(x)


# In[20]:


#Get Values:The values() method will return a list of all the values in the dictionary.
x = dict.values()
print(x)


# In[21]:


#Get Items:The items() method will return each item in a dictionary, as tuples in a list.Get a list of the key:value pairs
x = dict.items()
print(x)


# In[24]:


#Make a change in the original dictionary
x = dict["year"] = 2020

print(x) #after the change
print(dict)

#Add a new item to the original dictionary
y = dict["slno"] = "4100"

print(y) #after the change
print(dict)


# In[25]:


#Updating or changing in a dictionary
dict = {"brand": "Ford","electric": False,"year": 1964,"color":"red"}
dict.update({"year": 2020})
print(dict)


# In[26]:


#Removing Items from a dictionary
dict = {"brand": "Ford","electric": False,"year": 1964,"color":"red"}
dict.pop("brand")
print(dict)
print('\n')

#The popitem() method removes the last inserted item
dict.popitem()
print(dict)
print('\n')

#The del keyword removes the item with the specified key name
del dict["electric"]
print(dict)
print('\n')

#The clear() method empties the dictionary
dict.clear()
print(dict)


# In[27]:


#Looping in the dictionary
dict = {"brand": "Ford","electric": False,"year": 1964,"color":"red"}

"""Print all key names in the dictionary, one by one"""
for x in dict:
    print(x)

print('\n')
"""Print all values in the dictionary, one by one"""
for x in dict:
    print(dict[x])


# In[28]:


#returns values in dict
for x in dict.values():
    print(x)
print("\n")
#returns key in dict 
for x in dict.keys():
    print(x)
print('\n')
#returns key:value pair in dict
for x, y in dict.items():
    print(x,"->", y)


# In[29]:


#Nested dictionary

myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : 
            {"name" : "Linus","year" : 2011}}
print(myfamily)


# **Qno- Create three dictionaries separately, then create one dictionary that will contain the other three dictionaries

# **Qno- Create a dictionary of address using "name", "address", "street", "state" and print all the values using string formater

# **Qno- Write a program to multiply all elements of dictionary
# Input:- FruitDict = {'Apple': 10, 'banana': 5,'orange':4,'Guava':6}
# Output:- 1200

# **Qno- Create a user input dictionary having two key:value pair and check whether one of the key given by you is pesent in the dictionary
# Input:- {hari:59,sunny:60}
# Checking_input:- hari
# Output:- hari=59

# # Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# 
# Syntax: 
# lambda arguments : expression

# In[30]:


#Multiply 6 to argument a, and return the result:

x = lambda a : a * 6
print(x(5))

#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


# **Qno-Write a Python program to sort a list of tuples using Lambda.
# Input: [('Eng', 88), ('Sci', 90), ('Maths', 97), ('Sst', 82)]
# Output: [('Sst', 82), ('Eng', 88), ('Sci', 90), ('Maths', 97)]

# # Function

# Functions:A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# In[31]:


def func():
    print('This is a custom function')


# In[32]:


func()


# In[33]:


def func1(a):
    print('This ia s custom function '+str(a))


# In[34]:


func1('created by me')
func1(2)
func1(3.665)


# In[35]:


def func2(a,b):
    c=a+b
    print(c)
func2(9,7)
func2('ram & ','hari')


# In[36]:


#Use of Return Statement in a Function
def func3(a,b):
    c=a+b
    return c
a=func3(5,8)
print(a)


# **Qno- Define a function with two arguments a and b. Check if a is equal to 1 then return 'coming from if',check if b is equal to 1 ,then return 'coming from elif' otherwise return 'no condition is satisfied'

# In[37]:


#Use of Default Argument
def func5(name='ram',roll_no=1,branch='CSE'):
    print('Name is '+name)
    print('Roll no. is '+str(roll_no))
    print('Branch is '+branch,end='\n\n')
func5()


# In[38]:


func5('hari')


# In[39]:


func5('shayam',5)


# In[40]:


func5('sunny',7,'EEE')


# In[41]:


func5(branch='ECE')


# In[42]:


#Average of list of nos.
def average(a):
    s=0
    n=len(a)
    for i in a:
        s=s+i
    av=s/n
    return av
c=average([4,9,6])
print(c)


# In[43]:


#Use of Variable Argument
#If the number of arguments is unknown, add a * before the parameter name
def funvar(name='ram',*vararg):
    print('Name is '+name,end='\n')
    for i in vararg:
        print(i)
funvar()
funvar('Hari')


# In[44]:


funvar('Shyam','Roll no is 8','Branch is CSE')


# In[45]:


#If the number of keyword arguments is unknown, add a double ** before the parameter name
def my_function(**St):
    print("Her last name is " +St["lname"])

my_function(fname = "Supreeti", lname = "Subudhi")


# In[46]:


#for multiple values using an Variable Argument
def average(*a):
    s=0
    n=len(a)
    for i in a:
        s=s+i
    av=s/n
    return av
c=average(4,9,6)
print(c)


# **Qno-Take a Dictionary as given in input.Find the average of phy subject from the dict using function
# Input:- dict={1:{'name':'Ram','Mark':{'phy':56,'chem':78}},2:{'name':'Hari','Mark':{'phy':76,'chem':88}}}
# Output:- 66.0

# In[47]:


#use of Global variable: Global variable can be accessed by other functions also
def myadd(a,b,c):
    global d
    d=a+b+c
    return d
def mysub(e):
    f=d-e
    return f
print(myadd(1,2,3))
print(mysub(2))


# In[48]:


#use of Global variable
global d
def myadd(a,b,c):
    d=a+b+c
    return d
def mysub(e):
    f=d-e
    return f
print(myadd(1,2,3))
print(mysub(2))


# In[49]:


def myadd(a,b,c):
    d=a+b+c
    return d
def mysub(e):
    f=d-e
    return f
print(myadd(4,5,3))
print(mysub(28))
global d


# In[50]:


#Lambda function inside a function
def myfunc(n):
    return lambda a : a * n

x = myfunc(2)

print(x(11))

