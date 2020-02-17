import matplotlib.pyplot as plt
import sys

from interpolations.newton_interpolation import Newton
from interpolations.square_spline import SquareSpline
from interpolations.cubic_spline import CubicSpline


def read_data(path):
    x, y = [], []

    try:
        with open(path, 'r') as file:
            for line in file:
                x.append(float(line.split()[0]))
                y.append(float(line.split()[1]))
    except Exception as err:
        print(str(err))
        sys.exit(-1)

    return x, y


def main():
    p_x, p_y = read_data("data.txt")
    plt.plot(p_x, p_y, 'o', label='Data points')

    newton = Newton(p_x, p_y)
    newton.draw()

    square_spline = SquareSpline(p_x, p_y)
    square_spline.draw()

    cubic_spline = CubicSpline(p_x, p_y)
    cubic_spline.draw()

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
