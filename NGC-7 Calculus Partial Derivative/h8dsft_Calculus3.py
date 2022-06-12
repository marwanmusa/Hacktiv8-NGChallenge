#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 7 - Calculus Partial Derivative

# In[52]:


import numpy as np
import sympy as sy
import numdifftools as nd
from sympy.tensor.array import derive_by_array


# Find the gradient of:
# $3x+4y=5$

# In[53]:


x = sy.Symbol('x', real = True)
y = sy.Symbol('y', real = True)

# defining x, y as a real symbolic variable 


# if $3x+4y=5$ then $y=(-3/4)x+(5/4)$

# In[54]:


y = -(3/4)*x + (5/4)
y


# ## Using *derive_by_array* by *Sympy*

# In[55]:


print(f'gradient of y: {derive_by_array(y,x)}') 


# ## Using *np.gradient* by *Numpy*

# In[56]:


c = np.linspace(0,20,num = 10)
y1 = -(3/4)*c + (5/4)
ygrad = np.gradient(y1,c)
ygrad


# In[57]:


import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

#x = np.array([5, 4, 1, 4, 5])
#y = np.sort(x)

plt.title("Line graph")
plt.plot(c, ygrad, color="red")

plt.grid()
plt.show()


# For every $x$, the value of gradient $y$ will always be $0.75$

# ## Using *Numdiftools*

# In[58]:


g = lambda x:((-3*x)+ 5)/4
grad1 = nd.Gradient(g)([1])
print("Gradient of (-3^x + 5)/4 ", grad1)

