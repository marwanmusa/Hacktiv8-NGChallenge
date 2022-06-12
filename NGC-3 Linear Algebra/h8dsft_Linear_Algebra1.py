#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 3 - Linear Algebra

# In[24]:


import numpy as np
import matplotlib.pyplot as plt


# 1. Buatlah Vector dibawah ini dengan Python:
# 
#   $$
#   \begin{bmatrix}
#   17 \\
#   22 \\
#   19
#   \end{bmatrix}
#   $$

# In[25]:


np.array([17, 22, 19])


# 2. Diberikan 3 buah vektor 3 dimensi:
# $$
# A=
# \begin{bmatrix}
# 17 \\
# 22 \\
# 19
# \end{bmatrix}
# ,B=
# \begin{bmatrix}
# 10 \\
# 20 \\
# 11
# \end{bmatrix},
# C=
# \begin{bmatrix}
# 5 \\
# 12 \\
# 9
# \end{bmatrix}
# $$
# 
# Hitunglah:
#   - A+B
#   - B-C
#   - A dot C
#   - A x B
#   - norm A
#   - Sudut antara vektor A dan B

# In[26]:


A = np.array([17, 22, 19])
B = np.array([10, 20, 11])
C = np.array([5, 12, 9])
print(A)
print(B)
print(C)


# A + B

# In[27]:


A + B


# B - C

# In[28]:


B - C


# A dot C

# In[29]:


A @ C


# In[30]:


# or
np.dot(A, C)


# A x B

# In[31]:


A * B


# Norm A

# In[40]:


np.linalg.norm(A)


# Sudut antara vektor A dan B

# In[33]:


cos_theta = A @ B / (np.linalg.norm(A) * np.linalg.norm(B))
cos_theta


# In[34]:


# convert cos_theta to radian
rad = np.arccos(cos_theta)
rad


# In[35]:


# convert radian to degree
deg = np.degrees(rad)
deg


# *jadi, sudut yang terbentuk antara A dan B adalah 12.6 derajat.*

# Buatlah plot dari vector berikut ini kedalam bidang 2D:
# 
#   $$
#   U =
#   \begin{bmatrix}
#   2 \\ 5
#   \end{bmatrix},
#   V =
#   \begin{bmatrix}
#   3 \\ 1
#   \end{bmatrix}
#   $$

# In[36]:


# Vector U
U = np.array([2, 5])
U


# In[37]:


# Vector V
V = np.array([3, 1])
V


# Membuat fungsi plot2d

# In[38]:


def plot_vector2d(vector2d, origin=[0, 0], **options):
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
              head_width=0.2, head_length=0.3, length_includes_head=True,
              **options)


# In[39]:


plot_vector2d(U, color='r')
plot_vector2d(V, color='g')

plt.axis([0,6,0,6]) # rentang axis sumbu x dan y
plt.grid()
plt.show()

