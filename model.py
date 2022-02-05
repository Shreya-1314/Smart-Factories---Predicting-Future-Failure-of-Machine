import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import precision_score, recall_score
# import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

url = "Predict_Failures.csv"
data = pd.read_csv(url)
data.head()

X = data[['Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]']]
y = data['Machine failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=100)


model = KNeighborsClassifier(n_neighbors = 3)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# accuracy = model.score(y_test,y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Accuracy: ", accuracy)

# saving the model
import joblib
joblib.dump(model, 'model.pkl')

