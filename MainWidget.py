import WindowPresenter

import sys
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QScrollArea, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QStyledItemDelegate, QLineEdit, QTableWidgetItem, QDialog, QHBoxLayout, QVBoxLayout

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() // 2 - 2 * PADDING, 325)


class MainWidget(QWidget):
    font = QtGui.QFont("ttf", 16)

    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.scroll_area = QScrollArea()

        right_layout.addWidget(self.scroll_area)

        menu_layout = QHBoxLayout()

        self.curve_type_selector = QComboBox(self)
        self.run_button = QPushButton(self)
        menu_layout.addWidget(self.curve_type_selector)
        menu_layout.addWidget(self.run_button)
        left_layout.addLayout(menu_layout)

        self.setLayout(main_layout)
        self.set_listeners()

    def set_listeners(self):
        pass

    @staticmethod
    def start_window():
        app = QApplication(sys.argv)
        ex = MainWidget()
        ex.show()
        sys.exit(app.exec())
