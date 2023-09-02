class Button():
    def __init__(self,title_text,x_num,y_num):
        self.title=title_text
        self.x=x_num
        self.y=y_num
        self.apperance=True
    def hide(self):
        self.apperance=False
    def show(self):
        self.apperance=True
    def status(self):
        print("Дані про віджет")
        print(self.title,self.x,self.y,self.apperance)
ok_but=Button("ok",100,100)
ok_but.status()
ok_but.hide()
ok_but.status()
