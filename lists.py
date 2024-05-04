#!/usr/bin/env python
# coding: utf-8

# <h1> create a list </h1>

# In[38]:


instrument1 = 'flute' #list of strings
instrument2 = 'piano'
instrument3 = 'drums'
instrument4 = 'trombone'


# In[39]:


instruments = [instrument1, instrument2, instrument3, instrument4]


# In[18]:


numb = [1,2,6,4,8,14,8] #list of numbers


# In[14]:


let = ['a','g','r','e','h','f'] #list of letters


# In[6]:


mix = [1,4,'l','r','train','bus'] #list of mixed data types


# In[19]:


numb


# In[ ]:


let


# In[ ]:


mix


# <h2> append and remove data from a list </h2>

# To create a list you have to use square brackets. If you use normal brackets, you will create a tuple. 
# The difference is that it's not possible to change the data in a tuple.

# In[41]:


instruments.append('guitar') 
instruments


# In[78]:


let.remove('b')
let


# In[6]:


numb.append(2)


# In[10]:


numb.remove(2)
numb


# In[ ]:


numb.clear() #clear the list with 'listname.clear' and add () without an argument


# In[11]:


numb


# In[ ]:


type(numb)


# In[29]:


numb.insert(2, 3) #insert a variable in any point of the list. 
                #1. variable in the list 2. variable you want to insert


# In[62]:


del(numb[3])


# In[77]:


numb.pop(3) #.pop deletes the variable and shows wich variable was deleted


# In[78]:


numb


# In[80]:


let.remove('a')


# <h2> access data in a list </h2>

# In[46]:


numb


# In[47]:


numb.count(8) #count shows you the amount of one specific number, string, float, etc. in a list


# In[15]:


let


# In[51]:


let[3]


# In[53]:


let[0:4]


# In[54]:


let.index('f')


# In[23]:


numb.sort()


# In[25]:


numb.reverse()


# In[26]:


numb


# In[2]:


import numpy as np


# In[29]:


numb2 = ([4,5,6],[7,8,9])


# In[30]:


np.asarray(numb2)


# In[9]:


np.asarray(mix)


# In[ ]:





# %%

# %%

# %%
