#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\Employee Name.xlsx")
rw.head()


# In[3]:


Br = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'BRACES')
Br.head()


# In[4]:


Braces = pd.merge(Br, rw, how='left',
        left_on='Emp #', right_on='Emp #')


Braces.head()


# In[5]:


Med = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'MEDSUP')
Med.head()


# In[6]:


MedSupp = pd.merge(Med, rw, how='left',
        left_on='Emp #', right_on='Emp #')


MedSupp.head()


# In[7]:


CPU = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'CPU')
CPU.head()


# In[8]:


CPU = pd.merge(CPU, rw, how='left',
        left_on='Emp #', right_on='Emp #')


CPU.head()


# In[9]:


Cancer = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", sheet_name= 'Cancer')
Cancer.head()


# In[10]:


Cancer = pd.merge(Cancer, rw, how='left',
        left_on='Emp #', right_on='Emp #')


Cancer.head()


# In[11]:




writer = pd.ExcelWriter(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive Result.xlsx", engine='xlsxwriter')


# In[12]:




Braces.to_excel(writer, sheet_name='BRACES')
CPU.to_excel(writer, sheet_name='CPU')
Cancer.to_excel(writer, sheet_name='Cancer')
MedSupp.to_excel(writer, sheet_name='MEDSUP')




writer.save()

