import pygame,sys
import datetime
pygame.init()

display = pygame.display.set_mode((640,640))
pygame.display.set_caption('Clock')
disc= pygame.image.load('main-clock.png').convert_alpha()
disc= pygame.transform.scale(disc,(350,350))
disc_rect = disc.get_rect(center=(320,320))

s_hand=pygame.image.load('left-hand.png').convert_alpha()
s_rect=s_hand.get_rect(center=(320,320))
IMAGE_SMALL = pygame.transform.scale(s_hand, (300, 150))
s_handc=IMAGE_SMALL.copy()

m_hand = pygame.image.load('right-hand.png')
m_rect = m_hand.get_rect(center=(320,320))
IMAGE_SMALL2 = pygame.transform.scale(m_hand, (300, 150))
m_handc= IMAGE_SMALL2.copy()
fps = pygame.time.Clock()
def rotate(image,angle):
    new_image = pygame.transform.rotozoom(image,-angle,1)
    return new_image

while True:
    time = datetime.datetime.now()
    s_angle=int(time.strftime('%S'))*6
    m_angle=int(time.strftime('%M'))*6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.blit(disc,disc_rect)

    m_handc=rotate(IMAGE_SMALL2,m_angle)
    m_rect=m_handc.get_rect(center=(320,320))
    display.blit(m_handc,m_rect)

    s_handc = rotate(IMAGE_SMALL,s_angle)
    s_rect=s_handc.get_rect(center=(320,320))
    display.blit(s_handc,s_rect)

    pygame.display.update()
    fps.tick(60)