#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 8 - Calculus Integral

# In[6]:


import sympy as sy


# Carilah integral dari sebuah fungsi:
#   - $\int \! (3x^{2}-6x+3) \, \mathrm{d}x.$
#   - $\int \! (8x^{3}-x^{2}+5x-1) \, \mathrm{d}x.$

# Integral on Code // Symbolic

# In[7]:


x = sy.Symbol('x', real = True)


# In[8]:


f1 = 3*x**2 - 6*x + 3
f2 = 8*x**3 - x**2 + 5*x - 1
print(f'f1 : {f1}')
print(f'f2 : {f2}')


# Integral of $f1$

# In[9]:


sy.integrate(f1)


# Integral of $f2$

# In[10]:


sy.integrate(f2)

