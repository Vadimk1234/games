from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json

app = QApplication([])


notes = {
    "Good day its smart NOTES":{
        "text":"Best app",
        "tegs":["max","oleg"]
    }
}
with open ("notes.json","w") as file :
    json.dump(notes,file)


# параметри вікна програми
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

# віджети вікна програми
list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')


button_note_create = QPushButton('Створити замітку') # з'являється вікно з полем "Введіть ім'я замітки"
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')


# розташування віджетів по лейаутах
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItem(notes[key]["tags"])

def save_notes(): 
    if list_notes.selectedItems(): 
      key = list_notes.selectedItems()[0].text() 
      notes[key]["текст"] = field_tag.toPlainText() 
      with open("notes_data.json", "w") as file: 
        json.dump(notes,file,sort_keys=True,ensure_ascii=False)     
        print(notes) 
    else: 
       print("ти не зберигаеш ") 
def del_notes(): 
    if list_notes.selectedItems(): 
        key = list_notes.selectedItems()[0].text() 
        del notes[key] 
        list_notes.clear() 
        list_tags.clear() 
        field_text.clear() 
        list_notes.addItems(notes) 
        with open("notes_data.json", "w") as file: 
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)     
        print(notes) 
    else: 
        print("ти не зберигаеш ") 
 
def add_tags(): 
    if list_notes.selectedItems(): 
        key = list_notes.selectedItems()[0].text() 
        tag = field_tag.text() 
        if not tag in notes[key]["тегс"]: 
            notes[key]["теги"].append(tag) 
            list_tags.addItems(tag) 
            field_tag.clear() 
            with open("notes_data.json", "w") as file: 
                json.dump(notes,file,sort_keys=True,ensure_ascii=False)     
            print(notes) 
    else: 
            print("ти не зберигаеш ") 
 
def del_tags(): 
    if list_notes.selectedItems(): 
        key = list_notes.selectedItems()[0].text() 
        tag = field_tag.text() 
        notes[key]["тегс"].remove(tag) 
        list_tags.clear() 
        list_tags.addItems(notes[key]["теги"]) 
        with open("notes_data.json", "w") as file: 
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)     
        print(notes) 
    else: 
        print("ти ніц не вибрал ніц для видалення тегів") 
         
def search_tags(): 
    print(button_tag_search.text()) 
    tag = field_tag 
    if button_tag_search.text() == " шукати замітки по тегу" and tag: 
        print(tag) 
        notes_filtred = {} 
        for note in notes: 
            if tag in notes[note]["теги"]: 
                notes_filtred[note]==notes[note] 
        button_note_create.setText("Скинути") 
        list_notes.clear() 
        list_tags.clear() 
        list_notes.addItems(notes_filtred) 
        print(button_tag_search.text()) 
    elif button_tag_search.text() == "скинути замітку": 
        list_notes.clear() 
        list_tags.clear() 
        field_tag.clear() 
        list_notes.addItems(notes) 
        button_tag_search.setText("шукати замітки по тегу") 
        print(notes) 
    else: 
        pass

notes.itemCliked.connect(show_note)

# запуск програми
notes_win.show()
with open ("notes_data.json","r") as file :
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()
