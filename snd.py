from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def win():
    victory = QMessageBox()
    victory.setText("Nice Job")
    victory.exec()

def lose():
    loser = QMessageBox()
    loser.setText("Loser")
    loser.exec()

app = QApplication([])

main = QWidget()
main.setWindowTitle("Лохотрон")  # Changed the window title to use Cyrillic characters
main.resize(400, 200)

que = QLabel("Чому пан Максім не робить дз?")
an1 = QRadioButton("ілля заважає")
an2 = QRadioButton("школа заважає")
an3 = QRadioButton("Лінь")
an4 = QRadioButton("друзі")

layout_main = QVBoxLayout()
lat_h1 = QHBoxLayout()
lat_h2 = QHBoxLayout()
lat_h3 = QHBoxLayout()
lat_h4 = QHBoxLayout()

lat_h1.addWidget(que, alignment=Qt.AlignCenter)
lat_h2.addWidget(an1, alignment=Qt.AlignCenter)
lat_h3.addWidget(an2, alignment=Qt.AlignCenter)
lat_h4.addWidget(an3, alignment=Qt.AlignCenter)
lat_h4.addWidget(an4, alignment=Qt.AlignCenter)  # Changed from lat_h3 to lat_h4 to keep consistent

layout_main.addLayout(lat_h1)
layout_main.addLayout(lat_h2)
layout_main.addLayout(lat_h3)
layout_main.addLayout(lat_h4)

main.setLayout(layout_main)

an1.clicked.connect(win)
an2.clicked.connect(lose)
an3.clicked.connect(win)
an4.clicked.connect(lose)

main.show()
app.exec()
