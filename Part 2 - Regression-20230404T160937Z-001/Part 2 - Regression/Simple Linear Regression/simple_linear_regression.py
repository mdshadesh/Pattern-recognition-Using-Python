# Simple Linear Regression

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
x_train = dataset.iloc[:, :-1].values
y_train = dataset.iloc[:, -1].values

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
# Predicting the Test set results
yearExperience = 3.1
y_pred = regressor.predict([[yearExperience]])
print("Salary for ", yearExperience, " years of experience is ", y_pred[0])

# Visualising the Training set results
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
