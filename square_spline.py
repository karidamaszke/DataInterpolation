import matplotlib.pyplot as plt
import numpy as np


class SquareSpline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = len(self.x)
        self.h = self.create_h()
        self.A = self.create_A()
        self.B = self.create_B()
        self.result = self.spline()

    def create_h(self):
        h = []
        for i in range(self.size - 1):
            h.append(self.x[i + 1] - self.x[i])
        return h

    def create_A(self):
        A = np.matrix(np.zeros((self.size + 8, self.size + 8)))
        A[0, 0] = self.h[0]
        col = 1

        for i in range(1, self.size - 1):
            A[i, col] = self.h[i]
            col += 1
            A[i, col] = self.h[i] ** 2
            col += 1

        A[10, 0] = 1
        A[10, 1] = -1
        col = 1

        for i in range(self.size, self.size + 8):
            A[i, col] = 1
            A[i, col + 1] = 2 * self.h[i - 11]
            A[i, col + 2] = -1
            col += 2

        return A

    def create_B(self):
        B = np.matrix(np.zeros((self.size + 8, 1)))
        for i in range(self.size - 1):
            B[i, 0] = self.y[i + 1] - self.y[i]
        return B

    def spline(self):
        return np.linalg.inv(self.A) @ self.B

    def draw(self):
        res = []
        time = np.linspace(self.x[0], self.x[1], 20)
        for t in time:
            res.append(self.y[0] + self.result.item(0) * (t - self.x[0]))
        plt.plot(time, res, 'b', label='square spline interpolation')

        itr = 1
        while itr < self.size - 1:
            res = []
            time = np.linspace(self.x[itr], self.x[itr + 1])
            for t in time:
                res.append(self.y[itr] + self.result.item(2 * itr - 1) * (t - self.x[itr]) +
                           self.result.item(2 * itr) * (t - self.x[itr]) ** 2)
            plt.plot(time, res, 'b')
            itr += 1
