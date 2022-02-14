#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


Employee= pd.read_excel(r"C:\Users\3363\Desktop\Reports\Employee Report.xlsx")
Employee.head()


# In[3]:


Employee.info()


# In[4]:


Incentive = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Incetive amount.xlsx")
Incentive.head()


# In[5]:


Incentive = Incentive.rename(columns = {'Emp #' : 'Emp Id'})
#Incentive = Incentive.drop(columns=['DATE'])

Incentive.head()


# In[6]:


Result = pd.merge(Employee, Incentive, how = 'outer', on = 'Emp Id')

Result.head()


# In[7]:


import datetime

#Result['DOJ'] = pd.to_datetime(Result['DOJ'], errors='coerce')
#Result['DOJ'] = Result['DOJ'].dt.strftime('%d %b, %Y')
#Result['Total Amount'] = Result['Total Amount'].fillna(0)
#Result.head()


# In[8]:


Result = Result[(Result[['Total Amount']] != 0).all(axis=1)]
Result.head()


# In[9]:


Result1 = Result[['Emp Id','Employee Name', 'Total Amount']]


# In[10]:


raw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\HR.xlsx")
raw.head()


# In[11]:




writer = pd.ExcelWriter(r"C:\Users\3363\Desktop\Akshay\International Incetives.xlsx", engine='xlsxwriter')


# In[12]:



raw.to_excel(writer, sheet_name='Dump', index=False)
Result1.to_excel(writer, sheet_name='Emp VS Amt', index=False)
Result.to_excel(writer, sheet_name='Employee Report', index=False)

writer.save()


# In[ ]:




