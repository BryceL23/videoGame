# Constructed with the help of Mr. Cozorts's model code, my classmates assistance and feedback as well as the class resources listed in canvas


# Create a game that provides goals, rules, feedback and freedom

# make player start at base of screen and make the game stop when player hits top of screen
# make mobs move across the screen contiually
# don't allow player to leave the screen

# the goal of the game is to reach the top of the screen as fast as possible without touching the mobs moving across the screen, and when the player reaches the top of the screen the game will stop indicating the player has won

# import libraries and modules
# from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

# game settings 
WIDTH = 1000
HEIGHT = 800
FPS = 45


# the starting time


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sets the perameters for the the size and shape of the player and mob objects
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

def colorbyte():
    return random.randint(0,255)

# sprites...
# provides the perameters of the player, such as size, position, color and shape
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    # defines how the player of the game will be able to move around during the game
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.acc.y = -5
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_s]:
            self.acc.y = 5
        if keys[pg.K_d]:
            self.acc.x = 5
        # updates the rate at which the player moves and the imputs of the player
    def update(self):
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.vel += self.acc
        self.pos += self.vel + -0.1 * self.acc
      # sets the postition of the player and determines the velocity of the player
        self.rect.midbottom = self.pos
        if self.rect.x < 0 or self.rect.x > WIDTH - self.rect.width:
            self.vel*= -0.9
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.vel*= -0.9
# creates the player class providing it with the color and dimentions 
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # defines the mob class providing it with the coordinates, size, random color 
    class Mob(Sprite):
        def __init__(self, x, y, w, h, color):
            Sprite.__init__(self)
            self.image = pg.Surface((w,h))
            self.color = color
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = 5*random.choice([-1,1])
            self.speedy = 5*random.choice([-1,1])
            self.inbounds = True
    # defines the mob class with the specific size and speed at which they move across the screen 
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((45, 45))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 1
        self.speedy = 1
    def update(self):
        self.rect.x += 1
    
# defines the specific movement of the mob and directs them to continuesly move across the screen even when the mobs leave; they return coming from the same direction they started
    def warp(self):
        if self.rect.x > WIDTH:
            self.rect.x = 0
            print(self.rect.x)
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = HEIGHT

# defines the boundaries within which the player can move 
    def boundscheck(self):
        if not self.rect.x > 0 or not self.rect.x < WIDTH:
            self.speedx *=-1
        if not self.rect.y > 0 or not self.rect.y < HEIGHT:
            self.speedy *= -1

 # if mob collides with player it will tell us if it has collided
# makes the mob move from the top left to the bottom right and a constant pace
    def update(self):
        hits = pg.sprite.spritecollide(self,all_sprites, False) 
        if hits == True:
            player.pos.x = WIDTH/2
            player.pos.y = HEIGHT + 30
        self.rect.x += self.speedx
        self.rect.y += self.speedy

# init pygame and create a window
# allows you to write game and instantiate the different features of the game
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create groups
# creates the different sprites that are used throughout the game 
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
mbs = []
player = Player()

# run the game smoothly as long as all the correct perameters and met in order to continue 
running = True

for i in range(30):
    m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    mobs.add(m)
    mbs.append(m)

# add player to all sprites group
all_sprites.add(player)


# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    


    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        # could allow for player to make different provided movements
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    # using built in pygame collision detection, when player collides with mobs group, it goes back to the bottom of the screen 
    mobhits = pg.sprite.spritecollide(player, mobs, False)
    if mobhits:
        player.pos.y = HEIGHT 
        player.pos.x = WIDTH/2
        # running = False
        
    
# determining where the player begins the game which is at the bottom
    if player.pos.y-30 > 0:
        mobs.update()
        all_sprites.update()
    for m in mbs:
        m.warp()
    
   

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw text
   
    # draw all sprites
    all_sprites.draw(screen)
    mobs.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
