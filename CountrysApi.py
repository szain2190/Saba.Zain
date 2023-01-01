from PyQt6.QtWidgets import QApplication, QComboBox, QSpacerItem,QSizePolicy,QBoxLayout, QVBoxLayout, QMainWindow, QPushButton, QLabel, QLineEdit, QGridLayout, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys
import requests
import json

#window class inherits from the main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Window")
        self.setGeometry(500,500,500,500)
        self.setMaximumSize(1000,1000)
        self.show()
        self.setup()

    def GetCapital(self):
        query = f"https://restcountries.com/v3.1/name/{self.country_menu.currentText()}"
        req = requests.get(query)
        data = req.json()
        capital = data[0]["capital"][0]
        self.label_capital.setText(capital)


    def setup(self):
        #set up widgets
        window_widget = QWidget()
        self.label_title = QLabel("Capital Finder")
        self.label_header = QLabel("Countries")
        self.country_menu = QComboBox()
        self.country_menu.addItems(["peru","spain","france"])
        self.country_menu.currentIndexChanged.connect(self.GetCapital)

        self.label_header2 = QLabel("Capital")
        self.label_capital = QLabel()



        #sets up the layout of the widgets on the screen
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.label_title)
        window_layout.addWidget(self.label_header)
        window_layout.addWidget(self.country_menu)
        window_layout.addWidget(self.label_header2)
        window_layout.addWidget(self.label_capital)


        #set up stylesheets


        #sets up the layout on the actual screen
        window_widget.setLayout(window_layout)
        self.setCentralWidget(window_widget)


app = QApplication(sys.argv) #makes an instance of the app

window = MainWindow()#makes an instance the window object
window.show()

app.exec()#mainloop


