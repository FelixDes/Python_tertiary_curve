from WindowPresenter import WindowPresenter

import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWidget(QMainWindow):
    font = QtGui.QFont("ttf", 16)

    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)
        self.setWindowTitle("Кривые третьего порядка")

        self.wp = WindowPresenter(self.spinBox_grid_size.value())

        self.curveTypeComboBox.addItems(list(self.wp.get_curve_types()))
        self.set_listeners()

    def set_listeners(self):
        self.runButton.clicked.connect(self.run)
        self.clearButton.clicked.connect(lambda: self.MplWidget.clear_plot())

    def run(self):
        self.wp = WindowPresenter(self.spinBox_grid_size.value())
        self.wp.add_points_to_widget(self.MplWidget, self.curveTypeComboBox.currentIndex(),
                                     self.spinBox_a.value(),
                                     self.spinBox_b.value(),
                                     self.spinBox_c.value())

    @staticmethod
    def start_window():
        app = QApplication(sys.argv)
        ex = MainWidget()
        ex.show()
        sys.exit(app.exec())
