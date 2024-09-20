
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# <h2>Simple Regression Dataset - Straight Line</h2>
# 
# Input Feature: X  
# 
# Target: 5*X + 8 + some noise
# 
# Objective: Train a model to predict target for a given X


# Straight Line Function
def straight_line(x):
    return 5*x + 8
np.random.seed(5)
samples = 150
x = pd.Series(np.arange(0,150))
y = x.map(straight_line) + np.random.randn(samples)*10
df = pd.DataFrame({'x':x,'y':y})
print(df.head())

# Correlation will indicate how strongly features are related to the output
print(df.corr())

plt.plot(df.x,df.y,label='Target')
plt.grid(True)
plt.xlabel('Input Feature')
plt.ylabel('Target')
plt.legend()
plt.show()

# Save all data
df.to_csv('linear_all.csv',index=False,
          columns=['x','y'])


# <h2>SageMaker Convention for Training and Validation files</h2>
# 
# CSV File Column order: y_noisy, x
# 
# Training, Validation files do not have a column header




# Training = 70% of the data
# Validation = 30% of the data
# Randomize the datset
np.random.seed(5)
l = list(df.index)
np.random.shuffle(l)
df = df.iloc[l]
print(df.head())

rows = df.shape[0]
train = int(.7 * rows)
test = rows - train

print(rows, train, test)


# Write Training Set
df[:train].to_csv('linear_train.csv',index=False,header=False,columns=['y','x'])

# Write Validation Set
df[train:].to_csv('linear_validation.csv',index=False,header=False,columns=['y','x'])
