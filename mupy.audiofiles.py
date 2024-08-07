#!/usr/bin/env python
# coding: utf-8

# In[34]:


from scipy.io import wavfile
from IPython.display import Audio
from matplotlib import pyplot as plt
import numpy as np





# In[35]:


import os.path #use os.path to import a wavfile when you use mac
sample =  os.path.expanduser('/Users/benutzer/Desktop/audiobeispiel.wav')
    
samplerate, data = wavfile.read(sample) 


# In[36]:


plt.xlabel('samples') #use plt.label to label the x or y axes
plt.ylabel('Amplitude')
plt.xlim #use lim to zoom
plt.plot(data)


# In[37]:


Audio(sample)


# In[21]:


print(samplerate)


# In[26]:


samplerate, data = wavfile.read(sample)
print(f'number of samples :{data.shape[0]}' )
print(f'number of channels : {data.shape[1]}')
length = data.shape[0] / samplerate
print(f'length = {length}s')


# <h2> sample rate </h2>

# In[84]:


import matplotlib.image as mpimg


# In[85]:



img = mpimg.imread('/Users/benutzer/Downloads/80ffde40a1da-Increasing-bit-depth-resolution.png')
imgplot = plt.imshow(img)
plt.show()

# In[8]:





# In[12]:















