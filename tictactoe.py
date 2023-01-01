from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

import sys

#window class inherites from the main window, init like a constructer sets up object
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,500)

        self.setGui()

        self.show()

        self.turn = 0


    def setGui(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(20,20,80,80)
        self.button1.clicked.connect(self.buttonClicked)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(110,20,80,80)
        self.button2.clicked.connect(self.buttonClicked)
        
        self.button3 = QPushButton(self)
        self.button3.setGeometry(200,20,80,80)
        self.button3.clicked.connect(self.buttonClicked)

        self.button4 = QPushButton(self)
        self.button4.setGeometry(20,110,80,80)
        self.button4.clicked.connect(self.buttonClicked)
        self.button5 = QPushButton(self)
        self.button5.setGeometry(110,110,80,80)
        self.button5.clicked.connect(self.buttonClicked)
        self.button6 = QPushButton(self)
        self.button6.setGeometry(200,110,80,80)
        self.button6.clicked.connect(self.buttonClicked)
        self.button7 = QPushButton(self)
        self.button7.setGeometry(20,200,80,80)
        self.button7.clicked.connect(self.buttonClicked)
        self.button8 = QPushButton(self)
        self.button8.setGeometry(110,200,80,80)
        self.button8.clicked.connect(self.buttonClicked)
        self.button9 = QPushButton(self)
        self.button9.setGeometry(200,200,80,80)
        self.button9.clicked.connect(self.buttonClicked)

        self.label = QLabel(self)
        self.label.setGeometry(20,300,260,60)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}")

        self.buttonreset = QPushButton("Reset-Game",self)
        self.buttonreset.setGeometry(50,380,200,50)
        self.buttonreset.clicked.connect(self.reset)

    def reset(self):
        self.label.setText("")
        self.button1.setText("")
        self.button1.setEnabled(True)
        self.turn = 0

    def buttonClicked(self):
        self.turn += 1
        button = self.sender()

        if self.turn%2:
            button.setText("X")
        else:
            button.setText("O")

        button.setEnabled(False)

        win = self.checkWin()

        if win:
            self.label.setText("Winner, winner chicken dinner")


    def checkWin(self):
        #rows
        if self.button1.text() == self.button2.text() \
            and self.button2.text() == self.button3.text() \
            and self.button1.text() != "":
            return True
        if self.button4.text() == self.button5.text() \
            and self.button5.text() == self.button6.text() \
            and self.button4.text() != "":
            return True
        if self.button7.text() == self.button8.text() \
            and self.button8.text() == self.button9.text() \
            and self.button7.text() != "":
            return True

        #columns
        if self.button1.text() == self.button4.text() \
            and self.button4.text() == self.button7.text() \
            and self.button1.text() != "":
            return True
        if self.button2.text() == self.button5.text() \
            and self.button5.text() == self.button8.text() \
            and self.button2.text() != "":
            return True
        if self.button3.text() == self.button6.text() \
            and self.button6.text() == self.button9.text() \
            and self.button3.text() != "":
            return True

        #diagonals
        if self.button1.text() == self.button5.text() \
            and self.button5.text() == self.button9.text() \
            and self.button1.text() != "":
            return True
        if self.button3.text() == self.button5.text() \
            and self.button5.text() == self.button7.text() \
            and self.button3.text() != "":
            return True

        


#""

app = QApplication(sys.argv) #makes an instance of the app

window = Window()#makes an instance the window object

app.exec()#mainloop
