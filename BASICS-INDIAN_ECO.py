#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd          #reading csv files
import numpy as np          # For mathematical calculations 
import matplotlib.pyplot as plt  # For plotting graphs 



df= pd.read_csv(r'C:\Users\olich\OneDrive\Documents\Downloads\INDIAN ECO PROJECT/FINAL_DOW.csv')


# In[3]:


df.head()


# In[4]:


df.describe()


# In[6]:


df.hist()
plt.show()


# In[8]:


df2= pd.read_csv(r'C:\Users\olich\OneDrive\Documents\Downloads\INDIAN ECO PROJECT/nifty.csv')


# In[10]:


df2.head()


# In[9]:


df2.describe()


# In[11]:


df2.hist()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




