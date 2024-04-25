import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
RMBpressed = False
THICKNESS = 5
current_color = colorRED
drawing_shape = ""

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_shapes():
    global LMBpressed, RMBpressed, drawing_shape, prevX, prevY, current_color, THICKNESS

    if LMBpressed or RMBpressed:
        screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print("RMB pressed!")
            RMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed or RMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if drawing_shape == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif drawing_shape == "circle":
                    radius = max(abs(currX - prevX), abs(currY - prevY))
                    pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)
                elif drawing_shape == "eraser":
                    if LMBpressed:
                        pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS+10)
                    elif RMBpressed:
                        pygame.draw.circle(base_layer, colorBLACK, (currX, currY), THICKNESS+10)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if drawing_shape == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif drawing_shape == "circle":
                radius = max(abs(currX - prevX), abs(currY - prevY))
                pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print("RMB released!")
            RMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if drawing_shape == "eraser":
                if LMBpressed:
                    pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS+10)
                elif RMBpressed:
                    pygame.draw.circle(base_layer, colorBLACK, (currX, currY), THICKNESS+10)
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_PLUS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_r:
                print("Drawing rectangles")
                drawing_shape = "rectangle"
            if event.key == pygame.K_c:
                print("Drawing circles")
                drawing_shape = "circle"
            if event.key == pygame.K_e:
                print("Using eraser")
                drawing_shape = "eraser"
            if event.key == pygame.K_1:
                print("Selected RED color")
                current_color = colorRED
            if event.key == pygame.K_2:
                print("Selected BLUE color")
                current_color = colorBLUE
            if event.key == pygame.K_3:
                print("Selected WHITE color")
                current_color = colorWHITE
            if event.key == pygame.K_4:
                print("Drawing square")
                drawing_shape = "square"
            if event.key == pygame.K_5:
                print("Drawing right triangle")
                drawing_shape = "right_triangle"
            if event.key == pygame.K_6:
                print("Drawing equilateral triangle")
                drawing_shape = "equilateral_triangle"
            if event.key == pygame.K_7:
                print("Drawing rhombus")
                drawing_shape = "rhombus"

    pygame.display.flip()
    clock.tick(60)

done = False

while not done:
    done = draw_shapes()

pygame.quit()