#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Incetive.xlsx")
rw.head()


# In[3]:


rw.fillna(0)


# In[4]:


rw["BRACES"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100, 6:3800, 7:4500}, inplace=True)

rw["CARDIO/PGX- PULMONARY"].replace({1: 250, 2: 750, 3:1250}, inplace=True)

#rw["DIABETES"].replace({1: 200, 2: 600, 3:1000}, inplace=True)

rw["MED. SUP"].replace({1: 0, 2: 200, 3:300, 4:400, 5:500,6:600,7:700}, inplace=True)
rw["CANCER"].replace({1: 250, 2: 500, 3:750}, inplace=True)

rw.fillna(0)

rw['Total Amount'] = rw["BRACES"] + rw["CARDIO/PGX- PULMONARY"] + rw["MED. SUP"] + rw["CANCER"]
Report = rw
Report.head()


# In[5]:


Report.columns


# In[6]:


Report = Report[['Emp #', 'BRACES',  'CARDIO/PGX- PULMONARY' ,'MED. SUP',  'Total', 'Total Amount']]


# In[7]:


Report1 = Report[['Emp #' , 'Total Amount']]
Report1 = Report1[:-1]


# In[8]:


Report1.to_excel(r"C:\Users\3363\Desktop\Akshay\Incetive Final.xlsx", index = False)


# In[ ]:




