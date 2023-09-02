from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*
app=QApplication([])
win=QWidget()
win.setWindownTitle("Win picker")
win.move(100,100)
win.resize(400,200)
button=QPushButton("Generate")
text=QLabel("Press and get know winner")
winer=QLabel("")
line=QHBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(winer,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)
win.setLayout(line)
def show():
    number=randint(0,99)
    winer.setText(str(number))
    text.setText("winner")
button.clicked.connect(show)
win.show()
app.exec_()