#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 10 - Probability

# Buatlah sebuah kode untuk mensimulasikan melempar koin sebanyak 50.000 kali dengan assign value random berupa 0 dan 1 untuk kepala atau ekor. Setiap kali koin dilempar, peluang untuk mendapatkan kepala atau ekor adalah 50%.

# In[1]:


import random
from matplotlib import pyplot as plt


# In[2]:


# Create a list with 2 element (for heads and tails)
heads_tails = [0,0]


# In[8]:


# loop through 50000 trials
trials = 50000
trial = 0
while trial < trials:
    trial = trial + 1
    # Get a random 0 or 1
    toss = random.randint(0,1)
    # Increment the list element corresponding to the toss result
    heads_tails[toss] = heads_tails[toss] + 1 


# In[6]:


print (heads_tails)


# In[7]:


# Show a pie chart of the results
plt.figure(figsize=(5,5))
plt.pie(heads_tails, labels=['heads', 'tails'])
plt.legend()
plt.show()

