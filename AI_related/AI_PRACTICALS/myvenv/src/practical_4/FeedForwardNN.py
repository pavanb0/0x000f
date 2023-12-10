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
