#!/usr/bin/env python
# coding: utf-8

# # ASCII Value 

# In[2]:


cap=input("Enter the letter")
print("Enter value '"+cap+"' is:",ord(cap)) # ord() function to convert a character to an integer (ASCII value).


# # print half pyramid using *

# In[5]:


num=int(input("Enter the number"))

for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print("\n")


# In[9]:


num=int(input("Enter the number"))
for i in range(num):
    for j in range(i+1):
        print(1+j,end="")
    print("\n")


# In[12]:


n=int(input("Enter the number"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("\n")


# In[ ]:




