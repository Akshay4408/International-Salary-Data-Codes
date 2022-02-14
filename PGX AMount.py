#!/usr/bin/env python
# coding: utf-8

# In[3]:



import pandas as pd
import numpy as np


# In[4]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'PGX')
rw.head()


# In[10]:


Pg = rw
Pg.head()


# In[11]:


PGX = pd.read_excel(r"Z:\Akshay\Sanjit SIr\campaigns\Pux.xlsx")
PGX


# In[12]:


Pg["25 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Pg["26 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Pg["27 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Pg["28 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Pg["29 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
#Cr["30 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)


Pg['Total AMount'] =  Pg["25 Oct, 2021"] +Pg["26 Oct, 2021"] + Pg["27 Oct, 2021"] + Pg["28 Oct, 2021"] + Pg["29 Oct, 2021"]
Pg.head()


# In[13]:


Pg.to_excel(r"C:\Users\3363\Desktop\Akshay\PGX Amount.xlsx")


# In[ ]:




