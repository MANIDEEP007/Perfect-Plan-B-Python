x = [[0],[1],[2],[3]] #Mails
y = [0,0,1,1] #Inbox 0 Spam 1

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3) #Specify Number of neighbors
neigh.fit(x,y) #Apply The Model
print(neigh.predict([[0.9],[1.1],[1.5],[3.3]])) #Prediction for Test Data


#Accuracy Score Calculation
from sklearn.metrics import accuracy_score
y_pred = [0,2,1,3]
y_act = [0,1,2,3]
print(accuracy_score(y_act,y_pred))
