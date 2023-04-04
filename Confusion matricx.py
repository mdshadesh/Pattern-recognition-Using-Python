
Actual_class = ['p','p','N','N','p'] 
Predicted_class = ['p','p','N','p','N'] 
#Actual_class = [1,1,0,0,1]
#Predicted_class = [1,1,0,1,0] 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(Actual_class, Predicted_class, labels=['p','N']) 
print() 
TP = cm[0,0] 
FP = cm[0,1] 
FN = cm[1,0] 
TN = cm[1,1] 
accuracy = (TP+TN)/(TP+FP+FN+TN) 
print("Accuracy =", accuracy*100, "%")