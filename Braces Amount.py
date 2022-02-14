#!/usr/bin/env python
# coding: utf-8

# In[9]:



import pandas as pd
import numpy as np


# In[10]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'BRACES')
rw.head()


# In[11]:


Br = rw
Br.head()


# In[12]:


Braces = pd.read_excel(r"Z:\Akshay\Sanjit SIr\campaigns\Braces.xlsx")
Braces


# In[13]:


Br.columns


# In[14]:


Br["15 Nov"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)
Br["16 Nov"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)
Br["17 Nov"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)
Br["18 Nov"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)
Br["19 Nov"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)
#Br["30 Oct"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)

#Br["23 Oct, 2021"].replace({1: 300, 2: 1000, 3:1700, 4:2400, 5:3100}, inplace=True)


Br['Total AMount'] = Br["15 Nov"] + Br["16 Nov"] + Br["17 Nov"] + Br["18 Nov"] +Br["19 Nov"] 
Br.head()


# In[15]:


Br.to_excel(r"C:\Users\3363\Desktop\Akshay\Brace Amount.xlsx", index=False)


# In[ ]:




