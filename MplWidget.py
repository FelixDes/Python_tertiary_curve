from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111, projection='3d')
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

    def add_points(self, x, y, z):
        self.axes.plot_surface(x, y, z)
        self.canvas.draw()

    def clear_plot(self):
        self.axes.cla()
        self.canvas.draw()
