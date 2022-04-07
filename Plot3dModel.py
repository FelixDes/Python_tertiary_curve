import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


class Plot3dModel:
    curve_types = ["Saddle", "Ellipsoid"]

    def __init__(self, grid_size, shift):
        self.fig = Figure()
        self.x = np.arange(-grid_size, grid_size, shift)
        self.y = np.arange(-grid_size, grid_size, shift)
        self.x, self.y = np.meshgrid(self.x, self.y)

    def get_points(self, curve_index, *coefficients):
        match curve_index:
            case 0:
                saddle = SaddleCurve(*coefficients)
                z = saddle.get_z(self.x, self.y)
                return self.x, self.y, z
            case 1:
                pass


class Curve:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_z(self, x, y):
        return 0


class SaddleCurve(Curve):
    def __init__(self, a, b, c=None):
        super().__init__(a, b, c)

    def get_z(self, x, y):
        return ((x ** 2) / (2 * self.a ** 2)) - ((y ** 2) / (2 * self.b ** 2))


class EllipsoidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def get_z(self, x, y):
        return np.sqrt((1 - (x ** 2) / (self.a ** 2) - (y ** 2) / (self.b ** 2)) / (self.c ** 2))
