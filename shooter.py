from pygame import*
from random import randint

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound=mixer.Sound("fire.ogg")


img_back="galaxy.jpg"
img_here="rocket.png"
img_enemy="ufo.png"
img_bullet="bullet.png"


font.init()
font1=font.Font(None,36)
font2=font.Font(None,76)
win=font2.render("YOU WIN",True,(0,255,0))
lose=font2.render("LOSE YOU",True,(255,0,0))

lost=0
score=0
max_lost=5


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image =transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect_x=player_x
        self.rect_y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_wight - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet,self.rect.x,self.rect.top,20,10,-15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_wight-80)
            self.rect.y = 0
            lost +=1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_wight= 700
win_height=500
window = display.set_mode((win_wight,win_height))
display.set_caption("shooter")
background=transform.scale(image.load(img_back),(win_wight,win_height))
bullets = sprite.Group()
monsters = sprite.Group()

for i in range(1,6):
    monster=Enemy(img_enemy,randint(80,win_wight-80),-40,80,50,randint(1,6))
    monsters.add(monster)

player=Player(img_here,5,win_height - 100,80,100,10)

game_over=False
start=True

while start:
    for e in event.get():
        if e.type == QUIT:
            start = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire_sound.play()

    if not game_over:
        window.blit(background,(0,0))
        text_score = font1.render("Score:",str(score),(255,255,255))
        window.blit(text_score,(10,20))
        text_lose = font1.render("Lose:",str(score),(255,255,255))
        window.blit(background,(0,0))
        player.update()
        monsters.update()
        bullets.update()
        player.reset()
        monsters.draw(window)
        

        display.flip()
    time.delay(50)
