import matplotlib.pyplot as plt
import numpy as np


class CubicSpline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = len(x)
        self.h = self.create_h()
        self.A = self.create_A()
        self.R = self.create_R()
        self.C = self.spline()
        self.B = self.create_B()
        self.D = self.create_D()

    def create_h(self):
        h = []
        for i in range(self.size - 1):
            h.append(self.x[i + 1] - self.x[i])
        return h

    def create_A(self):
        A = np.matrix(np.zeros((self.size, self.size)))
        A[0, 0], A[10, 10] = 1, 1

        for i in range(1, self.size - 1):
            A[i, i - 1] = self.h[i - 1]
            A[i, i] = 2 * (self.h[i - 1] + self.h[i])
            A[i, i + 1] = self.h[i]

        return A

    def create_R(self):
        R = np.matrix(np.zeros((self.size, 1)))

        for i in range(1, self.size - 1):
            R[i, 0] = 3 * (self.finite_diff(i + 1, i) - self.finite_diff(i, i - 1))

        return R

    def create_B(self):
        B = np.matrix(np.zeros((self.size - 1, 1)))

        for i in range(self.size - 1):
            B[i, 0] = (self.y[i + 1] - self.y[i]) / self.h[i] - (self.h[i] / 3) * (2 * self.C[i, 0] + self.C[i + 1, 0])

        return B

    def create_D(self):
        D = np.matrix(np.zeros((self.size - 1, 1)))

        for i in range(self.size - 1):
            D[i, 0] = (self.C[i + 1, 0] - self.C[i, 0]) / (3 * self.h[i])

        return D

    def finite_diff(self, i, j):
        return (self.y[i] - self.y[j]) / (self.x[i] - self.x[j])

    def spline(self):
        return np.linalg.inv(self.A) @ self.R

    def draw(self):
        res = []
        time = 0
        for i in range(self.size - 1):
            res = []
            time = np.linspace(self.x[i], self.x[i + 1], 20)

            for t in time:
                res.append(self.y[i] + self.B.item(i) * (t - self.x[i]) + self.C.item(i) * ((t - self.x[i]) ** 2) +
                           self.D.item(i) * ((t - self.x[i]) ** 3))
            plt.plot(time, res, 'y')
        plt.plot(time, res, 'y', label='cubic spline interpolation')

