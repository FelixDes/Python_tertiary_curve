from Plot3dModel import Plot3dModel
from matplotlib.backends.backend_template import FigureCanvas

grid_size = 10
shift = 0.25


class WindowPresenter:
    def __init__(self):
        self.model = Plot3dModel(grid_size, shift)
        self.curve_types = Plot3dModel.curve_types

    def get_curve_types(self) -> list:
        return self.curve_types

    def get_canvas(self, curve_index, *args) -> FigureCanvas:
        return self.model.get_canvas(curve_index, *args)
