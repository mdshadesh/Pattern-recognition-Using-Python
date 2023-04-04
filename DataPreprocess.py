############ Data Preprocessing ################
#import libraries
import pandas as pd
import numpy as np

#load the dataset
dataset = pd.read_csv("OnlineShoppingStatus.csv")
describe = dataset.describe()
#print(describe['Age']['max'])
#create dependant and independant variable vectors
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

#handle missing data
#count the missing data in each collumn
print(dataset.isnull().sum())
#drop missing value records or rows
dataset.dropna(inplace=True)
dataset
#replace missing values
dataset = pd.read_csv("OnlineShoppingStatus.csv")
describe = dataset.describe()
#print(describe['Age']['max'])
#create dependant and independant variable vectors
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
#Data Encoding: handle categorical data
#One hot encoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
x = dataset.iloc[:, 1:3].values
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))
#print(x)

#label or class encoding
#when class contains categorical data like yes or no
from sklearn.preprocessing import LabelEncoder
y = dataset.iloc[:, -1].values
le = LabelEncoder()
y=le.fit_transform(y)
#print(y)
