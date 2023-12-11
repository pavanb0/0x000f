#practcal 1


def BFS_EASY(start,goal,map):
    # print(start,'\n',goal,'\n',map)
    from collections import deque
    queue = deque()
    queue.append(start)
    while queue:
        pointer = queue.popleft()
        print(queue)
        if pointer == goal:
            print("found")
            break 
        for i,j in map.get(pointer).items():
            queue.append(i)



def DFS_EASY(start,goal,map):
    stack = []
    stack.append(start)
    visited = set()
    while stack:
        print(stack)
        pointer = stack.pop()
        if pointer == goal:
            print("found goal city")
            return
        if pointer not in visited:
            visited.add(pointer)

            #expand the tree
            for i,j in map.get(pointer).items():
                stack.append(i)

print(DFS_EASY("Arad","Bucharest",dict_gn))





#practical 2 best first search


# its just Astar without pathcost only manhatten distance 

from romanianmap import dict_hn,dict_gn
import heapq
import time
def greedy_best_first_search(start, goal, graph, heuristic):
    priority_queue = [(heuristic[start], start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        
        print(priority_queue)
        if current_node == goal:
            print("Found goal city")
            return

        for next_node, _ in graph.get(current_node).items():
            heapq.heappush(priority_queue, (heuristic[next_node], next_node))
          

greedy_best_first_search("Arad", "Bucharest", dict_gn, dict_hn)






# practical 3 decision tree





import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

# Assuming the target variable is in a column named 'target'
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Visualize and interpret the generated decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=iris.target_names)
plt.title("Decision Tree Visualization")
plt.show()





#practical 4 feed forward




import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed()
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):
        input = inputs.astype(float)
        output = self.sigmoid(np.dot(input, self.synaptic_weights))
        return output

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    print("Beginning randomly generated weights:")
    print(neural_network.synaptic_weights)

    # Training data
    training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 15000)
    print("Ending weights after training:")
    print(neural_network.synaptic_weights)

    # User input
    user_input_one = float(input("User input One:"))
    user_input_two = float(input("User input Two:"))
    user_input_three = float(input("User input Three:"))
    print("Considering new situation:", user_input_one, user_input_two, user_input_three)

    # Make a prediction
    output_data = neural_network.think(np.array([user_input_one, user_input_two, user_input_three]))
    print("New output data:")
    print(output_data)





# practical 5 svm 





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





# practical 6 ada boost





import pandas
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
num_trees = 30
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
results = model_selection.cross_val_score(model, X, Y)
print(results.mean())




# practical 8 knn




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

# practical 9 associate rule mining
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample dataset (list of transactions)
dataset = [
    ['Milk', 'Eggs', 'Bread'],
    ['Beer', 'Diapers'],
    ['Milk', 'Beer', 'Chips', 'Diapers'],
    ['Milk', 'Bread', 'Chips'],
    ['Eggs', 'Bread', 'Diapers']
]

# Convert the dataset to a one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules
association_rules_df = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

# Display frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Display association rules with support and confidence
print("\nAssociation Rules:")
print(association_rules_df)
