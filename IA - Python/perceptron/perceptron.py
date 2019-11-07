from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Gerador de números aleatórios.
        random.seed(1)

        # Modelamos 6 conexões de entrada e 1 conexão de saída. Atribuímos pesos aleatórios a uma matriz 6 x 1.
        self.synaptic_weights = 2 * random.random((6, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Treinamos a rede neural através de um processo de tentativa e erro ajustando os pesos a cada iteração.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    print("Pesos iniciais aleatórios")
    print(neural_network.synaptic_weights)

    training_set_inputs = array([[1,0,0,0,0,1], [1,0,0,0,1,0], [1,0,0,0,1,1], [1,0,0,1,0,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,0,1,1,1], [0,1,0,0,0,0], [0,1,0,0,0,1], [0,1,0,0,1,0], [0,1,0,0,1,1], [0,1,0,1,0,0], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,0,1,1,1], [0,0,1,0,0,0], [0,0,1,0,0,1], [0,0,1,0,1,0], [0,0,1,0,1,1], [0,0,1,1,0,0], [0,0,1,1,0,1], [0,0,1,1,1,0], [0,0,1,1,1,1]])
    training_set_outputs = array([[1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0]]).T

    # Treina a rede neural 10.000x fazendo pequenos ajustes a cada iteração.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)
    print("Novo valor do peso após treino: ")
    print(neural_network.synaptic_weights)

    # Teste da rede neural.
    print("Testando entrada [1, 0, 0, 1, 0, 0]: ")
    print(neural_network.think(array([1, 0, 0, 1, 0, 0])))