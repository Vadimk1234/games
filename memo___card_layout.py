''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 
app=QApplication([])
# віджети, які треба буде розмістити:
btn_manu=QPushButton("Меню")
btn_sleep=QPushButton("відпочинок")

btn_min=QSpinBox()
btn_min.setValue(15)
btn_ok=QPushButton("Answer:")
lb_question=QLabel("")

# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів
radioGroupButton=QGroupBox("Варіанти відповіді")
radioGroup=QButtonGroup()
rbtn_1=QRadioButton("")
rbtn_2=QRadioButton("")
rbtn_3=QRadioButton("")
rbtn_4=QRadioButton("")
# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbtn_2)
radioGroup.addButton(rbtn_3)
radioGroup.addButton(rbtn_4)
#панель 
ans_group=QGroupBox("результати тесту")
lb_result=QLabel("")
lb_correct=QLabel("")
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radioGroupButton.setLayout(layout_ans1)
layout_res=QVBoxLayout()
layout_res.addWidget(lb_result,alignment=(Qt.Alignleft | Qt.aligntop))
layout_res.addWidget(lb_correct,alignment=(Qt.alignCenter,stretch=2))
ans_group.setLayout(layout_res)
ans_group.hide()
Layout_line1=QHBoxLayout()
Layout_line2=QHBoxLayout()
Layout_line3=QHBoxLayout()
Layout_line4=QHBoxLayout()
Layout_line1.addWidget(btn_manu)
Layout_line2.addStretch()
Layout_line2.addWidget(btn_sleep)
Layout_line2.addWidget(btn_min)
Layout_line2.addWidget(QLabel("minuts"))
Layout_line2.addWidget(lb_question,alignment=(Qt.AlignCenter | Qt.aligncente:))
Layout_line3.addWidget(radioGroupButton)
Layout_line3.addWidget(ans_group)
Layout_line4.addStretch(1)
Layout_line4.addWidget(btn_ok,stretch=2)
Layout_line4.addStretch(1)
layout_card=QVBoxLayout()
layout_card.addLayout(Layout_line1,stretch=1)
layout_card.addLayout(Layout_line2,stretch=2)
layout_card.addLayout(Layout_line3,stretch=3)
layout_card.addStretch(1)
layout_card.addLayout(Layout_line4,stretch=1)
layout_card.addStretch(1)
layout_card.setspacing(5)


