import matplotlib.pyplot as plt
import numpy as np

from interpolations.spline import Spline


class SquareSpline(Spline):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.h = self.create_h()
        self.a = self.create_a()
        self.b = self.create_b()
        self.result = self.spline()

    def create_a(self):
        a = np.array(np.zeros((self.size + 8, self.size + 8)))
        a[0, 0] = self.h[0]
        col = 1

        for i in range(1, self.size - 1):
            a[i, col] = self.h[i]
            col += 1
            a[i, col] = self.h[i] ** 2
            col += 1

        a[10, 0] = 1
        a[10, 1] = -1
        col = 1

        for i in range(self.size, self.size + 8):
            a[i, col] = 1
            a[i, col + 1] = 2 * self.h[i - 11]
            a[i, col + 2] = -1
            col += 2

        return a

    def create_b(self):
        b = np.array(np.zeros((self.size + 8, 1)))
        for i in range(self.size - 1):
            b[i, 0] = self.y[i + 1] - self.y[i]
        return b

    def spline(self):
        return np.linalg.inv(self.a) @ self.b

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
