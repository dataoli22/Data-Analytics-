#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
from pandas.plotting import scatter_matrix
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import StratifiedKFold





# In[13]:


#loading the dataset
url= "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names= ['sepal-length','sepal-width', 'petal-length', 'class']
dataset= read_csv(url, names=names)


# In[14]:


#dimesnions of the dataset
print(dataset.shape)


# In[15]:


#the first few sets
print(dataset.head(20))


# In[16]:


#statistical summary
print(dataset.describe())


# In[17]:


#classdistribution
print(dataset.groupby('class').size())


# In[18]:


#univariate-plots- box and whisker plots
dataset.plot(kind='box', subplots= True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()


# In[20]:


#histogram of the variable
dataset.hist()
pyplot.show()


# In[21]:


#multivariate plots
scatter_matrix(dataset)
pyplot.show()


# In[24]:


#creating a validation dataset
#splitting dataset
array= dataset.values
X= array[:, 0:3]
y= array[:,3]
X_train, X_validation, y_train, y_validation= train_test_split(X,y, test_size= 0.2, random_state=1 )


# In[33]:


#logistic regression
#linear discriminant analysis
#k-nearest neighbors
#classification and regression trees
#gaussian naive bayes
#support vector machines

#building models
models= []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
              


# In[38]:


#evaluate the created models
results= []
names= []
for name, model in models:
    kfold= StratifiedKFold(n_splits=10, shuffle=True)
    cv_results= cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
    
    
    


# In[39]:


#compare our models
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()


# In[44]:


#make predictions on svm
model= SVC(gamma= 'auto')
model.fit(X_train, y_train)
predictions= model.predict(X_validation)


# In[47]:


#evaluate our predictions
print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))


# In[ ]:




