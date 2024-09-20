#!/usr/bin/env python
# coding: utf-8

# <h2>Quadratic Regression Dataset - Linear Regression vs XGBoost</h2>
# 
# Model is trained with XGBoost installed in notebook instance
# 
# In the later examples, we will train using SageMaker's XGBoost algorithm.
# 
# Training on SageMaker takes several minutes (even for simple dataset).  
# 
# If algorithm is supported on Python, we will try them locally on notebook instance
# 
# This allows us to quickly learn an algorithm, understand tuning options and then finally train on SageMaker Cloud
# 
# In this exercise, let's compare XGBoost and Linear Regression for Quadratic regression dataset

# In[1]:


# Install xgboost in notebook instance.
#### Command to install xgboost
get_ipython().system('pip install xgboost==1.2')


# In[2]:


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error


# XGBoost 
import xgboost as xgb
# Linear Regression
from sklearn.linear_model import LinearRegression


# In[3]:


df = pd.read_csv('quadratic_all.csv')


# In[4]:


df.head()


# In[5]:


plt.plot(df.x,df.y,label='Target')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.legend()
plt.title('Quadratic Regression Dataset')
plt.show()


# In[6]:


train_file = 'quadratic_train.csv'
validation_file = 'quadratic_validation.csv'

# Specify the column names as the file does not have column header
df_train = pd.read_csv(train_file,names=['y','x'])
df_validation = pd.read_csv(validation_file,names=['y','x'])


# In[7]:


df_train.head()


# In[8]:


df_validation.head()


# In[9]:


plt.scatter(df_train.x,df_train.y,label='Training',marker='.')
plt.scatter(df_validation.x,df_validation.y,label='Validation',marker='.')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.title('Quadratic Regression Dataset')
plt.legend()
plt.show()


# In[10]:


X_train = df_train.iloc[:,1:] # Features: 1st column onwards 
y_train = df_train.iloc[:,0].ravel() # Target: 0th column

X_validation = df_validation.iloc[:,1:]
y_validation = df_validation.iloc[:,0].ravel()


# In[11]:


# Create an instance of XGBoost Regressor
# XGBoost Training Parameter Reference: 
#   https://github.com/dmlc/xgboost/blob/master/doc/parameter.md
regressor = xgb.XGBRegressor()


# In[12]:


regressor


# In[13]:


regressor.fit(X_train,y_train, eval_set = [(X_train, y_train), (X_validation, y_validation)])


# In[14]:


eval_result = regressor.evals_result()


# In[15]:


training_rounds = range(len(eval_result['validation_0']['rmse']))


# In[16]:


plt.scatter(x=training_rounds,y=eval_result['validation_0']['rmse'],label='Training Error')
plt.scatter(x=training_rounds,y=eval_result['validation_1']['rmse'],label='Validation Error')
plt.grid(True)
plt.xlabel('Iteration')
plt.ylabel('RMSE')
plt.title('Training Vs Validation Error')
plt.legend()
plt.show()


# In[17]:


xgb.plot_importance(regressor)
plt.show()


# ## Validation Dataset Compare Actual and Predicted

# In[18]:


result = regressor.predict(X_validation)


# In[19]:


result[:5]


# In[20]:


plt.title('XGBoost - Validation Dataset')
plt.scatter(df_validation.x,df_validation.y,label='actual',marker='.')
plt.scatter(df_validation.x,result,label='predicted',marker='.')
plt.grid(True)
plt.legend()
plt.show()


# In[21]:


# RMSE Metrics
print('XGBoost Algorithm Metrics')
mse = mean_squared_error(df_validation.y,result)
print(" Mean Squared Error: {0:.2f}".format(mse))
print(" Root Mean Square Error: {0:.2f}".format(mse**.5))


# In[22]:


# Residual
# Over prediction and Under Prediction needs to be balanced
# Training Data Residuals
residuals = df_validation.y - result
plt.hist(residuals)
plt.grid(True)
plt.xlabel('Actual - Predicted')
plt.ylabel('Count')
plt.title('XGBoost Residual')
plt.axvline(color='r')
plt.show()


# In[23]:


# Count number of values greater than zero and less than zero
value_counts = (residuals > 0).value_counts(sort=False)

print(' Under Estimation: {0}'.format(value_counts[True]))
print(' Over  Estimation: {0}'.format(value_counts[False]))


# In[24]:


# Plot for entire dataset
plt.plot(df.x,df.y,label='Target')
plt.plot(df.x,regressor.predict(df[['x']]) ,label='Predicted')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.legend()
plt.title('XGBoost')
plt.show()


# ## Linear Regression Algorithm

# In[24]:


lin_regressor = LinearRegression()


# In[25]:


lin_regressor.fit(X_train,y_train)


# Compare Weights assigned by Linear Regression.
# 
# Original Function: 5*x**2 -23*x + 47 + some noise
# 
# Linear Regression Function: -15.08 * x + 709.86 
# 
# Linear Regression Coefficients and Intercepts are not close to actual

# In[26]:


lin_regressor.coef_


# In[27]:


lin_regressor.intercept_


# In[28]:


result = lin_regressor.predict(df_validation[['x']])


# In[29]:


plt.title('LinearRegression - Validation Dataset')
plt.scatter(df_validation.x,df_validation.y,label='actual',marker='.')
plt.scatter(df_validation.x,result,label='predicted',marker='.')
plt.grid(True)
plt.legend()
plt.show()


# In[30]:


# RMSE Metrics
print('Linear Regression Metrics')
mse = mean_squared_error(df_validation.y,result)
print(" Mean Squared Error: {0:.2f}".format(mse))
print(" Root Mean Square Error: {0:.2f}".format(mse**.5))


