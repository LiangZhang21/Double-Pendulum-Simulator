import pygame
from constants import *
from equations import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Double Pendulum Simulator')

pygame.init()
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #caculation referenced from Auctux

    angle_a1 = angle1_a(gravity, mass1, mass2, angle1, angle2, length1, length2, angle_v1, angle_v2)
    angle_a2 = angle2_a(gravity, mass1, mass2, angle1, angle2, length1, length2, angle_v1, angle_v2) 
   
    # set up
    x1 = float(X + length1 * math.sin(angle1))
    y1 = float(Y + length1 * math.cos(angle1))

    x2 = float(x1 + length2 * math.sin(angle2))
    y2 = float(y1 + length2 * math.cos(angle2))

    track.append([x2, y2])

    
    angle_v1 += angle_a1
    angle_v2 += angle_a2
    angle1 += angle_v1
    angle2 += angle_v2
   

    # draw
    WIN.fill(BLACK)
    run2 = True
    i = 0
    while i < len(track) - 1:
        #pygame.draw.circle(WIN, WHITE, (pos[0], pos[1]), 1)
        i += 1
        pygame.draw.line(WIN, WHITE, (track[i-1][0], track[i-1][1]), (track[i][0], track[i][1]), 1)
        #pygame.draw.circle(WIN, WHITE, (track[i][0], track[i][1]), 1)

    pygame.draw.line(WIN, WHITE, (X, Y), (x1, y1))
    pygame.draw.circle(WIN, WHITE, (x1, y1), 10)
    pygame.draw.line(WIN, WHITE, (x1, y1), (x2, y2))
    pygame.draw.circle(WIN, WHITE, (x2, y2), 10)
    

    pygame.display.update()

pygame.quit()
