import matplotlib.pyplot as plt
from newton_interpolation import Newton
from square_spline import SquareSpline
from cubic_spline import CubicSpline


def read_data(path):
    x, y = [], []
    with open(path, 'r') as file:
        for line in file:
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))
    return x, y


def main():
    p_x, p_y = read_data("data.txt")
    plt.plot(p_x, p_y, 'o')

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
