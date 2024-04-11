# Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
car_width = 44
car_height = 96
boun_left = 0
boun_right = SCREEN_WIDTH - car_width
boun_top = 0
boun_bottom = SCREEN_HEIGHT - car_height
N =2

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play()
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("RACER")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("player1.png"), (44, 96))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 500)

    def move(self):
        klav = pygame.key.get_pressed()
        if klav[K_UP] and self.rect.top > boun_top:
            self.rect.move_ip(0, -5)
        if klav[K_DOWN] and self.rect.bottom < boun_bottom:
            self.rect.move_ip(0, 5)
        if klav[K_LEFT] and self.rect.left > boun_left:
            self.rect.move_ip(-5, 0)
        if klav[K_RIGHT] and self.rect.right < boun_right:
            self.rect.move_ip(5, 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20))
        self.weight = random.randint(1, 3) 

    def move(self):
        x = random.randint(20, SCREEN_WIDTH - 20)
        y = random.randint(20, SCREEN_HEIGHT - 20)
        self.rect.center = (x, y)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C = Coins()

# Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (350, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    for entity in coins:
        screen.blit(entity.image, entity.rect)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('crash.wav')
        pygame.mixer.music.play()
        time.sleep(1.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        res_scores = font.render("Score: " + str(SCORE), True, BLACK)
        screen.blit(res_scores, (20, 200))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(3)

        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('coinss.wav').play()
        SCORE += 1
        C.move()

        if SCORE >= N:
            SPEED += 1
            N += 10

    pygame.display.update()
    FramePerSec.tick(FPS)
