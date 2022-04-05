from WindowPresenter import WindowPresenter

import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWidget(QMainWindow):
    font = QtGui.QFont("ttf", 16)

    def __init__(self):
        super().__init__()
        self.wp = WindowPresenter()
        uic.loadUi("ui.ui", self)
        self.curveTypeComboBox.addItems(list(self.wp.get_curve_types()))
        self.set_listeners()

    def set_listeners(self):
        self.runButton.clicked.connect(self.run)

    def run(self):
        self.MplWidget.canvas = self.wp.get_canvas(self.curveTypeComboBox.count(),
                                                   self.spinBox_a.value(),
                                                   self.spinBox_b.value(),
                                                   self.spinBox_c.value())

    @staticmethod
    def start_window():
        app = QApplication(sys.argv)
        ex = MainWidget()
        ex.show()
        sys.exit(app.exec())
