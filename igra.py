from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self. image, (self.rect.x, self.rect.y)) 




window = display.set_mode((700,500))
display.set_caption('Котобойка')
background = transform.scale(image.load('background.jpg'), (700,500))
sprite1 = GameSprite('gazeta.png',600,300,5)
sprite2 = GameSprite('gazeta.png',0,300,5)
ball = GameSprite('cat.png',200,200,5)
fps=60
game = True
finish = False
speed_x = 3
speed_y = 3
chasi=time.Clock()
font.init()
font =font.SysFont('Arial',70)
lose = font.render('домой.',True, (180,0,0))
while game:
    window.blit(background,(0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:    
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_UP] and sprite1.rect.y >0:
            sprite1.rect.y -= 5
        if  keys_pressed[K_DOWN] and sprite1.rect.y <400:
            sprite1.rect.y += 5
        if  keys_pressed[K_w] and sprite2.rect.y >0:
            sprite2.rect.y -= 5
        if  keys_pressed[K_s] and sprite2.rect.y <400:
            sprite2.rect.y += 5
       
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(sprite1,ball) or sprite.collide_rect(sprite2,ball):
            speed_x *= -1
        if (ball.rect.y<=0) or (ball.rect.y>=430):
            speed_y*=-1
        if (ball.rect.x <=10):
            
            window.blit(lose,(50,200))
            display.update()
            time.wait(200)
            finish = True
        if  (ball.rect.x > 680):
            
            window.blit(lose,(350,200))
            display.update()
            time.wait(200)
            finish = True

        sprite1.reset()
        sprite2.reset()
        ball.reset()
        chasi.tick(fps)
        display.update()



