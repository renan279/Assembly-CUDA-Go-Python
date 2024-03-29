import matplotlib.pyplot as plt
import numpy as np
import operator

class DataPoint:
    def __init__(self, x, label, dist=None):
        self.x = x
        self.label = label
        self.dist = dist

class KNN:
    def __init__(self, x, y, k=2):
        self.x = x
        self.y = y
        self.k = k
        self.data = [DataPoint(x, y) for x, y in zip(self.x, self.y)]
        self.n_plot = 0

    def euclidean_distance(self, x, y):
        #Calculates euclidean distance between x and y
        dist = np.linalg.norm(x-y)
        return dist

    def predict(self, xi):
        # Calcular distância de cada ponto
        self.xi = xi

        for p in self.data:
            p.dist = self.euclidean_distance(xi, p.x)

        # vizinhos 
        self.k_neighbors = sorted(self.data, key=lambda p: p.dist)[:self.k]

        # calculo das probabilidades dos vizinhos
        n = { p.label:0 for p in self.data }
        for p in self.k_neighbors:
            n[p.label] += 1

        # melhores probabilidades
        return max(n.items(), key=operator.itemgetter(1))[0]

    def vis(self, show=False):
        plt.figure(self.n_plot)
        self.n_plot += 1

        not_neighbors = [plt.scatter(p.x[0], p.x[1], color='blue') for p in self.data if p not in self.k_neighbors]

        for n in self.k_neighbors:
            plt.scatter(n.x[0], n.x[1], color='green', marker='s')

        plt.scatter(self.xi[0], self.xi[1], color='red', marker='*', s=100)

        # legendas
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('knn')
        plt.savefig('knn.png')
        plt.show() if show else 0

def main():
    r = lambda x, y: np.random.randint(x, y)
    n_samples = 100
    x = np.array([ [r(1, 100), r(1, 100)] for _ in range(n_samples)])
    y = np.array([ i[0] for i in x ])

    knn = KNN(x, y, k=10)

    p_value = [r(1, 100), r(1, 100)]
    print('K-NN: {}'.format(knn.k))
    print('O centroid ideal do grupo é o de valor no eixo X: {}'.format(knn.predict(p_value)))

    knn.vis(show=True)

if __name__ == '__main__':
    main()