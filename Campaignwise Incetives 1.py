#!/usr/bin/env python
# coding: utf-8

# In[8]:



import pandas as pd
import numpy as np


# In[9]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\HR.xlsx")
rw.head()


# In[10]:


import datetime


# In[11]:



rw['DATE'] = rw['DATE'].dt.strftime('%d %b')
rw.head()


# In[12]:


Agent = pd.read_excel(r"Z:\Akshay\Sanjit SIr\campaigns\Agent List.xlsx")
Agent.head()


# In[13]:


#rw = pd.merge(rw, Agent, how='left',
#        left_on='Emp #', right_on='Emp #')


# In[14]:


BRACES = rw.loc[(rw['CAMPAIGN'] == "BRACES")]

CPU = rw.loc[(rw['CAMPAIGN'] == "CARDIO/PGX- PULMONARY")]

#DIABETES = rw.loc[(rw['CAMPAIGN'] == "DIABETES")]

MEDSUP = rw.loc[(rw['CAMPAIGN'] == "MED. SUP")]

#PGX = rw.loc[(rw['CAMPAIGN'] == "PGX")]
CANCER = rw.loc[(rw['CAMPAIGN'] == "CANCER")]


# In[15]:


Result1 =pd.pivot_table(data= BRACES , index = ['Emp #'],columns= ['DATE'],values = 'CAMPAIGN', aggfunc = np.size, fill_value=0)


Result1.head()


# In[16]:


Result2 =pd.pivot_table(data= CPU , index = ['Emp #'],columns= ['DATE'],values = 'CAMPAIGN', aggfunc = np.size, fill_value=0)



Result2.head()


# In[17]:


Result3 =pd.pivot_table(data= CANCER , index =['Emp #'],columns= ['DATE'],values = 'CAMPAIGN', aggfunc = np.size, fill_value=0)



Result3.head()


# In[18]:


Result4 =pd.pivot_table(data= MEDSUP , index = ['Emp #'],columns= ['DATE'],values = 'CAMPAIGN', aggfunc = np.size, fill_value=0)



Result4.head()


# In[19]:




writer = pd.ExcelWriter(r"C:\Users\3363\Desktop\Akshay\Campaign Wise incetive.xlsx", engine='xlsxwriter')


# In[20]:




Result1.to_excel(writer, sheet_name='BRACES')
Result2.to_excel(writer, sheet_name='CPU')
Result3.to_excel(writer, sheet_name='Cancer')
Result4.to_excel(writer, sheet_name='MEDSUP')




writer.save()


# In[ ]:




