#!/usr/bin/env python
# coding: utf-8

# # Genrate Randam Number

# In[1]:


import random


# In[2]:


print(random.randint(0,9))


# # Check if a Number is Positive, Negative or 0

# In[5]:


num=int(input("Enter the number"))
if num>0:
    print("Number is Positive")
elif num==0:
    print("Number is Zero")
else:
    print("Number is Negative")


# # Check if a Number is Odd or Even

# In[9]:


num=int(input("Enter the number"))
if num%2==0:
    print("Number is Even")
else:
    print("Number is odd")


# # Check if a Number is Prime Number or not

# In[13]:


num=int(input("Enter the number"))
flag=False
for i in range(2,num):
    if(num%i == 0):
        flag=True
        break
if flag:
    print(num,"Number is not Prime Number")
else:
    print(num,"Number is Prime Number")


# # Factorial Number

# In[16]:


num=int(input("Enter the number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("Factorial number is:",factorial)


# # Tables

# In[22]:


num=int(input("Enter the number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


# In[ ]:




