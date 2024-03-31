import pygame
import random

# Initialize
pygame.init()

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")

#music
brick_hit_sound = pygame.mixer.Sound("catch.mp3")
# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game variables
ball_speed = [5, 3]
paddle_speed = 0
ball_rect = pygame.Rect(400, 300, 40, 40)
paddle_rect = pygame.Rect(350, 580, 100, 10)
bricks = []
unbreakable_bricks = []
bonus_bricks = []
speed_increment = 0.1  # Amount to increase ball speed per frame
time_elapsed = 0  # Track time elapsed
clock = pygame.time.Clock()

for i in range(5):
    for j in range(3):
        brick = pygame.Rect(i * 150 + 50, j * 40 + 40, 110, 15)
        bricks.append(brick)
        if random.randint(1, 5) == 1:
            unbreakable_bricks.append(brick)
        elif random.randint(1, 5) == 1:
            bonus_bricks.append(brick)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_speed = -7
    elif keys[pygame.K_RIGHT]:
        paddle_speed = 7
    else:
        paddle_speed = 0

    paddle_rect.x += paddle_speed
    if paddle_rect.left < 0:
        paddle_rect.left = 0
    elif paddle_rect.right > SCREEN_WIDTH:
        paddle_rect.right = SCREEN_WIDTH

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0:
        ball_speed[1] = -ball_speed[1]
    if ball_rect.colliderect(paddle_rect):
        ball_speed[1] = -ball_speed[1]

    for brick in bricks[:]:
        if ball_rect.colliderect(brick):
            if brick in unbreakable_bricks:
                ball_speed[1] = -ball_speed[1]
            else:
                bricks.remove(brick)
                ball_speed[1] = -ball_speed[1]
                brick_hit_sound.play()
    time_elapsed += clock.tick() / 1000  # Time since the last frame in seconds
    if time_elapsed >= 1:  # Increase speed every second
        ball_speed[0] *= (1 + speed_increment)
        ball_speed[1] *= (1 + speed_increment)
        time_elapsed = 0
    for brick in bonus_bricks[:]:
        if ball_rect.colliderect(brick):
            bonus_bricks.remove(brick)
            
            brick_hit_sound.play()


    pygame.draw.rect(screen, BLUE, paddle_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()

