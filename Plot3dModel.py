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
                rx = 1 / (coefficients[0] ** 0.5)
                ry = 1 / (coefficients[1] ** 0.5)
                rz = 1 / (coefficients[2] ** 0.5)

                u = np.linspace(0, 2 * np.pi, 20)
                v = np.linspace(0, np.pi, 20)
                x = rx * np.outer(np.cos(u), np.sin(v))
                y = ry * np.outer(np.sin(u), np.sin(v))
                ellipsoid = EllipsoidCurve(*coefficients, rz, u, v)
                ellipsoid.set_x_y(x, y)
                return ellipsoid
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
        self.equation = r"$\frac{x^{2}}{{%(a)s}^{2}}-\frac{y^{2}}{{%(b)s}^{2}}={%(c)s}*z$" \
                        % {'a': a, 'b': b, 'c': c}

    def set_x_y(self, x, y):
        super(SaddleCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return (((x ** 2) / (2 * self.a ** 2)) - ((y ** 2) / (2 * self.b ** 2))) / self.c


class EllipsoidCurve(Curve):
    def __init__(self, a, b, c, rz, u, v):
        super().__init__(a, b, c)
        self.rz = rz
        self.u = u
        self.v = v
        self.equation = r"$\frac{x^2}{{%(a)s}^2} + \frac{y^2}{{%(b)s}^2} + \frac{z^2}{{%(c)s}^2} = 1$" \
                        % {'a': a, 'b': b, 'c': c}

    def set_x_y(self, x, y):
        super(EllipsoidCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return self.rz * np.outer(np.ones_like(self.u), np.cos(self.v))


class EllipticParaboloidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.equation = r"$\frac{x^{2}}{{%(a)s}^{2}}+\frac{y^{2}}{{%(b)s}^{2}}={%(c)s}*z$" \
                        % {'a': a, 'b': b, 'c': c}

    def set_x_y(self, x, y):
        super(EllipticParaboloidCurve, self).set_x_y(x, y)

    def get_z(self, x, y):
        return ((x ** 2) / (2 * self.a ** 2)) + ((y ** 2) / (2 * self.b ** 2))
