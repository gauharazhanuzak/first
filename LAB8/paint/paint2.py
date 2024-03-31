import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
#Initialization: Pygame is initialized, and a display window of size 800x600 pixels is created

#Clock: A clock object is created to control the frame rate of the application
clock = pygame.time.Clock()

#Color Constants: RGB color constants are defined for convenience
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (70, 70))

#Drawing Tools: The drawing tools include rectangles, circles, right triangles, equal triangles, and a rhombus. The draw_rect function draws rectangles of different colors at the top of the screen to select colors
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

#Pick Color Function: This function determines the color selected based on the position of the mouse click. It returns the corresponding color
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<=x<=40 and 0<=y<=40:
            return RED
        elif 40<x<=80 and 0<=y<=40:
            return GREEN
        elif 80<x<=120 and 0<=y<=40:
            return BLUE
        elif 1010<=x<=1080 and 0<=y<=40:
            return BLACK
    return color

#Painting Function: This function handles drawing based on the selected drawing mode (mode). It draws shapes or erases based on the mode
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and not (0<=x<=400 and 0<=y<=90):
        if mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), 27)
        if mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        if mode == 'right_triangle':
            pygame.draw.polygon(screen, color, ((x, y), (x, y+40), (x+40, y+40)), 3)
        if mode == 'equal_triangle':
            pygame.draw.polygon(screen, color, ((x,y), (x+20, y-40), (x+40, y)))
        if mode == 'rhomb':
            pygame.draw.polygon(screen, color, ((x, y), (x+20, y-20), (x+40, y), (x+20, y+20)))
        if mode == 'eraser':
            pygame.draw.circle(screen, BLACK, (x, y), 27)

mode = 'circle'

#Main Loop: This loop listens for events, updates the screen, and handles user input. It also updates the drawing mode based on the selected tool
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    for i in range(len(colors)):
        draw_rect(i)

    screen.blit(eraser, (1010, 0))
    rect = pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 3)
    circle = pygame.draw.circle(screen, WHITE, (197, 20), 23, 3)
    right = pygame.draw.polygon(screen, WHITE, ((230, 0), (230, 40), (270, 40)), 3)
    equal = pygame.draw.polygon(screen, WHITE, ((280, 40), (300, 0), (320, 40)), 3)
    rhomb = pygame.draw.polygon(screen, WHITE, ((330, 20), (350,0), (370, 20), (350, 40)), 3)
    eraser_button = pygame.Rect(1010, 0, 70, 70)

    pos = pygame.mouse.get_pos()
    if rect.collidepoint(pos):
        mode = "rect"
    if circle.collidepoint(pos):
        mode = "circle"
    if right.collidepoint(pos):
        mode = 'right_triangle'
    if equal.collidepoint(pos):
        mode = 'equal_triangle'
    if rhomb.collidepoint(pos):
        mode = 'rhomb'
    if eraser_button.collidepoint(pos):
        mode = 'eraser'


    color = pick_color()
    painting(color)


    clock.tick(370)
    pygame.display.update()
