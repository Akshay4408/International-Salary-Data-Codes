#!/usr/bin/env python
# coding: utf-8

# In[81]:



import pandas as pd
import numpy as np


# In[82]:


PF = pd.read_excel(r"C:\Users\3363\Desktop\International\PF.xlsx")
PF.head()


# In[83]:


salary = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Salary.xlsx")
salary.head()


# In[84]:


Report = pd.merge(salary, PF, how='inner',
        left_on='Employee #', right_on='Employee #')
Report


# In[85]:


Report.info()


# In[86]:


Report['PT'] = 200
Report['BASIC'] = Report['Salary Anounce'] / 2
Report['HRA'] = Report['Salary Anounce'] / 4
Report['TOTAL PF'] = Report['BASIC'] * (24/100)
Report['50%'] = Report['TOTAL PF'] * (50/100)
Report['0.75%'] = Report['Salary Anounce'] * (0.75/100)
Report['SALARY PAYABLE'] = Report['Salary Anounce'] - Report['PT'] - Report['50%'] - Report['0.75%']
Report['SALARY PAYABLE Rounded'] = Report['SALARY PAYABLE'].round()

Report.head()


# In[87]:


Result = salary.append(Report)
Result['Index'] = np.arange(len(Result))

Result.head()


# In[88]:




Result = Result.sort_values(["Employee #", "Index"], ascending=True)

Result


# In[89]:


Result = Result.drop_duplicates(
  subset = ['Employee #'],
  keep = 'last').reset_index(drop = True)


Result = Result.fillna('-')

Result.drop(['Index'], axis='columns', inplace=True)
Result


# In[90]:


Result.to_excel(r"C:\Users\3363\Desktop\Akshay\Salary Final.xlsx", index = False)


# In[ ]:




