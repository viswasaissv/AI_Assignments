#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])
print("add:",np.add(x,y))
print("subtract:",np.subtract(x,y))
print("multiply:",np.multiply(x,y))
print("division:",np.divide(x,y))


# In[4]:


X = np.array([[1,2], [3,4]])
sorted_columns=np.sort(X,axis=0)
print("max ",X.max())
print("min:",X.min())
print("median:",np.median(X))
print("square root",np.sqrt(X))
print("mean:",X.mean())
print("standard deviation:",X.std())
print("exponent:",np.exp(X))


# In[ ]:




