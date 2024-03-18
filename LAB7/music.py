import pygame
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions (not really needed for this example)
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

# Set up colors
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up music directory
music_dir = "Новая папка"

# List music files
music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]

# Initialize variables
current_track = 0
playing = False

# Load and play first track
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()
                playing = True
                
    # Display current track
    track_text = font.render(music_files[current_track], True, (0, 0, 0))
    screen.blit(track_text, (10, 10))
    
    # Display player status
    status_text = font.render("Playing" if playing else "Paused", True, (0, 0, 0))
    screen.blit(status_text, (10, 50))
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
