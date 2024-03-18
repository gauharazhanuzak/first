import pygame
import os

pygame.init()

W, H = 600, 450
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)

font = pygame.font.SysFont('Times New Roman', 24)

dir = "Новая папка"

files = [file for file in os.listdir(dir) if file.endswith(".mp3")]

t = 0
playing = False

pygame.mixer.music.load(os.path.join(dir, files[t]))

running = True
while running:
    screen.fill(WHITE)
    
    for l in pygame.event.get():
        if l.type == pygame.QUIT:
            running = False
        elif l.type == pygame.KEYDOWN:
            if l.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif l.key == pygame.K_RIGHT:
                t = (t + 1) % len(files)
                pygame.mixer.music.load(os.path.join(dir, files[t]))
                pygame.mixer.music.play()
                playing = True
            elif l.key == pygame.K_LEFT:
                t = (t - 1) % len(files)
                pygame.mixer.music.load(os.path.join(dir, files[t]))
                pygame.mixer.music.play()
                playing = True
                
    text = font.render(files[t], True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
