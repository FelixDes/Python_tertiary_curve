import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class Plot3dModel:
    curve_types = ["Saddle", "Ellipsoid"]

    def __init__(self, grid_size, shift):
        pass

    def get_canvas(self, curve_index) -> FigureCanvas:
        match curve_index:
            case 0:
                pass
            case 1:
                pass


class Curve:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_z(self):
        return 0


class SaddleCurve(Curve):
    def __init__(self, a, b, c=None):
        super().__init__(a, b, c)

    def get_z(self):
        pass


class EllipsoidCurve(Curve):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def get_z(self):
        pass
