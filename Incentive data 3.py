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


Incentive= pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Incetive Final.xlsx")
Incentive.head()


# In[5]:


Incentive = pd.DataFrame(Incentive.groupby(['Emp #'])['Total Amount'].agg('sum'))
Incentive.head()


# In[6]:


Incentive = Incentive.rename(columns = {'Emp #' : 'Emp Id'})
#Incentive = Incentive.drop(columns=['DATE'])

Incentive.head()


# In[7]:


Incentive.to_excel(r"C:\Users\3363\Desktop\Akshay\Incetive amount.xlsx")


# In[ ]:





# In[ ]:




