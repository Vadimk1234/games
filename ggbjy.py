class Widget():
    def __init__(self,title_text,x_num,y_num):
        self.title=title_text
        self.x=x_num
        self.y=y_num
    def kvazimodo(self):
        print("Напис:",self.title)
        print("Розташування:",self.x,self.y)
class button(Widget):
    def __init__(self, title_text,x_num,y_num,is_clicked):
        super().__init__(title_text, x_num, y_num)
        self.is_clicked=is_clicked
    def clicked(self):
        self.is_clicked=True
        print("Ви зареєстровані")
loat=button("брати участь",100,100,False)
loat.kvazimodo()
a=input("Так\ні")
if a =="Так":
    loat.clicked()
else:
    print("losser")

