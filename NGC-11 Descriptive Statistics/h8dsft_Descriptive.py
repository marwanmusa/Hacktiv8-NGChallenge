#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 11 - Descriptive Statistics

# In[180]:


import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt


# In[181]:


df = pd.read_csv('covid_19_indonesia_time_series_all.csv')


# In[182]:


df


# In[183]:


df.info()


# Before we start to measure *the central tendency and the variance* of the data, We will classify the data by its location level first.

# In[184]:


df_country = df[df['Location Level'] == 'Country']
df_country


# In[185]:


df_province = df[df['Location Level'] == 'Province']
df_province


# ## Measure of Central Tendency Data

# Mathematically central tendency means measuring the center or distribution of location of values of a data set. It gives an idea of the average value of the data in the data set and also an indication of how widely the values are spread in the data set. That in turn helps in evaluating the chances of a new input fitting into the existing data set and hence probability of success.
# 
# There are three main measures of central tendency which can be calculated using the methods in pandas python library.
# - Mean - It is the Average value of the data which is a division of sum of the values with the number of values.
# - Median - It is the middle value in distribution when the values are arranged in ascending or descending order.
# - Mode - It is the most commonly occurring value in a distribution.

# ### *Mean* 

# **This is calculated as the sum of the values in the dataset, divided by the number of observations in the dataset.** When the dataset consists of the full population, the mean is represented by the Greek symbol ***&mu;*** (*mu*), and the formula is written like this:
# 
# $$
# \begin{equation}\mu = \frac{\displaystyle\sum_{i=1}^{N}X_{i}}{N}\end{equation}
# $$

# We will calculate the mean of *Total Cases, Total Deaths, Total Recovered, Total Active Cases*.

# **Country Data**

# In[186]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' mean ' + str(df_country[col].mean()))


# **Provinces Data**

# In[187]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' mean ' + str(df_province[col].mean()))


# ### *Median*

# **To calculate the median, we need to sort the values into ascending order and then find the middle-most value.** When there are an odd number of observations, you can find the position of the median value using this formula (where *n* is the number of observations):
# 
# $$
# \begin{equation}\frac{n+1}{2}\end{equation}
# $$

# **Country Data**

# In[188]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' median ' + str(df_country[col].median()))


# **Provinces Data**

# In[189]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' median ' + str(df_province[col].median()))


# ### *Mode*

# Another related statistic is the mode, which indicates the most frequently occurring value. If you think about it, this is potentially a good indicator of how much a student might expect to earn when they graduate from the school; out of all the salaries that are being earned by former students, the mode is earned by more than any other.

# **Country Data**

# In[190]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' mode ' + str(df_country[col].mode()))


# **Provinces Data**

# In[191]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' mode ' + str(df_province[col].mode()))


# ---

# ## Measure of Variance Data

# We can see from the distribution plots of our data that the values in our dataset can vary quite widely. We can use various measures to quantify this variance.

# ### *Range*

# A simple way to quantify the variance in a dataset is to identify the **difference between the lowest and highest values**. This is called the range, and is calculated by **subtracting the minimim value from the maximum value**.

# **Country Data**

# In[192]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' range: ' + str(df_country[col].max() - df_country[col].min()))


# **Provinces Data**

# In[193]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' range: ' + str(df_province[col].max() - df_province[col].min()))


# ### *Percentiles and Quartiles*

# The range is easy to calculate, but it's not a particularly useful statistic. For example, a range of 4257241 between the lowest and highest total cases does not tell us which value within that range a case is most likely a lot - it doesn't tell us nothing about how the cases are distributed around the mean within that range.

# #### Percentiles

# A percentile tells us where a given value is ranked in the overall distribution. For example, 25% of the data in a distribution has a value lower than the 25th percentile; 75% of the data has a value lower than the 75th percentile, and so on. Note that half of the data has a value lower than the 50th percentile - so the 50th percentile is also the median!

# In[194]:


print(stats.percentileofscore(df_country['New Cases'], df_country['New Cases'].mean(), 'strict'))


# So this mean of new cases is at the 73.9th percentile of total new case data.

# #### Quartile

# Rather than using individual percentiles to compare data, we can consider the overall spread of the data by dividing those percentiles into four quartiles. The first quartile contains the values from the minimum to the 25th percentile, the second from the 25th percentile to the 50th percentile (which is the median), the third from the 50th percentile to the 75th percentile, and the fourth from the 75th percentile to the maximum.

