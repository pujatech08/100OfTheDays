#!/usr/bin/env python
# coding: utf-8

# # Python Program to Measure the Elapsed Time...

# In[4]:


import time
start=time.time()
print(23*2.3)
end=time.time()
print(end - start)


# # Python Program to Get the Class Name of an Instance  

# In[9]:


class Vahicle:
    def name(self,name):
        return name
v=Vahicle()   # Create an object v of class Vehicle().
print(v.__class__.__name__)  # Print the name of the class using __class__.__name__.


# # Python Program to Differentiate Between type() and isinstance()

# In[ ]:


class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def area(self):
        pass

obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)   # true
print(type(obj_triangle) == Polygon)    # false

print(isinstance(obj_polygon, Polygon))  # true
print(isinstance(obj_triangle, Polygon)) # true

