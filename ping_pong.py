from pygame import *
from time import time as timer

FPS = 60
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
speed_x = 4
speed_y = 4
finish = False
point_l = 0
point_r = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): 
        super().__init__()

        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 



racket_r = Player('racket.png', 30, 200, 4, 50, 150)
racket_l = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 50, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
loseL = font1.render('PLAYER LEFT LOSE!', True, (180, 0, 0))
loseR = font1.render('PLAYER RIGHT LOSE!', True, (180, 0, 0))


while game:
    point_l = 0
    point_r = 0
    for e in event.get():
        if e.type == QUIT:
            game = False



    



    if finish != True:
        window.fill(back)
        racket_l.update_l()
        racket_r.update_r()
       
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if sprite.collide_rect(racket_r, ball):
            speed_x *= -1
            point_r += 1

        if sprite.collide_rect(racket_l, ball):
            speed_x *= -1
            point_l += 1

        if ball.rect.y > 460 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 50:  
            fiish = True 
            window.blit(loseL, (175, 200))

        if ball.rect.x > 550:
            finish = True
            window.blit(loseR, (175, 200))

        racket_l.reset()
        racket_r.reset()
        ball.reset()

        

    
    display.update()
    time.delay(50)


