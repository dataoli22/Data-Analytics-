#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
import numpy as np
import warnings
import itertools
warnings.filterwarnings("ignore")


# In[77]:


df= pd.read_excel(r"C:\Users\olich\OneDrive\Documents\Book1.xlsx")


# In[78]:


df.head()


# In[ ]:





# In[79]:


df.isna()


# In[87]:


df['Arrival (tonn)'].dropna()


# In[91]:


l= df['state_name'].groupby(df['district_name'])


# In[92]:


print(l)


# In[93]:


l.value_counts()


# In[84]:


df.set_index('date_arrival', inplace=True)
df.index = pd.to_datetime(df.index)


# In[94]:


y= df['Arrival (tonn)'].resample('MS').mean()


# In[95]:


print(y)


# In[ ]:





# In[ ]:




