#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\HR.xlsx")
rw.head()


# In[3]:


import datetime


# In[4]:



rw['DATE'] = rw['DATE'].dt.strftime('%d %b')
rw.head()


# In[5]:


#rw = rw.loc[(rw['DATE'] == '18 Oct, 2021') | (rw['DATE'] == '19 Oct, 2021') | (rw['DATE'] == '20 Oct, 2021')]


# In[6]:


Result =pd.pivot_table(data= rw, index = ['DATE','Emp #'],columns= ['CAMPAIGN'],values = 'QA RESULT', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Result.head()


# In[7]:


Result.to_excel(r"C:\Users\3363\Desktop\Akshay\Incetive.xlsx")


# In[ ]:




