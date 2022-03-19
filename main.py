import numpy as np
import random
import matplotlib.pyplot as plt


class LRGD:
    a_current = 0
    b_current = 0
    error = []

    def plot_data_label(self, x, y):
        plt.xlabel("X")
        plt.ylabel("Y")
        y_current = self.a_current * x + self.b_current
        plt.plot(x, y_current, "-r")
        plt.scatter(x, y)
        plt.show()
        plt.plot(lgrd.error)
        plt.show()

    def generate_random_data(self, a, b):
        X = np.random.randint(100, size=100)
        Y = np.empty(100)
        for i in range(X.size):
            Y[i] = int(a * X[i] + b + random.gauss(50, 50))
        return X, Y

    def train_with_gd(self, X, y, epochs, e):
        N = float(len(y))
        for i in range(epochs):
            y_current = (self.a_current * X) + self.b_current
            cost = sum([data ** 2 for data in (y - y_current)]) / N
            a_gradient = -(2 / N) * sum(X * (y - y_current))
            b_gradient = -(2 / N) * sum(y - y_current)
            self.a_current = self.a_current - (e * a_gradient)
            self.b_current = self.b_current - (e * b_gradient)
            self.error.append(cost)

    def train_with_sgd(self, X, y, epochs, e):
        rn = random.randint(0, len(y))
        for i in range(epochs):
            y_current = (self.a_current * X[rn]) + self.b_current
            cost = (y[rn] - y_current)**2
            a_gradient = -2 * X[rn] * (y[rn] - y_current)
            b_gradient = -2 * y[rn] - y_current
            self.a_current = self.a_current - (e * a_gradient)
            self.b_current = self.b_current - (e * b_gradient)
            self.error.append(cost)

    def train_with_minibatch(self, X, y, epochs, e):
        print("TODO")

    def predict(self, X):
        return self.a_current * X + self.b_current


if __name__ == '__main__':
    epsilon = 0.00001
    iterations = 100
    lgrd = LRGD()
    X, Y = lgrd.generate_random_data(3, 7)
    lgrd.train_with_sgd(X, Y, iterations, epsilon)
    lgrd.plot_data_label(X, Y)
