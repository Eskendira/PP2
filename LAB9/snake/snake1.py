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
        self.timer = random.randint(10, 20)  # Random timer between 3 to 10 seconds
        self.types = ["normal", "rare", "super"]
        self.spawn_weights = [0.7, 0.2, 0.1]  # Weights for each food type

    def generate_random_position(self):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if (x, y) not in [(segment.x, segment.y) for segment in snake.body]:
                return Point(x, y)

    def generate_random_type(self):
        return random.choices(self.types, weights=self.spawn_weights)[0]

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def update_timer(self):
        self.timer -= 1
        if self.timer <= 0:
            self.pos = self.generate_random_position()
            self.timer = random.randint(10, 20)  # Reset timer

FPS = 8
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

    food.update_timer()  # Update food timer

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
