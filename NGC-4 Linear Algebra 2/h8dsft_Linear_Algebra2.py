#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 4 - Linear Algebra 2

# In[27]:


import numpy as np


# ---

# Buatlah Tensor dibawah ini dengan Python:
# 
#   $$
#   \begin{bmatrix}   \begin{bmatrix}   23 & 50 \\   7 & 12 \\   \end{bmatrix}   \begin{bmatrix}   57 & 67 \\   99 & 43   \end{bmatrix} \\    \begin{bmatrix}   75 & 21 \\   57 & 12 \\   \end{bmatrix}   \begin{bmatrix}   87 & 26 \\   18 & 84   \end{bmatrix}   \end{bmatrix}
#   $$

# In[28]:


T1 = np.array([[23, 50],
               [7, 12]])
T2 = np.array([[57, 67],
               [99, 43]])
T3 = np.array([[75, 21],
               [57, 12]])
T4 = np.array([[87, 26],
               [18, 84]])
T = np.array([[T1, T2],
              [T3, T4]])
T


# In[29]:


T.shape


# ---

# Lakukan perkalian terhadap matrix berikut:
# 
#   $$
#   A =
#   \begin{bmatrix}
#   23 & 50 & 19 \\
#   7 & 12 & 109 \\
#   57 & 67 & 98
#   \end{bmatrix}
#   \begin{bmatrix}
#   17 \\
#   22 \\
#   19
#   \end{bmatrix}
#   $$

# In[30]:


A = np.array([[23, 50, 19],
              [7, 12, 109],
              [57, 67, 98]])
A


# In[31]:


B = np.array([[17], [22], [19]])
B


# In[32]:


A @ B


# ---

# Lakukan Transpose, hitung determinan, dan inverse terhadap matrix dibawah ini:
# 
#   $$
#   \begin{bmatrix}
#   23 & 50 & 19 \\
#   7 & 12 & 109 \\
#   57 & 67 & 98
#   \end{bmatrix}
#   $$
# 

# In[37]:


A 


# Transpose A

# In[34]:


A.T


# Determinan A

# In[35]:


np.linalg.det(A)


# Inverse A

# In[36]:


np.linalg.inv(A)

