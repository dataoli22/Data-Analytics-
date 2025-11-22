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


# In[12]:


#Histogram
plt.hist(df, bins=50);

#Mean
mean = np.mean(df)
print(mean)

#Median
median = np.median(df)
print(median)

#Skewness Graph

xs = np.linspace(df.min(), df.max(), 100)

ys1 = st.norm.pdf(xs, loc=mean)

ps = st.skewnorm.fit(df) 

ys2 = st.skewnorm.pdf(xs, *ps)

plt.hist(df, bins=50, density=True, histtype="step", label="Data")

plt.plot(xs, ys1, label="Normal approximation")

plt.plot(xs, ys2, label="Skewnormal approximation")

plt.legend()

plt.ylabel("Probability");

skewness = st.skew(df)
print(skewness)

#Kurtosis

kurtosis = st.kurtosis(df, fisher=False)
print(kurtosis)


# In[ ]:




