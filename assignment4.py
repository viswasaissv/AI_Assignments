#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
items=[{'YEAR':1990,'NAME':'ALICE','DEPARTMENT':'HR','AGE':25,'SALARY':50000},{'YEAR':1990,'NAME':'BOB','DEPARTMENT':'RD','AGE':30,'SALARY':48000},{'YEAR':1990,'NAME':'CHARLIE','DEPARTMENT':'ADMIN','AGE':45,'SALARY':55000},{'YEAR':1991,'NAME':'ALICE','DEPARTMENT':'HR','AGE':26,'SALARY':52000},{'YEAR':1991,'NAME':'BOB','DEPARTMENT':'RD','AGE':31,'SALARY':50000},{'YEAR':1991,'NAME':'CHARLIE','DEPARTMENT':'ADMIN','AGE':46,'SALARY':60000},{'YEAR':1992,'NAME':'ALICE','DEPARTMENT':'ADMIN','AGE':27,'SALARY':60000},{'YEAR':1992,'NAME':'BOB','DEPARTMENT':'RD','AGE':32,'SALARY':52000},{'YEAR':1992,'NAME':'CHARLIE','DEPARTMENT':'ADMIN','AGE':28,'SALARY':62000},]
data=pd.DataFrame(items,index=[0,1,2,3,4,5,6,7,8])
print(data)
print(data.groupby(['YEAR'])['SALARY'].sum())
print(data.groupby(['NAME'])['SALARY'].sum())
print(data.groupby(['YEAR','DEPARTMENT'])['SALARY'].sum())


# In[ ]:




