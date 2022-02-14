#!/usr/bin/env python
# coding: utf-8

# In[40]:



import pandas as pd
import numpy as np


# In[41]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'DIABETES')
rw.head()


# In[42]:


Db = rw
Db.head()


# In[43]:


DIABETES = pd.read_excel(r"Z:\Akshay\Sanjit SIr\campaigns\Diabetes.xlsx")
DIABETES


# In[44]:


Db.columns


# In[36]:


Db["18 Oct"].replace({1: 200, 2: 600, 3:1000}, inplace=True)
Db["19 Oct"].replace({1: 200, 2: 600, 3:1000}, inplace=True)
Db["20 Oct"].replace({1: 200, 2: 600, 3:1000}, inplace=True)
Db["21 Oct"].replace({1: 200, 2: 600, 3:1000}, inplace=True)
Db["21 Oct"].replace({1: 200, 2: 600, 3:1000}, inplace=True)
#Db["30 Oct, 2021"].replace({1: 250, 2: 750, 3:1250}, inplace=True)


Db['Total AMount'] = Db["18 Oct"] + Db["19 Oct, 2021"] + Db["20 Oct, 2021"] + Db["21 Oct, 2021"] + Db["22 Oct, 2021"]
Db.head()


# In[39]:


Db.to_excel(r"C:\Users\3363\Desktop\Akshay\DIABETES Amount.xlsx", index= False)


# In[ ]:





# In[ ]:




