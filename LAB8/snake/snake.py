# import pygame
# import random
# import math
# import time
# import sys

# #const
# WIDTH = 640
# HEIGHT = 640
# PIXELS = 32
# SQUARES = int(WIDTH/PIXELS)

# #colors
# BG1 = (200, 200, 200)
# BG2 = (255, 255, 255)
# RED = (255, 0, 0)

# class Apple:
    
#     def __init__(self):
#         self.color = RED

#     def spawn(self):
#         self.posx = random.randrange

# class Background:

#     def draw(self,surface):
#         surface.fill(BG1)
#         counter = 0
#         for row in range (SQUARES):
#             for col in range (SQUARES):
#                 if counter % 2 == 0:
#                     pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS,PIXELS,PIXELS) )
#                 if col != SQUARES - 1:
#                     counter+=1

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
#     pygame.display.set_caption( "SNAKE" )

#     background = Background()

#     #Mainloop
#     while True:
#         background.draw(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#         pygame.display.update()

# main()


import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            return True
        return False

    def check_collision_with_border(self):
        head = self.body[0]
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        return False

class Food:
    def __init__(self):
        self.pos = self.generate_random_position()

    def generate_random_position(self):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if (x, y) not in [(segment.x, segment.y) for segment in snake.body]:
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = Food()

score = 0
level = 1

font = pygame.font.Font(None, 36)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()

    snake.move()
    if snake.check_collision(food):
        score += 1
        if score % 3 == 0:
            level += 1
            FPS += 1
        food.pos = food.generate_random_position()

    if snake.check_collision_with_border():
        print("Game Over! You hit the wall!")
        done = True

    snake.draw()
    food.draw()

    # Display score and level
    text = font.render(f"Score: {score} Level: {level}", True, colorBLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
