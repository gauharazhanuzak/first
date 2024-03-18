import pygame
import sys
pygame.init()

W, H = 600, 450
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Moving Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25
x = (W - radius) // 2
y = (H - radius) // 2
dx = 0
dy = 0
speed = 20


running = True
while running:
    screen.fill(WHITE)
    
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -speed
            elif event.key == pygame.K_DOWN:
                dy = speed
            elif event.key == pygame.K_LEFT:
                dx = -speed
            elif event.key == pygame.K_RIGHT:
                dx = speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
    

    x += dx
    y += dy
    
    x = max(radius, min(x, W - radius))
    y = max(radius, min(y, H - radius))
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(20)

pygame.quit()
sys.exit()