# In[31]:


# Residual
# Over prediction and Under Prediction needs to be balanced
# Training Data Residuals
residuals = df_validation.y - result
plt.hist(residuals)
plt.grid(True)
plt.xlabel('Actual - Predicted')
plt.ylabel('Count')
plt.title('Linear Regression Residual')
plt.axvline(color='r')
plt.show()


# In[32]:


# Count number of values greater than zero and less than zero
value_counts = (residuals > 0).value_counts(sort=False)

print(' Under Estimation: {0}'.format(value_counts[True]))
print(' Over  Estimation: {0}'.format(value_counts[False]))


# In[33]:


# Plot for entire dataset
plt.plot(df.x,df.y,label='Target')
plt.plot(df.x,lin_regressor.predict(df[['x']]) ,label='Predicted')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.legend()
plt.title('LinearRegression')
plt.show()


# Linear Regression is showing clear symptoms of under-fitting
# 
# Input Features are not sufficient to capture complex relationship

# <h2>Your Turn</h2>
# You can correct this under-fitting issue by adding relavant features.
# 
# 1. What feature will you add and why?
# 2. Complete the code and Test
# 3. What performance do you see now?

# In[34]:


# Specify the column names as the file does not have column header
df_train = pd.read_csv(train_file,names=['y','x'])
df_validation = pd.read_csv(validation_file,names=['y','x'])
df = pd.read_csv('quadratic_all.csv')


# # Add new features 

# In[36]:


# Place holder to add new features to df_train, df_validation and df
# if you need help, scroll down to see the answer
# Add your code


# In[37]:


X_train = df_train.iloc[:,1:] # Features: 1st column onwards 
y_train = df_train.iloc[:,0].ravel() # Target: 0th column

X_validation = df_validation.iloc[:,1:]
y_validation = df_validation.iloc[:,0].ravel()


# In[38]:


lin_regressor.fit(X_train,y_train)


# Original Function: -23*x + 5*x**2 + 47 + some noise (rewritten with x term first)

# In[39]:


lin_regressor.coef_


# In[40]:


lin_regressor.intercept_


# In[41]:


result = lin_regressor.predict(X_validation)


# In[42]:


plt.title('LinearRegression - Validation Dataset')
plt.scatter(df_validation.x,df_validation.y,label='actual',marker='.')
plt.scatter(df_validation.x,result,label='predicted',marker='.')
plt.grid(True)
plt.legend()
plt.show()


# In[43]:


# RMSE Metrics
print('Linear Regression Metrics')
mse = mean_squared_error(df_validation.y,result)
print(" Mean Squared Error: {0:.2f}".format(mse))
print(" Root Mean Square Error: {0:.2f}".format(mse**.5))

print("***You should see an RMSE score of 30.45 or less")


# In[44]:


df.head()


# In[45]:


# Plot for entire dataset
plt.plot(df.x,df.y,label='Target')
plt.plot(df.x,lin_regressor.predict(df[['x','x2']]) ,label='Predicted')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.legend()
plt.title('LinearRegression')
plt.show()


# ## Solution for under-fitting
# 
# add a new X**2 term to the dataframe
# 
# syntax:
# 
# df_train['x2'] = df_train['x']**2
# 
# df_validation['x2'] = df_validation['x']**2
# 
# df['x2'] = df['x']**2

# ### Tree Based Algorithms have a lower bound and upper bound for predicted values

# In[46]:


# True Function
def quad_func (x):
    return 5*x**2 -23*x + 47


# In[47]:


# X is outside range of training samples
# New Feature: Adding X^2 term

X = np.array([-100,-25,25,1000,5000])
y = quad_func(X)
df_tmp = pd.DataFrame({'x':X,'y':y,'x2':X**2})
df_tmp['xgboost']=regressor.predict(df_tmp[['x']])
df_tmp['linear']=lin_regressor.predict(df_tmp[['x','x2']])


# In[48]:


df_tmp


# In[49]:


plt.scatter(df_tmp.x,df_tmp.y,label='Actual',color='r')
plt.plot(df_tmp.x,df_tmp.linear,label='LinearRegression')
plt.plot(df_tmp.x,df_tmp.xgboost,label='XGBoost')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Input Outside Range')
plt.show()


# In[50]:


# X is inside range of training samples
X = np.array([-15,-12,-5,0,1,3,5,7,9,11,15,18])
y = quad_func(X)
df_tmp = pd.DataFrame({'x':X,'y':y,'x2':X**2})
df_tmp['xgboost']=regressor.predict(df_tmp[['x']])
df_tmp['linear']=lin_regressor.predict(df_tmp[['x','x2']])


# In[51]:


df_tmp


# In[52]:


# XGBoost Predictions have an upper bound and lower bound
# Linear Regression Extrapolates
plt.scatter(df_tmp.x,df_tmp.y,label='Actual',color='r')
plt.plot(df_tmp.x,df_tmp.linear,label='LinearRegression')
plt.plot(df_tmp.x,df_tmp.xgboost,label='XGBoost')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Input within range')
plt.show()


# <h2>Summary</h2>

# 1. In this exercise, we compared performance of XGBoost model and Linear Regression on a quadratic dataset
# 2. The relationship between input feature and target was non-linear.
# 3. XGBoost handled it pretty well; whereas, linear regression was under-fitting
# 4. To correct the issue, we had to add additional features for linear regression
# 5. With this change, linear regression performed much better
# 
# XGBoost can detect patterns involving non-linear relationship; whereas, algorithms like linear regression may need complex feature engineering
