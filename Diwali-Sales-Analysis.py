#!/usr/bin/env python
# coding: utf-8

# # DIWALI SALE ANALYSIS 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #data visualization
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('Diwali Sales Data.csv',  encoding = 'unicode_escape')
#to avoid any encoding error using unicode_escape


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


#dropping blank columns
df.drop(['Status','unnamed1'], axis = 1, inplace = True)


# In[9]:


df.head()


# In[10]:


#finding null value
df.isnull().sum()


# In[11]:


#dropping null values
df.dropna(inplace = True)


# In[12]:


df.shape


# In[13]:


#changing datatype 
df['Amount'] = df['Amount'].astype('int64')


# In[14]:


df.dtypes


# In[15]:


[df.dtypes == 'int64']


# In[16]:


df[['Age','Orders','Amount']].describe()


# ## EDA (EXPLORATORY DATA ANALYSIS)

# #### GENDER

# In[17]:


df.columns


# In[18]:


ax = sns.countplot(x ='Gender', data = df)
#for adding the bar values

for i in ax.containers:
    ax.bar_label(i)
    


# In[19]:


sales_inf = df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by = 'Amount', ascending = False)
sns.barplot(data = sales_inf, x = 'Gender', y = 'Amount')


# **From above graphs we can see that most of the buyers are female as well as the amount spent by the females are also higher then the males.**

# ### AGE

# In[20]:


df.columns


# In[21]:


bx = sns.countplot( data = df, x = 'Age Group', hue = 'Gender')

for i in bx.containers:
    bx.bar_label(i)


# In[22]:


#total amount vs age
sales_age = df.groupby(['Age Group'], as_index= False)['Amount'].sum().sort_values( by = 'Amount',ascending = False)

sns.barplot(data = sales_age, x ='Age Group', y = 'Amount')


# **From above graphs we can see that most of the buyers are of age group between 26-35 yrs female**

# ### STATE

# In[23]:


df.columns


# In[24]:


sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.set(rc={'figure.figsize' : (15,5)})
sns.barplot(data = sales_state, x='State', y ='Orders')


# In[25]:


sales_state = df.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.set(rc={'figure.figsize' : (15,5)})
sns.barplot(data = sales_state, x='State', y ='Amount')


# **Frome above graphs we can see that the maximum orders are from Uttar Pradesh, Maharastra, Karnataka respectively.**

# ### MARITAL STATUS

# In[26]:


df.columns


# In[27]:


sales_mstatus = df.groupby(['Marital_Status','Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.set(rc={'figure.figsize' : (8,5)})
sns.barplot(data =  sales_mstatus, x= 'Marital_Status', y ='Amount', hue='Gender')


# In[28]:


ax = sns.countplot(x ='Marital_Status', data = df)
#for adding the bar values
sns.set(rc={'figure.figsize' : (8,5)})
for i in ax.containers:
    ax.bar_label(i)


# **From above graphs we can see that most of the buyers are married (women) and they have high purchasing power**

# ### OCCUPATION

# In[29]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# **From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector**

# ### PRODUCT CATEGORY

# In[31]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# **From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category**

# In[33]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[34]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## CONCLUSION

# **Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category**

# THANK YOU
