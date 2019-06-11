#!/usr/bin/env python
# coding: utf-8

# In[2]:


population={"Shangali":17.8,"Istambul":13.3,"Karachi":13.0,"Mumbai":12.5}
print(population)


# In[7]:


animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals['dogs'])
print(animals['dogs'][3])
print(animals['fish'])
print(animals[3])


# In[8]:


a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))


# In[9]:


tuple_a = 3, 4
tuple_b = (3, 4)

print(tuple_a == tuple_b)
print(tuple_a[1])


# In[10]:


names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


# In[ ]:




