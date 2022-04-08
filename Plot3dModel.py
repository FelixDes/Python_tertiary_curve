from matplotlib.figure import Figure
import numpy as np


class Plot3dModel:
    curve_types = ["Saddle", "Ellipsoid", "Elliptic paraboloid"]

    def __init__(self, grid_size, shift):
        self.grid_size = grid_size
        self.shift = shift
        self.fig = Figure()


    def get_points(self, curve_index, *coefficients):
        match curve_index:
            case 0:
                x = np.arange(-self.grid_size, self.grid_size, self.shift)
                y = np.arange(-self.grid_size, self.grid_size, self.shift)
                x, y = np.meshgrid(x, y)
                saddle = SaddleCurve(*coefficients)
                z = saddle.get_z(x, y)
                return x, y, z
            case 1:
                pass
                # ellipsoid = EllipsoidCurve(*coefficients)
                # z = ellipsoid.get_z(x, y)
                # return x, y, z
            case 2:
                x = np.arange(-self.grid_size, self.grid_size, self.shift)
                y = np.arange(-self.grid_size, self.grid_size, self.shift)
                x, y = np.meshgrid(x, y)
                elliptic_paraboloid = EllipticParaboloidCurve(*coefficients)
                z = elliptic_paraboloid.get_z(x, y)
                return x, y, z


class Curve:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_z(self, x, y):
        return 0


class SaddleCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def get_z(self, x, y):
        return (((x ** 2) / (2 * self.a ** 2)) - ((y ** 2) / (2 * self.b ** 2))) / self.c


class EllipsoidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def get_z(self, x, y):
    #     for i in range(len(x)):
    #         if ((1 - (x[i][i] ** 2) / (self.a ** 2) - (y[i][i] ** 2) / (self.b ** 2)) / (self.c ** 2)) < 0:
    #             return np.nan
            return np.sqrt((1 - (x ** 2) / (self.a ** 2) - (y ** 2) / (self.b ** 2)) / (self.c ** 2))


class EllipticParaboloidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def get_z(self, x, y):
        return ((x ** 2) / (2 * self.a ** 2)) + ((y ** 2) / (2 * self.b ** 2))
