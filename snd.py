from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def win():
    victory=QMessageBox()
    victory.setText("Nice Job")
    victory.exec()
def lose():
    loser=QMessageBox
    loser.setText("loser")
    loser.exec()
app=QApplication([])
main=QWidget()
main.setWindowTitle("лохотрон")
main.resize(400,200)
que=QLabel("Чому пан Максім не робить дз?")
an1=QRadioButton("ілля заважає")
an2=QRadioButton("школа заважає")
an3=QRadioButton("Лінь")
an4=QRadioButton("друзі")
layout_main=QVBoxLayout()
lat_h1=QVBoxLayout()
lat_h2=QVBoxLayout()
lat_h3=QVBoxLayout()
lat_h4=QVBoxLayout()

lat_h1.addWidget(que,aligment=Qt.Alignment.AlightCenter)
lat_h2.addWidget(an1,aligment=Qt.Alignment.AlightCenter)
lat_h3.addWidget(an2,aligment=Qt.Alignment.AlightCenter)
lat_h4.addWidget(an3,aligment=Qt.Alignment.AlightCenter)
lat_h3.addWidget(an4,aligment=Qt.Alignment.AlightCenter)
layout_main.addLayout(lat_h1)
layout_main.addLayout(lat_h2)
layout_main.addLayout(lat_h3)
layout_main.addLayout(lat_h4)
layout_main.setLayout(layout_main)
an1.clicked.connect(win)
an2.clicked.connect(lose)
an3.clicked.connect(win)
an4.clicked.connect(lose)
main.show()
app.exec()