import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load the Iris dataset from scikit-learn
iris = load_iris()
data = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
data['Target'] = iris['target']

# Extract relevant columns for binary classification (Iris Setosa vs. Others)
data_binary = data[data['Target'] != 2]
X = data_binary.drop(['Target'], axis=1).values
y = data_binary['Target'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear', C=1.0)

# Train the SVM model
svm_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = svm_classifier.predict(X_test)

# Evaluate classification accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Classification Accuracy:", accuracy)

# Display classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))
