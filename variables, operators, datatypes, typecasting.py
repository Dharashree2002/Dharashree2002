#!/usr/bin/env python
# coding: utf-8

# # Welcome to Python Lab

# In[1]:


print("Welcome Python Learners!!")


# # Variables 

# In[2]:


#variable stores some value
x="Hello!"


# In[3]:


x


# In[4]:


y=5


# In[5]:


print(y)


# Suitable variable names

# In[6]:


my_value=78


# In[1]:


my%value=90#invalid syntax


# In[13]:




_my=78.0


# In[12]:


My+value=85#invalid syntax


# In[14]:


2my=78 #variable name cannot start with a numeric value


# In[16]:


x,y,z=1,2,3

print(x,y,z)


# In[15]:


x=y=z=10
print(x,y,z)


# # Datatypes

# In[2]:


y=667 #integer variable
x=3.14 #float variable
z="Hi!" #string variable
p=4+5j #complex variable
q=True #boolean variable


# In[3]:


#finding the datatypes of variables
print(type(y))
print(type(x))
print(type(z))
print(type(p))
print(type(q))


# In[20]:


#boolean value written under cotations then it's a string 
val="False"
print(val)
print(type(val))


# In[23]:


a = 5+8j
b = 6+9j
print(a+b)
print(type(a))

# For taking real or imaginary part separately
print(a.real, ' ',  a.imag)


# In[24]:


l = [10,12,'vivek',13]
print(type(l))


# In[25]:


s = {10,12,'vivek',13}
print(type(s))


# In[26]:


d = {101:'name', 102:'class',102:'year'}
print(type(d))


# In[28]:


s = {10,20,12,'vivek', 20} #here elements of the set can be modified
fs = frozenset(s) #frozenset means the elements in the set can't be modified
print(type(s))
print(type(fs))
print(fs)
#fs[0]=11
#print(fs)


# In[29]:


r = range(10)
print(type(r))
print(r)


# In[30]:


t = (10,12,'vivek',13)
print(type(t))


# In[31]:


#finding the id of an variable
id(val)


# In[32]:


print(id(y))
print(id(x))
print(id(z))
print(id(p))
print(id(q))


# In[33]:


print("id of y is->",id(y))


# In[34]:


#Input by user
name = input("Enter your name:")


# # Operators

# Arithmetic Operators 

# In[39]:


a= 10
b =5

print(a+b)  # Addition

print(a-b)  # Subtraction

print(a*b)  # Multiplication

print(a/b)  # Division and it will always return float values

print(a%b)  # Modulo it finds the remainder

