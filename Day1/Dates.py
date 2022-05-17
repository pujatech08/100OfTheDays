#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[2]:


x=datetime.datetime.now()


# In[3]:


print(x)


# In[4]:


print(x.strftime("%A")) # Weekday, full version


# In[5]:


print(x.strftime("%a")) # Weekday, short version


# In[6]:


print(x.strftime("%B")) #Month name, full version


# In[7]:


print(x.year)


# In[8]:


print(x.strftime("%w")) # Weekday as a number 0-6, 0 is Sunday


# In[9]:


print(x.strftime("%m")) # Month as a number 01-12


# In[10]:


print(x.strftime("%y")) # Year, short version, without century


# In[11]:


print(x.strftime("%Y")) # Year, full version


# In[12]:


print(x.strftime("%H")) # Hour 00-23


# In[13]:


print(x.strftime("%I")) # Hour 00-12


# In[14]:


print(x.strftime("%p")) # AM/PM


# In[15]:


print(x.strftime("%M")) # Minute 00-59


# In[18]:


print(x.strftime("%S"))  # Second 00-59


# In[19]:


print(x.strftime("%f")) # Microsecond 000000-999999


# In[21]:


print(x.strftime("%z"))


# In[22]:


print(x.strftime("%j")) # Day number of year 001-366


# In[23]:


print(x.strftime("%U")) # Week number of year, Sunday as the first day of week, 00-53


# In[24]:


print(x.strftime("%W")) # 	Week number of year, Monday as the first day of week, 00-53


# In[25]:


print(x.strftime("%c")) # 	Local version of date and time


# In[26]:


print(x.strftime("%x")) # Local version of date


# In[27]:


print(x.strftime("%X"))  # Local version of time


# In[28]:


print(x.strftime("%G")) # ISO 8601 year


# In[29]:


print(x.strftime("%u")) # ISO 8601 weekday (1-7)


# In[30]:


print(x.strftime("%V")) # ISO 8601 weeknumber (01-53)


# In[ ]:




