#Создай собственный Шутер!

from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Arkanoid')
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
font.init()
f1 = font.Font(None, 36)
count = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_name, speed, x, y, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_name), (sizex, sizey)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def Shoot(self):
        bullet = Bullet('bullet.png', 100, self.rect.centerx, self.rect.centery, 10,10)
        Bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global count
        if self.rect.y > 500:
            count += 1
            self.rect.y = 0
            self.rect.x = randint(20, 680)
            self.speed = randint(5, 10)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

            
player = Player('rocket.png', 15, 50, 50, 60, 60)
enemy = Enemy('ufo.png', 10, 1000, 50, 60, 60)
enemy2 = Enemy('ufo.png', 10, 1000, 50, 60, 60)
enemy3 = Enemy('ufo.png', 10, 1000, 50, 60, 60)
enemy4 = Enemy('ufo.png', 10, 1000, 50, 60, 60)
enemy5 = Enemy('ufo.png', 10, 1000, 50, 60, 60)
ufo = sprite.Group()
ufo.add(enemy)
ufo.add(enemy2)
ufo.add(enemy3)
ufo.add(enemy4)
ufo.add(enemy5)
Bullets= sprite.Group()
game = True
finish = False 
kick = mixer.Sound('fire.ogg')
while game:
    
    if finish != True:
        window.blit(background,(0, 0))
        text1 = f1.render('счёт: ' + str(count), 1, (180, 0, 0))
        window.blit(text1, (180, 60))
        player.update()
        player.reset()
        ufo.update()
        ufo.draw(window)
        Bullets.update()
        Bullets.draw(window)
        collides = sprite.groupcollide(ufo, Bullets, True, True)
        for c in collides:
            cringe = Enemy('ufo.png', 10, 1000, 50, 60, 60)
            ufo.add(cringe)
            cringe2 = Enemy('ufo.png', 10, 1000, 50, 60, 60)
            ufo.add(cringe2)
            

 

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            player.Shoot()
    display.update()



