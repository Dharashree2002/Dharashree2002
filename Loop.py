#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [1, 2, 3, 4] 
your_list = [4, 3, 2, 1] 
his_list = [1, 2, 3, 4]
print(my_list == your_list) 


# In[2]:


print(my_list == his_list)


# In[3]:


my_dict = {1:1, 2:2, 3:3, 4:4} 
your_dict = {4:4, 3:3, 2:2, 1:1}
print(my_dict == your_dict)


# In[4]:


for num in [1,2,3,4,5]:
    print(num**2)


# In[5]:


for num in 'computer':
    print(num)


# In[10]:


import random
r1 = random.random() # Gives us a random number from [0.0, 1.0]
print(r1)


# In[8]:


r2 = random.choice([1,2,3,4,5]) # Gives us a random choice from a list
print(r2)


# In[ ]:


r3 = random.randint(1, 1000) # Gives us a random number in this range
print(r3)


# In[ ]:


for i in range(2004, 2016, 4):
    print(i)


# In[ ]:


menu_prices = {'Knackered Spam': 0.50, 'Pip pip Spam': 1.50, 'Squidgy Spam': 2.50, 'Smashing Spam': 3.50 }
for name, price in menu_prices.items():
    print(name, ': $', price)


# In[ ]:


n= int(input("Enter the Number"))
for num in range(1,n+1,1):
    print(num)


# In[ ]:


n = 1
num= int(input("Enter the Number"))
while n < num :
    n+=1
    print(n)
    n+=1
    


# In[ ]:


x = int(input("Enter the Number X"))
y = int(input("Enter the Number y"))
if x < y: 
    print('x is less than y') 
elif x > y: 
    print('x is greater than y') 
else: 
    print('x and y are equal')


# In[ ]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers:
    print(x)
print(x)


# In[ ]:


name = 'Kochi Python'

for character in name:
    print(character)


# In[ ]:


sports = {"A": "Cricket", "B": "Football", "C": "Hockey", "D": "Badminton", "E": "Kabaddi"}

for x in sports:
    print(x, sports[x])


# In[ ]:


total = 0
values = [1, 2, 4, 8, 16]

for v in values:
    total = total + v
    # total += v
    print(total)

print(total)


# In[ ]:


markList = {
    'Tintumon': 22, 
    'Dundumol': 86, 
    'Dingan': 69, 
    'Luttapi': 45
}

for person in markList:
    if markList.get(person) < 45:
        print(person, " : Failed")
        
    elif markList.get(person) > 45:
        print(person, " : Passed")
        
    else:
        print(person, ' : Just Pass' )


# In[ ]:


value = 0.25
while value < 8:
    value = value * 2
    print(value)
    break

print("final value:", value)


# In[ ]:


#Sum of positive integers in a list
values = [10, -5, 3, -1, 7]

total = 0
for v in values:
    if v < 0:
        continue # Skip this iteration   
    total += v

print(total)


# In[ ]:


#Print from 1 - 7
for n in range(1,10):
    if n % 8 == 0:
        break            # Quit looping at this point
    else:
        print(n)


# In[ ]:


print(list(range(10)))

print(list(range(5, 10)))

print(list(range(0, 10, 3)))

print(list(range(7, 2, -1)))


# In[ ]:


for x in range(8):
    print(x*x)


# In[ ]:


squares = []
for x in range(8):
    s = x*x
    squares.append(s)
    
print(squares)


# In[ ]:


alphabets = ['A', 'B', 'C', 'D', 'E']

for index in range(len(alphabets)):
    print(index, alphabets[index])


# In[ ]:


alphabets = ['A', 'B', 'C', 'D', 'E']
more_alphabets = ['F', 'G', 'H', 'I', 'J']

for index in range(len(alphabets)):
    print(index, alphabets[index], more_alphabets[index])


# In[ ]:


letters = ['A','B','C','D']
for index, letter in enumerate(letters):
    print(index, letter)


# In[ ]:


numbered_letters = list(enumerate(letters))
print(numbered_letters)


# In[ ]:


city_pops = {
    'London': 8200000,
    'Cambridge': 130000,
    'Edinburgh': 420000,
    'Glasgow': 1200000
}

big_cities = []
for city in city_pops:
    if city_pops[city] >= 1000000:
         big_cities.append(city)

print(big_cities)


# In[ ]:


total = 0
for city in city_pops:
    total += city_pops[city]
print("total population:", total)


# In[ ]:


pops = list(city_pops.values())
print("total population:", sum(pops))

