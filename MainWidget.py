import WindowPresenter

import sys
import webbrowser

from PyQt5 import QtGui, uic
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QScrollArea, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QStyledItemDelegate, QLineEdit, QTableWidgetItem, QDialog, QHBoxLayout, QVBoxLayout, \
    QMainWindow

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() // 2 - 2 * PADDING, 325)


class MainWidget(QMainWindow):
    font = QtGui.QFont("ttf", 16)

    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)


    def set_listeners(self):
        pass

    @staticmethod
    def start_window():
        app = QApplication(sys.argv)
        ex = MainWidget()
        ex.show()
        sys.exit(app.exec())
