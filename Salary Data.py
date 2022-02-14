#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


Attendence = pd.read_excel(r"C:\Users\3363\Desktop\International\salary.xlsx")
Attendence.head()


# In[3]:


Attendence.info()


# In[4]:


salary= pd.read_excel(r"C:\Users\3363\Desktop\International\salary Amount.xlsx")
salary.head()


# In[5]:


Report = pd.merge(Attendence, salary, how='left',
        left_on='Employee #', right_on='Employee #')
Report.head()


# In[6]:


Report['HD'] = Report['F-OUT'] + Report['F-IN'] + Report['PP-(HD)']


# In[7]:


Report['PER DAY'] = Report['Salary'] / 30
Report['PRESENT'] = Report['PER DAY'] * Report['PP']
Report['HALFDAY'] = (Report['PER DAY'] * Report['HD'])/2
Report['ABSENT'] = Report['PER DAY'] * Report['AA']
Report['WeekOff'] = Report['PER DAY'] * Report['WW']
Report['EEarining'] = Report['PER DAY'] * Report['EE']
Report['Training Earning'] = Report['TT'] * 100
Report['Salary Anounce'] = Report['PRESENT'] + Report['HALFDAY'] + Report['EEarining'] + Report['WeekOff'] + Report['Training Earning']
Report['Salary Deduct']= Report['Salary'] - Report['Salary Anounce']


# In[8]:


Report.to_excel(r"C:\Users\3363\Desktop\Akshay\Salary.xlsx", index = False)


# In[ ]:




