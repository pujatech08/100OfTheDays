#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x,y):
    return x+y
def Subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Please select operation -\n" "1. Add\n" "2. Subtract\n" "3. Multiply\n" "4. Divide\n")

select = int(input("Select Operations from 1,2,3,4 :"))
num    = int(input("Enter the First Number:"))
num1   = int(input("Etner the Second Number:"))

if select == 1:
    print(num,"+",num1,"=",add(num,num1))
elif select ==2:
    print(num,"-",num1,"=",Subtract(num,num1))
elif select == 3:
    print(num,"*",num1,"=",multiply(num,num1))
elif select == 4:
    print(num,"/",num1,"=",divide(num,num1))
else:
    print("Invalid Input")


# In[ ]:




