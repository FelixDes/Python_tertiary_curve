from Plot3dModel import Plot3dModel
from matplotlib.backends.backend_template import FigureCanvas


class WindowPresenter:
    def __init__(self):
        self.model = Plot3dModel
        self.curve_types = Plot3dModel.curve_types

    def get_canvas(self, curve_index) -> FigureCanvas:
        return self.model.get_canvas(curve_index)
