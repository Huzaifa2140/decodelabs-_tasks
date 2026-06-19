from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

# scaling is needed here since knn is distance based, raw values would mess it up
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)
print("Accuracy:", round(acc * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# quick test on one sample just to see prediction working manually
sample = [X_test[0]]
result = model.predict(sample)
print("\nSample prediction:", iris.target_names[result[0]])
print("Actual label:", iris.target_names[y_test[0]])
