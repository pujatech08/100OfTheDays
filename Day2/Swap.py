#!/usr/bin/env python
# coding: utf-8

# # Swap Two Number

# In[1]:


num=int(input("Enter First Number"))
num1=int(input("Enter Second Number"))
tem=num
num=num1
num1=tem
print("After Swap of First Number",num)
print("After swap of second Number",num1)


# # Another way of swap two number

# In[3]:


num=int(input("Enter First Number"))
num1=int(input("Enter Second Number"))
num=num+num1   # 10+11=21
num1 =num-num1  # 21-11=10
num =num-num1 
print("After Swap of First Number",num)
print("After swap of second Number",num1)


# In[6]:


num=int(input("Enter First Number"))
num1=int(input("Enter Second Number"))
num=num*num1  # 5*4=20
num1=num/num1  
num=num/num1
print("After Swap of First Number",num)
print("After swap of second Number",num1)


# In[ ]:




