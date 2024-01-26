from pygame import *

"""class"""
class GameSprite(sprite.Sprite):
    def __init__(self, player_img , player_x, player_y , player_speed ):
        super().__init__()
        # тут ми маємо написати загрузку зоображень
        self.image = transform.scale (image.load(player_img), (65,65))
        self.speed = player_speed
        #маємо зробити спрайт прямокутником
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   
    def reset(self):
        window.blit (self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def move (self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed


class Enemy (GameSprite):
    direction = "left"
    def go(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



#game scene
win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("Valery")

background = transform.scale (image.load("background.jpg"), (win_width,win_height))
player = Player("hero.png",5,win_height-80, 4)
monster =Enemy("cyborg.png",win_width-80, 280 , 2)
final =GameSprite("treasure.png",win_width-120,win_height - 80,0)

#w1=Wall(154,205,50,100,50,350,10)
#w2=Wall(154,205,50,100,400,350,10)
#w3=Wall(154,205,50,100,0,10,300)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font=font.Font(None,70)
win=font.render('YOU WIN!',True,(233,215,0))
lose=font.render('YOU LOSE!',True,(160,0,0))

#musicІ
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money=mixer.Sound('money.ogg')
kick=mixer.Sound('kick.ogg')


while game :
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        #w1.draw_wall()
        #w2.draw_wall()
        #w3.draw_wall()

    #ситуація Програш
    if sprite.collide_rect(player,monster) or sprite.collide_rect:
        finish=True
        window.blit(lose,(200,200))
        kick.play()

    #ситуація Перемога
    if sprite.collide_rect(player,monster):
        finish=True
        window.blit(win,(200,200))
        money.play()

    display.flip()  #display.update()
    clock.tick(FPS)


