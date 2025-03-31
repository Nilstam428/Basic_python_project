# Auto-generated Python script - 2025-03-31
# Question: Create a Python class for a simple neural network with one hidden layer

```python
import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.random.randn(hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.random.randn(output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output

    def train(self, inputs, targets, epochs, learning_rate):
        for _ in range(epochs):
            # Forward pass
            outputs = self.forward(inputs)

            # Compute error
            output_error = targets - outputs
            output_delta = output_error * self.sigmoid_derivative(outputs)

            # Backpropagation
            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

            # Update weights and biases
            self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0) * learning_rate
            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate

    def predict(self, inputs):
        return self.forward(inputs)
``` 

# If this code contains a function or class but no execution code,
# here's a simple test to run it:

def test_solution():
    print("Testing the solution...")
    # Add test code here if needed
    print("Test completed!")

if __name__ == "__main__":
    test_solution()
