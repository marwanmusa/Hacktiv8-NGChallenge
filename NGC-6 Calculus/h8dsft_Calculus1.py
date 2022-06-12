#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 6 - Calculus

# Carilah derivative dari sebuah fungsi:
#   - $y = x^{2} + 2x + 1$
#   - $y = 4x^{3} - 3x^{2} + 2x -1$

# In[7]:


import sympy as sy


# In[11]:


x = sy.Symbol('x', real = True) # mendefinisikan x sebagai symbolic variabel bernilai real
y = sy.Symbol('y', real = True) # mendefinisikan y sebagai symbolic variabel bernilai real


# Derivative $y = x^{2} + 2x + 1$ terhadap $x$

# In[12]:


y = x**2 + 2*x + 1
y_diff = y.diff(x)
y_diff


# Derivative $y = 4x^{3} - 3x^{2} + 2x -1$ terhadap $x$

# In[13]:


y1 = 4*x**3 - 3*x**2 + 2*x - 1
y1_diff = y1.diff(x)
y1_diff

