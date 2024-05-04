#!/usr/bin/env python
# coding: utf-8

# In[145]:


import numpy as np


# In[295]:


liste = np.array([1,2,3,4,5,6,7,8])
arr2 = np.asarray([[1,2,3],[5,6,7],[8,9,11]])
arr3 = np.array ([[1,2,5,1],[3,2,1,6],[7,5,3,7],[1,5,7,5],[1,4,4,6]])

print(liste)
print(arr2)
print(arr3)


# In[141]:


print(type(liste))


# In[297]:


print(arr2[ 1, 0])


# In[ ]:


np.ones([5,6])


# In[ ]:


np.zeros([5,6,7])


# In[ ]:


np.empty(1)


# In[ ]:


np.empty(5)


# In[ ]:


np.ndim(arr2)


# In[ ]:


np.ndim([5,6,7])


# In[ ]:


np.transpose(art)


# In[21]:


np.arange(-30.2, 30.4, 10) #use arange when step size between the values is important


# In[20]:


np.linspace(-30.2, 30.4, 10) #use linspace when the exact values when the start and end point are important


# <h2> export a list/an array into a CSV file </h2>

# In[189]:


from numpy import genfromtxt


# In[190]:


liste.tofile('eine.liste', sep = ',') #converting a list into a csv file


# In[211]:


my_data = genfromtxt('eine.liste', delimiter=",") #import a csv file 


# In[212]:


print(my_data)


# In[288]:


np.savetxt('ein.array.csv', arr2, fmt="%d", delimiter=",") #1. the name of the file
                                                            #2. the name of the array
                                                            #3. fmt = format of the data
                                                            #4. delimiter = define the space between data(only necessary if you don't open it as an array)
                                                            


# In[289]:


arrayfile = genfromtxt('ein.array.csv', delimiter=",")


# In[290]:


print(arrayfile)


# In[291]:


type(my_data)


# In[306]:


import pandas as pd

anderefile = pd.read_csv('ein.array.csv')


# In[307]:


print(anderefile)


# In[301]:


type(anderefile)


# In[ ]:




