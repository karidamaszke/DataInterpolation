import matplotlib.pyplot as plt
import numpy as np

from interpolations.spline import Spline


class CubicSpline(Spline):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.a = self.create_a()
        self.r = self.create_r()
        self.c = self.spline()
        self.b = self.create_b()
        self.d = self.create_d()

    def create_a(self):
        a = np.array(np.zeros((self.size, self.size)))
        a[0, 0], a[10, 10] = 1, 1

        for i in range(1, self.size - 1):
            a[i, i - 1] = self.h[i - 1]
            a[i, i] = 2 * (self.h[i - 1] + self.h[i])
            a[i, i + 1] = self.h[i]

        return a

    def create_r(self):
        r = np.array(np.zeros((self.size, 1)))

        for i in range(1, self.size - 1):
            r[i, 0] = 3 * (self.finite_diff(i + 1, i) - self.finite_diff(i, i - 1))

        return r

    def create_b(self):
        b = np.array(np.zeros((self.size - 1, 1)))

        for i in range(self.size - 1):
            b[i, 0] = (self.y[i + 1] - self.y[i]) / self.h[i] - (self.h[i] / 3) * (2 * self.c[i, 0] + self.c[i + 1, 0])

        return b

    def create_d(self):
        d = np.array(np.zeros((self.size - 1, 1)))

        for i in range(self.size - 1):
            d[i, 0] = (self.c[i + 1, 0] - self.c[i, 0]) / (3 * self.h[i])

        return d

    def finite_diff(self, i, j):
        return (self.y[i] - self.y[j]) / (self.x[i] - self.x[j])

    def spline(self):
        return np.linalg.inv(self.a) @ self.r

    def draw(self):
        res = []
        time = 0
        for i in range(self.size - 1):
            res = []
            time = np.linspace(self.x[i], self.x[i + 1], 20)

            for t in time:
                res.append(self.y[i] + self.b.item(i) * (t - self.x[i]) + self.c.item(i) * ((t - self.x[i]) ** 2) +
                           self.d.item(i) * ((t - self.x[i]) ** 3))
            plt.plot(time, res, 'y')
        plt.plot(time, res, 'y', label='cubic spline interpolation')

