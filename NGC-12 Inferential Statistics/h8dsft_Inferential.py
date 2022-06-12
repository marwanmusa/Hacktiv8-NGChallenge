#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 12 - Inferential Statistics

# In[11]:


import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)


# *Import Dataframe*

# In[12]:


df = pd.read_csv('covid_19_indonesia_time_series_all.csv')
df


# In[13]:


df['Date'] = pd.to_datetime(df['Date'])


# In[14]:


df.info()


# Before we do *the Hypothesis Testing*, We will classify the data by its location level first.

# In[15]:


df_country = df[df['Location Level'] == 'Country']
df_country


# In[16]:


df_province = df[df['Location Level'] == 'Province']
df_province


# ## *Single Sample Hypothesis Testing*

# Suppose that during the last 2 years, our country daily new cases of covid-19 is 6600 on average and during the last a year, we reach 6631 a day on average. Is it means that the cases are improved significantly?

# In[17]:


daily_newcases = df_country[['Date','New Cases']].groupby('Date').sum()
print('Average New Cases a Day for the last a year: {}'.format(np.round(daily_newcases['New Cases'].mean())))


# To check whether the case is significantly increase or not, we will perform the single sample one sided and set the significance level of 0.05. We use this method since we only test a variable and compare the sample (last a year data) and the population (we assume it is the last two years data).
# 
# Our hypothesis on this case:
# 
# **H0: μ <= 6600**
# 
# **H1: μ > 6600**

# In[18]:


daily_newcases


# In[20]:


t_stat,p_val = stats.ttest_1samp(daily_newcases['New Cases'], 6600)
print('P-value:',p_val/2) #The p-value divided by 2 since the output is two-sided p-value
print('t-statistics:',t_stat)


# In[21]:


daily_newcases_pop = np.random.normal(daily_newcases['New Cases'].mean(), daily_newcases['New Cases'].std(), 10000)

ci = stats.norm.interval(0.90, daily_newcases['New Cases'].mean(), daily_newcases['New Cases'].std())

plt.figure(figsize=(16,5))
sns.distplot(daily_newcases_pop, label='Daily New Cases (Population)', color='blue')
plt.axvline(daily_newcases['New Cases'].mean(), color='red', linewidth=2, label='Daily New Cases (Mean)')
plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(daily_newcases_pop.mean() + t_stat*daily_newcases_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.legend()


# **Since our p-value is more than `0.05`, so we fail to reject the null hypothesis** and we can conclude that, the cases for the last a year is not significantly improved . 
# 
# *Note: Variable `t-statistics` refers to how far the alternative hypothesis from null hypothesis away.*

# ## *One Sample Two Tailed*

# Our hypothesis on this case:
# 
# **H0: μ = 6600**
# 
# **H1: μ != 6600**

# In[24]:


t_stat,p_val = stats.ttest_1samp(daily_newcases['New Cases'], 6600)
print('P-value:',p_val)
print('t-statistics:',t_stat)


# In[25]:


daily_newcases_pop = np.random.normal(daily_newcases['New Cases'].mean(), daily_newcases['New Cases'].std(), 10000)

ci = stats.norm.interval(0.95, daily_newcases['New Cases'].mean(), daily_newcases['New Cases'].std())

plt.figure(figsize=(16,5))
sns.distplot(daily_newcases_pop, label='Daily New Cases (Population)', color='blue')
plt.axvline(daily_newcases['New Cases'].mean(), color='red', linewidth=2, label='Daily New Cases (Mean)')

plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')

plt.axvline(daily_newcases_pop.mean() + t_stat*daily_newcases_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.axvline(daily_newcases_pop.mean() - t_stat*daily_newcases_pop.std(), color='black', linestyle='dashed', linewidth=2)
plt.legend()


# ## *Two Samples Independent Two Tailed Hypothesis Testing*

# Now, we want to check, whether daily average of New Cases of two province are significantly different or not using two samples independent two tailed test. We will pick sample of Jawa Barat and Jawa Timur.

# In[32]:


daily_jabar = df_province[df_province['Location']=='Jawa Barat'][['Date','New Cases']].groupby('Date').sum()
daily_jatim = df_province[df_province['Location']=='Jawa Timur'][['Date','New Cases']].groupby('Date').sum()

print('Average new cases of Jawa Barat a day: {}'.format(np.round(daily_jabar['New Cases'].mean())))
print('Average new cases of Jawa Timur a day: {}'.format(np.round(daily_jatim['New Cases'].mean())))


# Our hypothesis on this case:
# 
# **H0: μ_jabar = μ_jatim**
# 
# **H1: μ_jabar != μ_jatim**

# In[39]:


t_stat, p_val = stats.ttest_ind(daily_jabar, daily_jatim)
print('P-value:',p_val[0]) #the p-value isn't divided by 2 since the output is two-sided p-value
print('t-statistics:',t_stat[0])


# In[44]:


jabar_pop = np.random.normal(daily_jabar['New Cases'].mean(),daily_jabar['New Cases'].std(),10000)
jatim_pop = np.random.normal(daily_jatim['New Cases'].mean(),daily_jatim['New Cases'].std(),10000)

ci = stats.norm.interval(0.95, daily_jabar['New Cases'].mean(), daily_jabar['New Cases'].std())
plt.figure(figsize=(16,5))
sns.distplot(jabar_pop, label='Jawa Barat Average New Cases a Day *Pop',color='blue')
sns.distplot(jatim_pop, label='Jawa Timur Average New Cases a Day *Pop',color='red')

plt.axvline(daily_jabar['New Cases'].mean(), color='blue', linewidth=2, label='Jawa Barat mean')
plt.axvline(daily_jatim['New Cases'].mean(), color='red',  linewidth=2, label='Jawa Timur mean')

plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

plt.axvline(jabar_pop.mean()+t_stat[0]*jabar_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.axvline(jabar_pop.mean()-t_stat[0]*jabar_pop.std(), color='black', linestyle='dashed', linewidth=2)

plt.legend()


# Based on the result above, we can conclude that **we reject the null hypothesis** which between Jawa Barat and Jawa Timur are significantly different in terms of average new cases per day.

# ## *ANOVA*

# ANOVA is similar to the t-test. It used for testing whether more than two variables are significantly different or not. So, we will test whether the mean of daily new cases of Sumatera Selatan, Kalimantan Selatan, and Sulawesi Selatan are significantly different or not.

# In[53]:


sumsel_newcases = df_province[df_province['Location'] == 'Sumatera Selatan'].groupby('Date').sum()['New Cases']
kalsel_newcases = df_province[df_province['Location'] == 'Kalimantan Selatan'].groupby('Date').sum()['New Cases']
sulsel_newcases = df_province[df_province['Location'] == 'Sulawesi Selatan'].groupby('Date').sum()['New Cases']

print("Daily Average of Sumatera Selatan",sumsel_newcases.mean())
print("Daily Average of Kalimantan Selatan",kalsel_newcases.mean())
print("Daily Average of Sulawesi Selatan",sulsel_newcases.mean())


# It seems that they are significantly different since `Sumatera Selatan` average is `96`, `Kalimantan Selatan` average is `114` and `Sulawesi Selatan` average is `176`.

# In[54]:


f_stat,p_value = stats.f_oneway(sumsel_newcases, kalsel_newcases, sulsel_newcases)
print('P-value:',p_value)


# **Since the p-value is below 0.05, then we reject the Null Hypothesis.** We conclude that the difference of Sumatra Selatan, Kalimantan Selatan, and Sulawesi Selatan daily new cases is statistically significant.
