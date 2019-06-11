#!/usr/bin/env python
# coding: utf-8

# In[1]:


answer=19
guess=int(input("enter a number:"))
if answer==guess:
    print("answer and guess are same ")
elif answer>guess:
    print("guess is lower than answer")
else:
    print("guess is higher than answer")


# In[3]:


for i in range(0,7):
    print(5*i)


# In[4]:


i=0
integerlimit=int(input("enter integerlimit:"))
while(i**2<=integerlimit):
    i+=1
print("nearest square:",i-1)

