import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
bankdata = pd.read_csv("dataset/bill_authentication.csv")
#axis=0 means row drop and axis=1 means column drop
features = bankdata.drop('Class', axis=1)
label = bankdata['Class']

feature_train, feature_test, label_train, label_test = train_test_split(features, label, test_size = 0.25, random_state=0)

svclassifier = SVC(kernel='linear')
svclassifier.fit(feature_train, label_train)
predicted_label = svclassifier.predict(feature_test)
cm = confusion_matrix(label_test, predicted_label)
TP = cm[0,0]
print(TP)