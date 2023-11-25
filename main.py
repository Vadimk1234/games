from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

#открой файл с оригиналом картинки
with Image.open("original.jpg")as mops_org:
    print("size",mops_org.size)
    print("size",mops_org.format)
    print("size",mops_org.mode)

#сделай оригинал изображения чёрно-белым
    pic_gray= mops_org.convert('L')
    pic_gray.save("mopsgray.jpg")
    print("Type:",pic_gray.mode)
    #pic_gray.show()
#сделай оригинал изображения размытым
    pic_blured=mops_org.filter(ImageFilter.BLUR)
    #pic_blured.show()
#поверни оригинал изображения на 180 градусов
    pic_up = mops_org.transpose(Image.ROTATE_180)
    #pic_up.show()
    class ImageEnhance():
        def __init__(self, file_name):
            self.file_name = file_name
            self.original = None
            self.changed = list()

        def open(self):
            try:
                self.original = Image.open(self.file_name)
            except :
                print("None")
            self.original.show()
        def do_left(self):
            rotated=self.original.transpose(Image.FLIP_LEFT_RIGHT)
            self.changed.append(rotated)
            rotated.save()

        def do_cropped(self):
            box=(250,100,600,460)
            cropped = self.original.crop(box)
            self.changed.append(cropped)
            temp_filename= self.filename.split("")
            new_filename= temp_filename[0] + str(len(self.change)) + '.jpg'
            cropped.save(new_filename)