print(a//b)  # Floor Division it will give o/p in float if any number is float otherwise int

print(a**b)  # Exponent Power Operator it is used to raise the 1st operand to power of 2nd


# We can use + (concatenation  operator)  and *(Str multiplication op. ) for str also

print("Ram"+'Shyam'*3)


# Relational Operators

# In[41]:


# >,<,<=,>= are the relational operators
a = 10
b = 5
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# We can apply for strings also

print('a'>'ab')
print('bcd'>'w')


# Logical Operators

# In[42]:


#mainly logical operators are used for conditional statements
a=5
print( a < 10 or a > 5)
print(a < 10 and a > 5)
print(not a)


# Bitwise Operators

# In[43]:


a=10 #1010
b=4 #0100

print(a & b) # If both are is not zero(False) o/p will be True otherwise False

print(a | b) # If any digit is not zero o/p will be True otherwise False

print(~a) # Bitwise complement (complement of 0000 1010)-1111 0101

print(a ^ b)  # x-or If bits are different then result is 1 otherwise 0


# In[44]:


a=10 #in binary no. it is 0000 1010

print(a >> 1) #right shift in binary form

a=-10 #1000 1010 

print(a >> 1)

b=5

print(b << 1) #left shift in binary form

b=-10

print(b << 1)


# Identity Operators

# In[45]:


#It is used to compare objects
a = 10.5
b = 10.5
print(a is b)
print(a is not b)

x = 5+6j
z = 5+6j

print(x is z)
print(x is not z)


# Assignment operators

# In[ ]:


a = 31
b = 10
c = 0

c=a+b
print(c)

c += a #c=c+a
print(c)

c *= a
print(c)

c /= a
print(c)

c=3

c %= a
print(c)

c **= a
print(c)

c //= a
print(c)


# Membership Operators

# In[46]:


#It has in & not in
#it checks if a sequence is present in an object
a = 'Vivek is a great man'
list = [10,13,14]
c =10

print('v' in a)  
print(c in list)  


# Ternary Operator

# In[47]:


x=30 if 10>40 else 40 #condition?option1:option2
print(x)


# In[48]:


#  Print min one
a = 3
b = 7
min = a if a<b else b
print(min)


# # Typecasting

# In[49]:


# bool() is used to convert one type to bool'

print (bool(0))
print(bool(-5))
print(bool("True"))
print(bool("2345678o"))
print(bool(""))
print(bool(10+9j))


# In[50]:


#  complex() function to convert  in complex from,
# While  converting str, it should  be  in form of integral value or float

print(complex(10))
print( complex(10.5))
print( complex("10.5"))
print( complex("10"))
print( complex(True))
print( complex(False))


#  complex(x,y) for creating  x real and  y imag

print(complex(10,-23))
print(complex(1,8))


# In[ ]:


#  float() function for conversion from

float(10)
# float(10+5j)  #cant convert complex  to float

print(float(10))
print(float("10"))
print(float("10.5"))

# While converting str to float, str must be in form of integral or floating point literal
float("10.5")


# In[ ]:


#  int() is used to  convert  values from  other types to int. We  cant convert complex to int

# float to int
print(int(1.234))



# bool to int
print (int(True))
print (int(False))

# Numeric str(whole numbers)  to int
str = "10"
print(int(str))

# For converting from str  to int,  str must contain  only integral value in base 10 form

print(int(0O100))


# # String Operations

# In[ ]:


#Multiline string to a variable
a = """Computer programming is the process of designing and building an executable computer program to 
accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, 
generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms 
in a chosen programming language (commonly referred to as coding).The source code of a program is written in one 
or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central
processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a 
task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient 
programming thus often requires expertise in several different subjects, including knowledge of the application domain, 
specialized algorithms, and formal logic."""


b = "I'm Supreeti.I'm from Odisha.I'm an Indian"
#or 

a='''Computer programming is the process of designing and building an executable computer program to accomplish a 
specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating 
algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen
programming language (commonly referred to as coding).The source code of a program is written in one or more 
languages that are intelligible to programmers, rather than machine code, which is directly executed by the central 
processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of 
a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient 
programming thus often requires expertise in several different subjects, including knowledge of the application domain, s
pecialized algorithms, and formal logic.'''

print(a)
print("\n")
print(b)


# In[51]:


#Length of a string
a="hello!"
print(len(a))


# In[ ]:


#Checking certain phrase or character in the string
t="Hard work and determination leads to success "
print("leads" in t)
print("Hard work" not in t)
print("Hardwork" not in t)


# Slicing
# 

# In[ ]:


b="Hello World!!"
print(b[2:5]) 
print(b[:5]) 
print(b[2:]) 
print(b[-5:-2]) 
print(b[2:5:]) 
print(b[4::]) 
print(b[::])
print(b[2:8:2])
print(b[::-1])
print(b[-10:8])


# In[52]:


#returns string in uppercase
b="Hello World!!"
print(b.upper())
print(b.lower())


# In[53]:


#String Concatenation
str1="Hello"
str2="World"
str=str1 + str2
print(str)
print(str1 + ' ' + str2)


# In[54]:


#Qno1-Slice & Convert the following text into lowercase & uppercase
#input:- My dog maxx performs the sTuntS Under EXperT suPErVIsion. 
#output:- My dog MAXX performs the stunts under expert spervision.
a="My dog maxx performs the sTuntS Under EXperT suPErVIsion."
print(len(a))
print(a[0:7] + a[7:11].upper() + a[11:].lower())


# In[55]:


#Removing whitespaces using strip function
str="  PYTHON  "
print(str.strip())
#Removing whitespaces on right side using rstrip function
str="  PYTHON  "
print(str.rstrip())
#Removing whitespaces on left side using lstrip function
str="  PYTHON  "
print(str.lstrip())


# In[56]:


#split() method that returns a list where the text between the specified separator becomes the list items
a="My handwriting, is not good as, expected."
print(a.split(","))


# In[57]:


#Finding the position of the word
str="python is very easy to learn"
print(str.find("easy"))
print(str.find("very"))
print(str.rfind("easy")) #searching from right to left


# In[ ]:


#Replacing the word in a string
str="python is very easy to learn"
str.replace("easy","difficult")
str.replace("o","a")


# In[58]:


#String format
age = '36'
txt = "My name is John, I am " +age
print(txt)


# In[ ]:


a = "My name is John"
b = " and I'm from Odisha"
print(f"{a}{b}")


# In[ ]:


#String formatting using format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# In[ ]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# In[ ]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# Escape Character:
# 
# To insert characters that are illegal in a string, use an escape character.
# 
# An escape character is a backslash \ followed by the character you want to insert.
# 
# 

# In[ ]:


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# In[ ]:


txt = 'It\'s alright.'
print(txt) 


# In[ ]:


txt = "This will insert one \\ (backslash)."
print(txt) 


# In[ ]:


txt = "Hello\nWorld!"
print(txt) 


# In[ ]:


txt = "Hello\rWorld!"
print(txt) 


# In[ ]:


txt = "Hello\tWorld!"
print(txt) 


# In[ ]:


#This example erases one character (backspace):
txt = "Hello\bWorld!"
print(txt) 

