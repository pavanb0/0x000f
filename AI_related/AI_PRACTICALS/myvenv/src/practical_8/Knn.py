import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset from scikit-learn
iris = load_iris()
data = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
data['Target'] = iris['target']

# Extract relevant columns for the feature matrix
X = data.drop(['Target'], axis=1).values
# Target variable for classification
y = data['Target'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the value of k for K-NN
k = 3

# Classification with K-NN
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Evaluate classification accuracy
classification_accuracy = accuracy_score(y_test, y_pred)
print("Classification Accuracy:", classification_accuracy)
