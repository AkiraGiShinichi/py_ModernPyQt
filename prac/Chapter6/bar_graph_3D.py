# bar_graph_3D.py
# Import necessary modules
import sys
import csv
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtDataVisualization import (
    Q3DBars, QBarDataItem, QBar3DSeries, QValue3DAxis, Q3DCamera)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class SimpleBarGraph(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        print(f'\ninitializeUI')
        self.setMinimumSize(800, 700)
        self.setWindowTitle('6.1 - 3D Bar Graph')

        self.setupGraph()
        self.show()

    def setupGraph(self):
        print(f'\nsetupGraph')
        pass

    def loadCSVFile(self):
        print(f'\nloadCSVFile')
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleBarGraph()
    sys.exit(app.exec_())
