# Logistic Regression

# Importing the libraries
import pandas as pd
from sklearn import model_selection

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
#x = dataset.iloc[:, [2, 3]].values
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.33, random_state = 0)

#if we use StandardScaler() then accuracy will increase
# Feature Scaling
#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix")
print(cm)