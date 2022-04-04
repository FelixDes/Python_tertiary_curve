import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class Plot3dModel:
    curve_types = ["Saddle", "Ellipsoid"]

    def __init__(self):
        pass

    def get_canvas(self, curve_index) -> FigureCanvas:
        match curve_index:
            case 0:
                pass
            case 1:
                pass
