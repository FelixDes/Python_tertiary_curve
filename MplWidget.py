from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111, projection='3d')

        self.scroll_for_equations = QScrollArea()

        layout = QHBoxLayout(self)
        layout.addWidget(self.canvas)

    def add_curve(self, curve):
        self.axes.plot_surface(curve.x, curve.y, curve.z)
        self.canvas.draw()

    def clear_plot(self):
        self.axes.cla()
        self.canvas.draw()
