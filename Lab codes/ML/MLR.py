import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import linear_model
sns.set()

df = pd.read_csv('datasets/house_price.csv')
print(df.head())
print(df.describe())

X = df.drop([' Price'],axis=1).values
Y = df[' Price'].values

sns.scatterplot(data=df)

reg = linear_model.LinearRegression()
reg.fit(X,Y)

print(reg.coef_)
print(reg.intercept_)

reg.predict(X)

reg.predict([[6,8]])

plt.scatter(Y, reg.predict(X))
plt.xlabel('Actual')
plt.ylabel('Prediction')
plt.show()