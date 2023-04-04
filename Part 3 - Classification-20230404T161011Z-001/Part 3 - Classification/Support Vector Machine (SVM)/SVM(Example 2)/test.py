import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
bankdata = pd.read_csv("dataset/bill_authentication.csv")
x = bankdata.drop('Class', axis=1)
y = bankdata['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)
y_pred = svclassifier.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)