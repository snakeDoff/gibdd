import Reformat as ref

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPixmap

class Rules(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.label = QLabel()
        self.label.setGeometry(0, 0, 854, 7048)
        self.label.move(0, 0)



        self.vbox.addWidget(self.label)

        self.widget.setLayout(self.vbox)


        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.show()


        self.scroll.setFixedSize(881, 600)

class Bilet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('bilet.ui', self)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.go2rules.clicked.connect(self.go2rule)
        self.go2signs.clicked.connect(self.go2sign)
        self.go2dopusks.clicked.connect(self.go2dopusk)
        self.go2bilets.clicked.connect(self.go2bilet)

    def go2rule(self):
        text = ref.rrules(self.PddRules.currentText())

        self.w2 = Rules()
        self.w2.scroll.setWindowTitle(text[0])
        self.w2.label.setPixmap(QPixmap(text[1]))
        self.w2.scroll.show()

    def go2sign(self):
        text = ref.rrules(self.PddSigns.currentText())

        self.w2 = Rules()
        self.w2.scroll.setWindowTitle(text[0])
        self.w2.label.setPixmap(QPixmap(text[1]))
        self.w2.scroll.show()

    def go2dopusk(self):
        text = ref.rrules(self.PddDopusk.currentText())

        self.w2 = Rules()
        self.w2.scroll.setWindowTitle(text[0])
        self.w2.label.setPixmap(QPixmap(text[1]))
        self.w2.scroll.show()

    def go2bilet(self):
        self.w2 = Bilet()
        self.w2.setWindowTitle(self.PddVariants.currentText())
        self.w2.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())