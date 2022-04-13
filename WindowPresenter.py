from Plot3dModel import Plot3dModel

grid_size = 10
shift = 1


class WindowPresenter:
    def __init__(self):
        self.model = Plot3dModel(grid_size, shift)
        self.curve_types = Plot3dModel.curve_types

    def get_curve_types(self) -> list:
        return self.curve_types

    def add_points_to_widget(self, mpl_widget, curve_index, *args):
        if 0 not in args:
            return mpl_widget.add_curve(self.model.get_points(curve_index, *args))
