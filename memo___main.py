from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса

card_width, card_height = 600, 500 # начальные размеры окна "карточка"

def show_data():
    ''' показывает на экране нужную информацию '''
    pass

def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    pass

win_card = QWidget()
#здесь должны быть параметры окна

win_card.show()
app.exec_()