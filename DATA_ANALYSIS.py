#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as st


df= pd.read_excel('OneDrive/Documents/Downloads/Programming/case_study/daymin_daycall.xlsx')
                  


# In[11]:


print (df)


# In[18]:


df.groupby('510').mean()


# In[16]:


plt.hist(df)


# In[ ]:




