import Reformat as ref

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPixmap
import sqlite3
import random
import datetime as dt

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

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('exam.ui', self)
        self.timer = self.timer

class Bilet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('bilet.ui', self)
        self.timer = self.timer


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.go2rules.clicked.connect(self.go2rule)
        self.go2signs.clicked.connect(self.go2sign)
        self.go2dopusks.clicked.connect(self.go2dopusk)
        self.go2bilets.clicked.connect(self.go2bilet)
        self.go2exams.clicked.connect(self.go2exam)

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

    def tick_timer(self):
        timer = QTimer()
        if self.a != dt.time(0, 0, 0):
            self.a = self.a - dt.timedelta(seconds=1)
            self.w2.timer.setText(self.a.strftime("%M:%S"))
            timer.singleShot(1000, self.tick_timer)
        else:
            timer.isActive(False)


    def go2bilet(self):
        self.w2 = Bilet()
        self.w2.setWindowTitle(self.PddVariants.currentText())
        self.w2.show()
        self.a = dt.datetime(20, 1, 1, 0, 0, 0)
        self.a = dt.datetime(20, 1, 1, 0, 20, 0)
        self.tick_timer()
        self.variant = ref.rrules(self.PddVariants.currentText())
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        self.questions = cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                    WHERE variant = {self.variant}""").fetchall()
        con.close()
        self.w2.ans1.clicked.connect(self.answer)
        self.w2.ans2.clicked.connect(self.answer)
        self.w2.ans3.clicked.connect(self.answer)
        self.w2.ans4.clicked.connect(self.answer)
        self.w2.g2.clicked.connect(self.chose)
        self.w2.g1.clicked.connect(self.chose)
        self.w2.g3.clicked.connect(self.chose)
        self.w2.g4.clicked.connect(self.chose)
        self.w2.g5.clicked.connect(self.chose)
        self.w2.g7.clicked.connect(self.chose)
        self.w2.g8.clicked.connect(self.chose)
        self.w2.g9.clicked.connect(self.chose)
        self.w2.g10.clicked.connect(self.chose)
        self.w2.g11.clicked.connect(self.chose)
        self.w2.g12.clicked.connect(self.chose)
        self.w2.g13.clicked.connect(self.chose)
        self.w2.g14.clicked.connect(self.chose)
        self.w2.g15.clicked.connect(self.chose)
        self.w2.g16.clicked.connect(self.chose)
        self.w2.g17.clicked.connect(self.chose)
        self.w2.g18.clicked.connect(self.chose)
        self.w2.g19.clicked.connect(self.chose)
        self.w2.g20.clicked.connect(self.chose)
        self.w2.g6.clicked.connect(self.chose)
        self.prevb = self.w2.g1
        self.prev = 1
        self.c = 0
        self.t = 0
        self.w2.ans1.hide()
        self.w2.ans2.hide()
        self.w2.ans3.hide()
        self.w2.ans4.hide()




        self.stat = {'1': (0, 0), '2': (0, 0), '3': (0, 0), '4': (0, 0), '5': (0, 0), '6': (0, 0), '7': (0, 0),
                     '8': (0, 0), '9': (0, 0), '10': (0, 0), '11': (0, 0), '12': (0, 0), '13': (0, 0), '14': (0, 0),
                     '15': (0, 0), '16': (0, 0), '17': (0, 0), '18': (0, 0), '19': (0, 0), '20': (0, 0)}
    def chose(self):
        self.w2.ans1.setDisabled(False)
        self.w2.ans2.setDisabled(False)
        self.w2.ans3.setDisabled(False)
        self.w2.ans4.setDisabled(False)
        self.current = int(self.sender().text())
        if str(self.questions[self.current - 1][1]) != 'empty':
            self.w2.ans1.setText(str(self.questions[self.current - 1][1]))
            self.w2.ans1.show()
        else:
            self.w2.ans1.hide()
        if str(self.questions[self.current - 1][2]) != 'empty':
            self.w2.ans2.setText(str(self.questions[self.current - 1][2]))
            self.w2.ans2.show()
        else:
            self.w2.ans3.hide()
        if str(self.questions[self.current - 1][3]) != 'empty':
            self.w2.ans3.setText(str(self.questions[self.current - 1][3]))
            self.w2.ans3.show()
        else:
            self.w2.ans3.hide()
        if str(self.questions[self.current - 1][4]) != 'empty':
            self.w2.ans4.setText(str(self.questions[self.current - 1][4]))
            self.w2.ans4.show()
        else:
            self.w2.ans4.hide()
        self.w2.question.setPixmap(QPixmap(self.questions[self.current - 1][0]))
        self.w2.poyas.setPixmap(QPixmap(self.questions[self.current - 1][6]))
        self.w2.poyas.hide()
        self.w2.sender().setStyleSheet('background: rgb(0,125,125);')
        self.curbuton = self.w2.sender()
        self.w2.ans1.setStyleSheet('background: rgb(225,225,225);')
        self.w2.ans2.setStyleSheet('background: rgb(225,225,225);')
        self.w2.ans3.setStyleSheet('background: rgb(225,225,225);')
        self.w2.ans4.setStyleSheet('background: rgb(225,225,225);')
        if self.stat[str(self.current)][0] == 1:
            if self.w2.ans1.text() == self.questions[self.current - 1][5]:
                self.w2.ans1.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans2.text() == self.questions[self.current - 1][5]:
                self.w2.ans2.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans3.text() == self.questions[self.current - 1][5]:
                self.w2.ans3.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans4.text() == self.questions[self.current - 1][5]:
                self.w2.ans4.setStyleSheet('background: rgb(0,255,125);')
            self.w2.ans1.setDisabled(True)
            self.w2.ans2.setDisabled(True)
            self.w2.ans3.setDisabled(True)
            self.w2.ans4.setDisabled(True)
            self.w2.poyas.show()
        elif self.stat[str(self.current)][0] == 2:
            if self.stat[str(self.current)][1] == 1:
                self.w2.ans1.setStyleSheet('background: rgb(255,20,0);')
            if self.stat[str(self.current)][1] == 2:
                self.w2.ans2.setStyleSheet('background: rgb(255,20,0);')
            if self.stat[str(self.current)][1] == 3:
                self.w2.ans3.setStyleSheet('background: rgb(255,20,0);')
            if self.stat[str(self.current)][1] == 4:
                self.w2.ans4.setStyleSheet('background: rgb(255,20,0);')
            if self.w2.ans1.text() == self.questions[self.current - 1][5]:
                self.w2.ans1.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans2.text() == self.questions[self.current - 1][5]:
                self.w2.ans2.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans3.text() == self.questions[self.current - 1][5]:
                self.w2.ans3.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans4.text() == self.questions[self.current - 1][5]:
                self.w2.ans4.setStyleSheet('background: rgb(0,255,125);')
            self.w2.ans1.setDisabled(True)
            self.w2.ans2.setDisabled(True)
            self.w2.ans3.setDisabled(True)
            self.w2.ans4.setDisabled(True)
            self.w2.poyas.show()
        if self.stat[str(self.prev)][0] == 0:
            self.prevb.setStyleSheet('background: rgb(225,225,225);')
        if self.stat[str(self.prev)][0] == 1:
            self.prevb.setStyleSheet('background: rgb(0,255,14);')
        if self.stat[str(self.prev)][0] == 2:
            self.prevb.setStyleSheet('background: rgb(255,0,14);')
        self.prevb = self.w2.sender()
        self.prev = self.current
    def endbil(self):
        if self.t != 20:
            self.w2.final_2.setText(f"Билет\n не сдан\n правильных\n ответов:\n {self.t} из 20")
            self.w2.final_2.setStyleSheet('color: rgb(255,0,14);')
            self.b = self.a
            self.a = dt.time(0, 0, 0)
            self.w2.timer.setText(self.b.strftime("%M:%S"))
        if self.t == 20:
            self.w2.final_2.setText(f"Билет\n cдан\n правильных\n ответов:\n {self.t} из 20")
            self.w2.final_2.setStyleSheet('color: rgb(0,255,14);')
            self.b = self.a
            self.a = dt.time(0, 0, 0)
            self.w2.timer.setText(self.b.strftime("%M:%S"))

    def answer(self):
        if self.w2.sender().text() == self.questions[self.current - 1][5]:
            self.w2.sender().setStyleSheet('background: rgb(0,255,125);')
            self.w2.poyas.setPixmap(QPixmap(self.questions[self.current - 1][6]))
            self.w2.ans1.setDisabled(True)
            self.w2.ans2.setDisabled(True)
            self.w2.ans3.setDisabled(True)
            self.w2.ans4.setDisabled(True)
            self.sender().setEnabled(True)
            self.curbuton.setStyleSheet('background: rgb(0,255,14);')
            self.w2.poyas.show()
            self.stat[str(self.current)] = (1, self.stat[str(self.current)][1])
            self.t += 1
        else:
            self.stat[str(self.current)] = (2, self.stat[str(self.current)][1])
            self.w2.sender().setStyleSheet('background: rgb(255,20,0);')
            self.w2.poyas.setPixmap(QPixmap(self.questions[self.current - 1][6]))
            if self.w2.ans1.text() == self.questions[self.current - 1][5]:
                self.w2.ans1.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans2.text() == self.questions[self.current - 1][5]:
                self.w2.ans2.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans3.text() == self.questions[self.current - 1][5]:
                self.w2.ans3.setStyleSheet('background: rgb(0,255,125);')
            if self.w2.ans4.text() == self.questions[self.current - 1][5]:
                self.w2.ans4.setStyleSheet('background: rgb(0,255,125);')
            self.w2.ans1.setDisabled(True)
            self.w2.ans2.setDisabled(True)
            self.w2.ans3.setDisabled(True)
            self.w2.ans4.setDisabled(True)
            self.sender().setEnabled(True)
            self.curbuton.setStyleSheet('background: rgb(255,0,14);')
            self.w2.poyas.show()
            if self.w2.ans1.text() == self.sender().text():
                self.stat[str(self.current)] = (self.stat[str(self.current)][0], 1)
            if self.w2.ans2.text() == self.sender().text():
                self.stat[str(self.current)] = (self.stat[str(self.current)][0], 2)
            if self.w2.ans3.text() == self.sender().text():
                self.stat[str(self.current)] = (self.stat[str(self.current)][0], 3)
            if self.w2.ans4.text() == self.sender().text():
                self.stat[str(self.current)] = (self.stat[str(self.current)][0], 4)
        self.c += 1
        if self.c == 20:
            self.endbil()

    def tick_timere(self):
        timer = QTimer()
        if self.trimer != dt.datetime(20, 1, 1, 0, 0, 0):
            self.trimer = self.trimer - dt.timedelta(seconds=1)
            self.w3.timer.setText(self.trimer.strftime("%M:%S"))
            timer.singleShot(1000, self.tick_timere)


    def go2exam(self):
        self.w3 = Exam()
        self.w3.setWindowTitle('Экзамен категории ABM')
        self.w3.show()
        self.trimer = dt.datetime(20, 1, 1, 0, 0, 0)
        self.trimer = dt.datetime(20, 1, 1, 0, 20, 0)
        self.tick_timere()
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        self.block1v = (random.randrange(1,5), 1)
        self.block2v = (random.randrange(1,5), 2)
        self.block3v = (random.randrange(1,5), 3)
        self.block4v = (random.randrange(1,5), 4)
        self.questions = cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                    WHERE variant = {self.block1v[0]} and block = 1""").fetchall()
        self.questions = self.questions + cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                    WHERE variant = {self.block2v[0]} and block = 2""").fetchall()
        self.questions = self.questions + cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                            WHERE variant = {self.block3v[0]} and block = 3""").fetchall()
        self.questions = self.questions + cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                            WHERE variant = {self.block4v[0]} and block = 4""").fetchall()
        con.close()
        self.w3.g21.hide()
        self.w3.g22.hide()
        self.w3.g23.hide()
        self.w3.g24.hide()
        self.w3.g25.hide()
        self.w3.g26.hide()
        self.w3.g27.hide()
        self.w3.g28.hide()
        self.w3.g29.hide()
        self.w3.g30.hide()
        self.w3.ans1.hide()
        self.w3.ans2.hide()
        self.w3.ans3.hide()
        self.w3.ans4.hide()
        self.w3.g1.clicked.connect(self.choseEX)
        self.w3.g2.clicked.connect(self.choseEX)
        self.w3.g3.clicked.connect(self.choseEX)
        self.w3.g4.clicked.connect(self.choseEX)
        self.w3.g5.clicked.connect(self.choseEX)
        self.w3.g6.clicked.connect(self.choseEX)
        self.w3.g7.clicked.connect(self.choseEX)
        self.w3.g8.clicked.connect(self.choseEX)
        self.w3.g9.clicked.connect(self.choseEX)
        self.w3.g10.clicked.connect(self.choseEX)
        self.w3.g11.clicked.connect(self.choseEX)
        self.w3.g12.clicked.connect(self.choseEX)
        self.w3.g13.clicked.connect(self.choseEX)
        self.w3.g14.clicked.connect(self.choseEX)
        self.w3.g15.clicked.connect(self.choseEX)
        self.w3.g16.clicked.connect(self.choseEX)
        self.w3.g17.clicked.connect(self.choseEX)
        self.w3.g18.clicked.connect(self.choseEX)
        self.w3.g19.clicked.connect(self.choseEX)
        self.w3.g20.clicked.connect(self.choseEX)
        self.w3.g21.clicked.connect(self.choseEX)
        self.w3.g22.clicked.connect(self.choseEX)
        self.w3.g23.clicked.connect(self.choseEX)
        self.w3.g24.clicked.connect(self.choseEX)
        self.w3.g25.clicked.connect(self.choseEX)
        self.w3.g26.clicked.connect(self.choseEX)
        self.w3.g27.clicked.connect(self.choseEX)
        self.w3.g28.clicked.connect(self.choseEX)
        self.w3.g29.clicked.connect(self.choseEX)
        self.w3.g30.clicked.connect(self.choseEX)
        self.w3.ans1.clicked.connect(self.answerEX)
        self.w3.ans2.clicked.connect(self.answerEX)
        self.w3.ans3.clicked.connect(self.answerEX)
        self.w3.ans4.clicked.connect(self.answerEX)
        self.ended = False
        self.overtime1 = False
        self.overtime2 = False
        self.c = 0
        self.t = 0
        self.stat = {'1': (0, 0), '2': (0, 0), '3': (0, 0), '4': (0, 0), '5': (0, 0), '6': (0, 0), '7': (0, 0),
                     '8': (0, 0), '9': (0, 0), '10': (0, 0), '11': (0, 0), '12': (0, 0), '13': (0, 0), '14': (0, 0),
                     '15': (0, 0), '16': (0, 0), '17': (0, 0), '18': (0, 0), '19': (0, 0), '20': (0, 0),
                     '21': (0, 0), '22': (0, 0), '23': (0, 0), '24': (0, 0), '25': (0, 0), '26': (0, 0),
                     '27': (0, 0), '28': (0, 0), '29': (0, 0), '30': (0, 0)}

    def choseEX(self):
        self.w3.ans1.setDisabled(False)
        self.w3.ans2.setDisabled(False)
        self.w3.ans3.setDisabled(False)
        self.w3.ans4.setDisabled(False)
        self.current = int(self.sender().text())
        self.w3.sender().setStyleSheet('background: rgb(0,125,125);')
        if str(self.questions[self.current - 1][1]) != 'empty':
            self.w3.ans1.setText(str(self.questions[self.current - 1][1]))
            self.w3.ans1.show()
        else:
            self.w3.ans1.hide()
        if str(self.questions[self.current - 1][2]) != 'empty':
            self.w3.ans2.setText(str(self.questions[self.current - 1][2]))
            self.w3.ans2.show()
        else:
            self.w3.ans3.hide()
        if str(self.questions[self.current - 1][3]) != 'empty':
            self.w3.ans3.setText(str(self.questions[self.current - 1][3]))
            self.w3.ans3.show()
        else:
            self.w3.ans3.hide()
        if str(self.questions[self.current - 1][4]) != 'empty':
            self.w3.ans4.setText(str(self.questions[self.current - 1][4]))
            self.w3.ans4.show()
        else:
            self.w3.ans4.hide()
        self.w3.question.setPixmap(QPixmap(self.questions[self.current - 1][0]))
        self.w3.poyas.setPixmap(QPixmap(self.questions[self.current - 1][6]))
        self.w3.poyas.hide()
        self.curbuton = self.w3.sender()
        self.w3.ans1.setStyleSheet('background: rgb(225,225,225);')
        self.w3.ans2.setStyleSheet('background: rgb(225,225,225);')
        self.w3.ans3.setStyleSheet('background: rgb(225,225,225);')
        self.w3.ans4.setStyleSheet('background: rgb(225,225,225);')
        if self.stat[str(self.current)][0] == 1:
            if self.w3.ans1.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans1.setStyleSheet('background: rgb(0,255,125);')
                self.w3.poyas.show()
            if self.w3.ans2.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans2.setStyleSheet('background: rgb(0,255,125);')
                self.w3.poyas.show()
            if self.w3.ans3.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans3.setStyleSheet('background: rgb(0,255,125);')
                self.w3.poyas.show()
            if self.w3.ans4.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans4.setStyleSheet('background: rgb(0,255,125);')
                self.w3.poyas.show()
            self.w3.ans1.setDisabled(True)
            self.w3.ans2.setDisabled(True)
            self.w3.ans3.setDisabled(True)
            self.w3.ans4.setDisabled(True)
        elif self.stat[str(self.current)][0] == 2:
            if self.stat[str(self.current)][1] == 1 and self.ended:
                self.w3.ans1.setStyleSheet('background: rgb(255,20,0);')
                self.w3.poyas.show()
            if self.stat[str(self.current)][1] == 2 and self.ended:
                self.w3.ans2.setStyleSheet('background: rgb(255,20,0);')
                self.w3.poyas.show()
            if self.stat[str(self.current)][1] == 3 and self.ended:
                self.w3.ans3.setStyleSheet('background: rgb(255,20,0);')
                self.w3.poyas.show()
            if self.stat[str(self.current)][1] == 4 and self.ended:
                self.w3.ans4.setStyleSheet('background: rgb(255,20,0);')
                self.w3.poyas.show()
            if self.w3.ans1.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans1.setStyleSheet('background: rgb(0,255,125);')
            if self.w3.ans2.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans2.setStyleSheet('background: rgb(0,255,125);')
            if self.w3.ans3.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans3.setStyleSheet('background: rgb(0,255,125);')
            if self.w3.ans4.text() == self.questions[self.current - 1][5] and self.ended:
                self.w3.ans4.setStyleSheet('background: rgb(0,255,125);')
            self.w3.ans1.setDisabled(True)
            self.w3.ans2.setDisabled(True)
            self.w3.ans3.setDisabled(True)
            self.w3.ans4.setDisabled(True)
            self.prevb = self.w3.sender()
            self.prev = self.current

    def go2over1(self):
        self.w3.g21.show()
        self.w3.g22.show()
        self.w3.g23.show()
        self.w3.g24.show()
        self.w3.g25.show()
        self.trimer = self.trimer + dt.timedelta(minutes=5)
        self.overtime1 = True
        
        
    def go2over2(self):
        self.w3.g26.show()
        self.w3.g27.show()
        self.w3.g28.show()
        self.w3.g29.show()
        self.w3.g30.show()
        self.trimer = self.trimer + dt.timedelta(minutes=5)
        self.overtime2 = True
    
    def endex(self):
        self.ended = True
        if self.t < 18:
            self.w3.final_2.setText(f"Экзамен\n не сдан\n правильных\n ответов:\n {self.t} из 20")
            self.w3.final_2.setStyleSheet('color: rgb(255,0,14);')
            self.b = self.trimer
            self.trimer = dt.datetime(20, 1, 1, 0, 0, 0)
            self.w3.timer.setText(self.b.strftime("%M:%S"))
        if self.t == 20:
            self.w3.final_2.setText(f"Экзамен\n cдан\n правильных\n ответов:\n {self.t} из 20")
            self.w3.final_2.setStyleSheet('color: rgb(0,255,14);')
            self.b = self.trimer
            self.trimer = dt.datetime(20, 1, 1, 0, 0, 0)
            self.w3.timer.setText(self.b.strftime("%M:%S"))
        if self.t == 24 and self.overtime2 is False:
            self.w3.final_2.setText(f"Экзамен\n cдан\n правильных\n ответов:\n {self.t} из 25")
            self.w3.final_2.setStyleSheet('color: rgb(0,255,14);')
            self.b = self.trimer
            self.trimer = dt.datetime(20, 1, 1, 0, 0, 0)
            self.w3.timer.setText(self.b.strftime("%M:%S"))
        if self.t == 28:
            self.w3.final_2.setText(f"Экзамен\n cдан\n правильных\n ответов:\n {self.t} из 30")
            self.w3.final_2.setStyleSheet('color: rgb(0,255,14);')
            self.b = self.trimer
            self.trimer = dt.datetime(20, 1, 1, 0, 0, 0)
            self.w3.timer.setText(self.b.strftime("%M:%S"))



    def answerEX(self):
        if self.w3.sender().text() == self.questions[self.current - 1][5]:
            self.w3.ans1.setDisabled(True)
            self.w3.ans2.setDisabled(True)
            self.w3.ans3.setDisabled(True)
            self.w3.ans4.setDisabled(True)
            self.stat[str(self.current)] = (1, self.stat[str(self.current)][1])
            self.t += 1
        else:
            self.stat[str(self.current)] = (2, self.stat[str(self.current)][1])
            self.w3.ans1.setDisabled(True)
            self.w3.ans2.setDisabled(True)
            self.w3.ans3.setDisabled(True)
            self.w3.ans4.setDisabled(True)

        self.c += 1
        if self.c == 20 and self.t == 19:
            missedblock1 = 0
            for i in self.stat:
                if self.stat[i][1] == 2:
                    que = int(i)
                if que <= 5:
                    missedblock1 = 1
                    misap = self.block1v
                elif que > 5 and que <= 10:
                    missedblock1 = 2
                    misap = self.block2v
                elif que > 10 and que <= 15:
                    missedblock1 = 3
                    misap = self.block3v
                elif que > 15 and que <= 20:
                    missedblock1 = 4
                    misap = self.block4v
            con = sqlite3.connect("base.db")
            cur = con.cursor()
            f = True
            vari = random.randrange(1,5)
            while f:
                if vari != misap[0]:
                    f = False
                else:
                    vari = random.randrange(1, 5)
            self.questions = self.questions + cur.execute(f"""SELECT question, firstu, secondu, firdu, fourth, rightu, poyas FROM questions
                                WHERE variant = {vari} and block = {missedblock1}""").fetchall()
            con.close()


        self.go2over1()
        if self.c == 20 and self.t == 18:
            self.go2over1()
            self.go2over2()
        if self.c == 20:
            self.endex()
        if self.c == 25:
            self.endex()
        if self.c == 30:
            self.endex()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())