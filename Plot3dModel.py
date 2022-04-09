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
                saddle.set_x_y(x, y)
                return saddle
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
                elliptic_paraboloid.set_x_y(x, y)
                return elliptic_paraboloid


class Curve:
    def __init__(self, a, b, c):
        self.x = None
        self.y = None
        self.z = None
        self.a = a
        self.b = b
        self.c = c
        self.equation = None

    def set_x_y(self, x, y):
        self.x = x
        self.y = y
        self.z = self.get_z(self.x, self.y)

    def get_z(self, x, y):
        return 0


class SaddleCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.equation = r"$f(x) = \frac{x^{2}}{{%(a)s}^{2}}-\frac{y^{2}}{{%(b)s}^{2}}={%(c)s}*z$" \
                        % {'a': a, 'b': b, 'c': c}

    def set_x_y(self, x, y):
        super(SaddleCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return (((x ** 2) / (2 * self.a ** 2)) - ((y ** 2) / (2 * self.b ** 2))) / self.c


class EllipsoidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.formula = ""

    def set_x_y(self, x, y):
        super(EllipsoidCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return np.sqrt((1 - (x ** 2) / (self.a ** 2) - (y ** 2) / (self.b ** 2)) / (self.c ** 2))


class EllipticParaboloidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.equation = r"$f(x) = \frac{x^{2}}{{%(a)s}^{2}}-\frac{y^{2}}{{%(b)s}^{2}}={%(c)s}*z$"\
                        % {'a': a, 'b': b, 'c': c}

    def set_x_y(self, x, y):
        super(EllipticParaboloidCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return ((x ** 2) / (2 * self.a ** 2)) + ((y ** 2) / (2 * self.b ** 2))