# **Country Data**

# In[195]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print('Country ' + df_country[col].name + ' quartile:\n' + str(df_country[col].quantile([0.25, 0.5, 0.75])))


# **Provinces Data**

# In[196]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print('All Provinces ' + df_province[col].name + ' quartile:\n' + str(df_province[col].quantile([0.25, 0.5, 0.75])))


# ### *Box Plot & Outliers*

# **An outlier is a value that is so far from the center of the distribution compared to other values that it skews the distribution by affecting the mean.** There are all sorts of reasons that you might have outliers in your data, including data entry errors, failures in sensors or data-generating equipment, or genuinely anomalous values.

# Its usually easier to understand how data is distributed across the quartiles by visualizing it. We can use a histogram, but many data scientists use a kind of visualization called a box plot (or a box and whiskers plot).

# **Country Data**

# In[197]:


# Plot a box-whisker chart
numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    df_country[col].plot(kind='box', title= col + ' Distribution', figsize=(10,8))
    plt.show()


# **Provinces Data**

# In[198]:


# Plot a box-whisker chart
numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    df_province[col].plot(kind='box', title= col + ' Distribution', figsize=(10,8))
    plt.show()


# The box plot consists of:
# - A rectangular *box* that shows where the data between the 25th and 75th percentile (the second and third quartile) lie. This part of the distribution is often referred to as the *interquartile range* - it contains the middle 50 data values.
# - *Whiskers* that extend from the box to the bottom of the first quartile and the top of the fourth quartile to show the full range of the data.
# - A line in the box that shows that location of the median (the 50th percentile, which is also the threshold between the second and third quartile)

# ### *Variance and Standard Deviation*
# We've seen how to understand the *spread* of our data distribution using the range, percentiles, and quartiles; and we've seen the effect of outliers on the distribution. Now it's time to look at how to measure the amount of variance in the data.

# #### Variance

# Variance is measured as the average of the squared difference from the mean. For a full population, it's indicated by a squared Greek letter *sigma* (***&sigma;<sup>2</sup>***) and calculated like this:
# 
# $$
# \begin{equation}\sigma^{2} = \frac{\displaystyle\sum_{i=1}^{N} (X_{i} -\mu)^{2}}{N}\end{equation}
# $$
# 
# For a sample, it's indicated as ***s<sup>2</sup>*** calculated like this:
# 
# $$
# \begin{equation}s^{2} = \frac{\displaystyle\sum_{i=1}^{n} (x_{i} -\bar{x})^{2}}{n-1}\end{equation}
# $$
# 
# In both cases, we sum the difference between the individual data values and the mean and square the result. Then, for a full population we just divide by the number of data items to get the average. When using a sample, we divide by the total number of items **minus 1** to correct for sample bias.

# **Country Data**

# In[199]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' variance ' + str(df_country[col].var()))


# **Provinces Data**

# In[200]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' variance ' + str(df_province[col].var()))


# #### Standard Deviation

# To calculate the variance, we squared the difference of each value from the mean. If we hadn't done this, the numerator of our fraction would always end up being zero (because the mean is at the center of our values). However, this means that the variance is not in the same unit of measurement as our data - in our case, since we're calculating the variance for New Cases, New Deaths, etc., it's in number of cases squared; which is not very helpful.
# 
# To get the measure of variance back into the same unit of measurement, we need to find its square root:
# 
# $$
# \begin{equation}s = \sqrt{91317496} \approx 9556\end{equation}
# $$
# 
# So what does this value represent?
# 
# It's the *standard deviation* for our grades data. More formally, it's calculated like this for a full population:
# 
# $$
# \begin{equation}\sigma = \sqrt{\frac{\displaystyle\sum_{i=1}^{N} (X_{i} -\mu)^{2}}{N}}\end{equation}
# $$
# 
# Or like this for a sample:
# 
# $$
# \begin{equation}s = \sqrt{\frac{\displaystyle\sum_{i=1}^{n} (x_{i} -\bar{x})^{2}}{n-1}}\end{equation}
# $$
# 
# Note that in both cases, it's just the square root of the corresponding variance forumla!

# **Country Data**

# In[201]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_country[col].name + ' standard deviation ' + str(df_country[col].std()))


# **Provinces Data**

# In[202]:


numcols = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases']
for col in numcols:
    print(df_province[col].name + ' standard deviation ' + str(df_province[col].std()))

