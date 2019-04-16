import matplotlib.pyplot as plt
import numpy as np


class Newton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b = self.coef()
        self.time = np.linspace(self.x[0], self.x[-1], 1000)
        self.result = self.newton()

    def coef(self):
        b = []
        for i in range(len(self.x)):
            b.append(self.y[i])

        for j in range(1, len(self.x)):
            for i in range(len(self.x) - 1, j - 1, -1):
                b[i] = float(b[i] - b[i - 1]) / float(self.x[i] - self.x[i - j])

        return np.array(b)

    def newton(self):
        n = len(self.b) - 1
        current_value = self.b[n]
        for i in range(n - 1, -1, -1):
            current_value = current_value * (self.time - self.x[i]) + self.b[i]
        return current_value

    def draw(self):
        plt.plot(self.time, self.result, 'r', label='Newton\'s polynomial interpolation')
