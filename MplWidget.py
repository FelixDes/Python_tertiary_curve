import matplotlib
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QFormLayout, QGroupBox, QLabel
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111, projection='3d')

        self.equations = QFormLayout()
        group_box = QGroupBox()
        scroll_for_equations = QScrollArea()
        scroll_for_equations.setMinimumSize(150, -1)

        group_box.setLayout(self.equations)
        scroll_for_equations.setWidget(group_box)
        scroll_for_equations.setWidgetResizable(True)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(scroll_for_equations)

    def add_curve(self, curve):
        self.add_curve_equation(curve.equation)
        self.axes.plot_surface(curve.x, curve.y, curve.z)
        self.canvas.draw()

    def clear_plot(self):
        self.clear_curve_equations()
        self.axes.cla()
        self.canvas.draw()

    def add_curve_equation(self, equation):
        eq = QLabel()
        eq.setPixmap(self.mathTex_to_QPixmap(equation, 10))
        self.equations.addRow(eq)

    def clear_curve_equations(self):
        [self.equations.removeRow(0) for _ in range(self.equations.rowCount())]

    def mathTex_to_QPixmap(self, mathTex, fs):
        fig = matplotlib.figure.Figure()
        fig.patch.set_facecolor('none')
        fig.set_canvas(FigureCanvasAgg(fig))
        renderer = fig.canvas.get_renderer()

        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        ax.patch.set_facecolor('none')
        t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs)

        fwidth, fheight = fig.get_size_inches()
        fig_bbox = fig.get_window_extent(renderer)

        text_bbox = t.get_window_extent(renderer)

        tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
        tight_fheight = text_bbox.height * fheight / fig_bbox.height

        fig.set_size_inches(tight_fwidth, tight_fheight)

        buf, size = fig.canvas.print_to_buffer()
        qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                      QtGui.QImage.Format_ARGB32))
        qpixmap = QtGui.QPixmap(qimage)

        return qpixmap
