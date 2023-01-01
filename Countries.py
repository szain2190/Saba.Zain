from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
import sys
import requests
import json
import random

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Country API")
        self.setGeometry(200,200,400,200)

        request = requests.get("https://restcountries.com/v3.1/all")
        self.data = request.json()
        f = open("countries.json","w")
        json.dump(self.data,f)
        f.close()

        self.label_country = QLabel("Country:")
        self.label_data = QLabel(self.data[0]["name"]["common"])
        self.label_capital = QLabel("Capital:")
        self.label_capital_data = QLabel(self.data[0]["capital"][0])
        button_random = QPushButton("Random country")
        button_random.clicked.connect(self.random_country)

        self.label_search = QLabel("Search for: ")
        self.entry = QLineEdit()
        self.button_search = QPushButton("Search country")
        self.button_search.clicked.connect(self.search_country)
        self.label_question = QLabel("What is the capital of: ")
        self.label_country_question = QLabel()
        self.entry_country = QLineEdit()
        self.button_question = QPushButton("New question")
        self.button_question.clicked.connect(self.new_question)
        self.button_answer = QPushButton("Check answer")
        self.button_answer.clicked.connect(self.check_answer)
        self.label_answer = QLabel()




        window_layout = QGridLayout()
        window_layout.addWidget(self.label_country,0,0)
        window_layout.addWidget(self.label_data,0,1)
        window_layout.addWidget(self.label_capital,1,0)
        window_layout.addWidget(self.label_capital_data,1,1)
        window_layout.addWidget(button_random,2,0,1,2)
        window_layout.addWidget(self.label_search,3,0)
        window_layout.addWidget(self.entry,3,1)
        window_layout.addWidget(self.button_search,4,0,1,2)
        window_layout.addWidget(self.label_question,5,0)
        window_layout.addWidget(self.label_country_question,5,1)
        window_layout.addWidget(self.entry_country,6,0,1,2)
        window_layout.addWidget(self.button_question,7,0)
        window_layout.addWidget(self.button_answer,7,1)
        window_layout.addWidget(self.label_answer,8,0,1,2)
        
        
        
        widget = QWidget()
        widget.setLayout(window_layout)
        self.setCentralWidget(widget)


    def random_country(self):
        num = random.randint(0,len(self.data)-1)
        self.label_data.setText(self.data[num]["name"]["common"])
        self.label_capital_data.setText(self.data[num]["capital"][0])

    def search_country(self):
        entry = self.entry.text()
        for country in self.data:
            if country["name"]["common"] == entry:
                self.label_data.setText(country["name"]["common"])
                self.label_capital_data.setText(country["capital"][0])

    def new_question(self):
        num = random.randint(0,len(self.data)-1)
        self.label_country_question.setText(self.data[num]["name"]["common"])

    def check_answer(self):
        entry = self.entry_country.text()
        for country in self.data:
            if country["name"]["common"] == self.label_country_question.text():
                if country["capital"][0] == entry:
                    self.label_answer.setText("correct")
                    return
                else:
                    self.label_answer.setText(f"incorrect. The answer is {country['capital'][0]}")





        # self.label_data.setText("hello")

    



app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()

