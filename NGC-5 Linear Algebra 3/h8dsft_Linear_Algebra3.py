#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 5 - Linear Algebra 3

# In[30]:


import numpy as np


# ---

# Apakah $\begin{bmatrix}1 \\3\end{bmatrix}$ adalah eigenvector dari $\begin{bmatrix}1 & -1\\6 &-4 \end{bmatrix}$? Jika iya, berapakah eigenvalue-nya?

# In[31]:


x = np.array([[1],[3]])
x


# In[32]:


A = np.array([[1, -1],
              [6, -4]])
A


# *Pembuktian secara rumus matematika*

# Karena **Ax** = λ**x**

# In[33]:


A @ x


# Apakah ada nilai λ yang memenuhi $\begin{bmatrix}-2 \\-6\end{bmatrix}$ = λ$\begin{bmatrix}1 \\3\end{bmatrix}$?

# In[34]:


# misalkan
y = np.array([[-2],[-6]])
y


# In[35]:


y / x


# In[36]:


# sehingga diperoleh nilai 
λ = -2


# karena $\begin{bmatrix}-2 \\-6\end{bmatrix}$ = -2 $\begin{bmatrix}1 \\3\end{bmatrix}$

# In[37]:


# atau
x * λ # akan menghasilkan y


# ---

# Sekarang kita mengujinya menggunakan ***numpy.linalg.eig***

# In[38]:


eig_val, eig_vec = np.linalg.eig(A)


# In[39]:


eig_val


# di sini kita memiliki 2 *eigen value*, -1 dan -2

# In[40]:


eig_vec


# Kita akan merekonstruksi matrix A

# In[41]:


# jika -1 dan -2 adalah eigen value maka 
eig_vec @ np.diag(eig_val) @ np.linalg.inv(eig_vec) # akan menghasilkan vektor A


# Sehingga, terbukti bahwa $\begin{bmatrix}1 \\3\end{bmatrix}$ adalah eigen vektor dan eigen valuenya adalah λ = -2 dari vektor $\begin{bmatrix}1 & -1\\6 &-4 \end{bmatrix}$
