#!/usr/bin/env python
# coding: utf-8

# In[14]:



import pandas as pd
import numpy as np


# In[15]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'CPU')
rw.head()


# In[16]:


Cr = rw
Cr.head()


# In[17]:


CARDIAC = pd.read_excel(r"Z:\Akshay\Sanjit SIr\campaigns\cardiac.xlsx")
CARDIAC


# In[18]:


Cr.columns


# In[19]:


Cr["08 Nov"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Cr["09 Nov"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Cr["10 Nov"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Cr["11 Nov"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
Cr["12 Nov"].replace({1: 250, 2: 750, 3:1250}, inplace=True)
#Cr["22 Oct"].replace({1: 250, 2: 750, 3:1250}, inplace=True)


Cr['Total AMount'] = Cr["08 Nov"] + Cr["09 Nov"] + Cr["10 Nov"] +  Cr["11 Nov"] + Cr["12 Nov"]
Cr.head()


# In[20]:


Cr.to_excel(r"C:\Users\3363\Desktop\Akshay\CPU Amount.xlsx")


# In[ ]:




