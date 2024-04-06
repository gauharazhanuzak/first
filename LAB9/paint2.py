import sys
import pygame
from pygame import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_rectangle = False
    start_rect_pos = None
    shape_to_draw = 'circle'

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    shape_to_draw = 'circle'
                elif event.key == pygame.K_e:
                    shape_to_draw = 'rectangle'
                elif event.key == pygame.K_s:
                    shape_to_draw = 'square'  # Draw square
                elif event.key == pygame.K_t:
                    shape_to_draw = 'right_triangle'  # Draw right triangle
                elif event.key == pygame.K_q:
                    shape_to_draw = 'equilateral_triangle'  # Draw equilateral triangle
                elif event.key == pygame.K_h:
                    shape_to_draw = 'rhombus'  # Draw rhombus

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)
                elif event.button == 2:  # middle click starts drawing rectangle
                    start_rect_pos = event.pos
                    drawing_rectangle = True

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:  # middle click ends drawing rectangle
                    if drawing_rectangle:
                        end_rect_pos = event.pos
                        if shape_to_draw == 'rectangle':
                            pygame.draw.rect(screen, (255, 255, 255), (start_rect_pos[0], start_rect_pos[1],
                                                                      end_rect_pos[0] - start_rect_pos[0],
                                                                      end_rect_pos[1] - start_rect_pos[1]))
                        elif shape_to_draw == 'circle':
                            pygame.draw.circle(screen, (255, 255, 255),
                                               ((start_rect_pos[0] + end_rect_pos[0]) // 2,
                                                (start_rect_pos[1] + end_rect_pos[1]) // 2),
                                               max(abs(end_rect_pos[0] - start_rect_pos[0]),
                                                   abs(end_rect_pos[1] - start_rect_pos[1])) // 2)
                        elif shape_to_draw == 'square':
                            side_length = max(abs(end_rect_pos[0] - start_rect_pos[0]),
                                              abs(end_rect_pos[1] - start_rect_pos[1]))
                            pygame.draw.rect(screen, (255, 255, 255), (start_rect_pos[0], start_rect_pos[1],
                                                                      side_length, side_length))
                        elif shape_to_draw == 'right_triangle':
                            pygame.draw.polygon(screen, (255, 255, 255),
                                                [(start_rect_pos[0], start_rect_pos[1]),
                                                 (end_rect_pos[0], start_rect_pos[1]),
                                                 (start_rect_pos[0], end_rect_pos[1])])
                        elif shape_to_draw == 'equilateral_triangle':
                            side_length = max(abs(end_rect_pos[0] - start_rect_pos[0]),
                                              abs(end_rect_pos[1] - start_rect_pos[1]))
                            height = int(side_length * (3 ** 0.5) / 2)
                            pygame.draw.polygon(screen, (255, 255, 255),
                                                [(start_rect_pos[0], end_rect_pos[1]),
                                                 ((start_rect_pos[0] + end_rect_pos[0]) // 2, start_rect_pos[1]),
                                                 (end_rect_pos[0], end_rect_pos[1])])
                        elif shape_to_draw == 'rhombus':
                            pygame.draw.polygon(screen, (255, 255, 255),
                                                [(start_rect_pos[0], (start_rect_pos[1] + end_rect_pos[1]) // 2),
                                                 ((start_rect_pos[0] + end_rect_pos[0]) // 2, start_rect_pos[1]),
                                                 (end_rect_pos[0], (start_rect_pos[1] + end_rect_pos[1]) // 2),
                                                 ((start_rect_pos[0] + end_rect_pos[0]) // 2, end_rect_pos[1])])
                        drawing_rectangle = False

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
