from pygame import *


window = display.set_mode((700, 500))
display.set_caption("catch")
background = transform.scale(image.load("background.jpg"), (700, 500))



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
#parameters of the image sprite


#game loop
run = True
clock = time.Clock()
FPS = 60
speed = 10
finish = False

font.init()
font = font.Font(None,70)
win = font.render('you win!',True,(0,100,0))
lose = font.render('you lose!',True,(255,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        self.player_image = transform.scale(image.load(player_image), (100, 100))
        self.player_speed = player_speed
        self.rect = self.player_image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.player_image,(self.rect.x,self.rect.y))

class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += speed
class enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        elif self.rect.x >= 625:
            self.direction ='left'
        
        if self.direction == 'left':
            self.rect.x -= self.player_speed
        else:
            self.rect.x += self.player_speed

class wall(sprite.Sprite):
    def __init__(self,color1,color2,color3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_hight = wall_hight

        self.player_image = Surface((self.wall_width,self.wall_hight))
        self.player_image.fill((color1,color2,color3))
        self.rect = self.player_image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.player_image,(self.rect.x,self.rect.y))


hero = player("hero.png",300,200,10)
cyborg = enemy("cyborg.png",620,280,2)
treasure = GameSprite("treasure.png",400,400,0)

w1 = wall(0,100,0,100,0,600,20)
w2 = wall(0,100,0,100,0,20,400)
w3 = wall(0,100,0,100,400,300,20)

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:

        window.blit(background,(0, 0))
        hero.reset()
        cyborg.reset()
        treasure.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        hero.update()
        cyborg.update()

        if sprite.collide_rect(hero,cyborg):
            finish = True
            window.blit(lose,(200,200))
            kick.play()

        if sprite.collide_rect(hero,treasure):
            finish = True
            window.blit(win,(200,200))

        if sprite.collide_rect(hero,w1) or sprite.collide_rect(hero,w2) or sprite.collide_rect(hero,w3):
            finish = True
            window.blit(lose,(200,200))

    display.update()
    clock.tick(FPS)