import pygame
import sys
from planets import *
from constantes import *

pygame.init()
sun_x=SCREEN_WIDTH//2
sun_y=SCREEN_WIDTH//2

clock = pygame.time.Clock()

screen=pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

planets = [
    # Mercure
    Planets(screen, ORANGE, sun_x, sun_y, 100, 10),
    # Venus
    Planets(screen, YELLOW, sun_x, sun_y, 150, 15, theta=2),
    # Terre
    Planets(screen, BLUE, sun_x, sun_y, 200, 18, theta=4),
    # Mars
    Planets(screen, RED, sun_x, sun_y, 250, 14, theta=1),
    # Jupitere
    Planets(screen, ORANGE, sun_x, sun_y, 320, 30, theta=3)
]

speeds = [0.03, 0.02, 0.015, 0.01, 0.005]

    
if __name__=="__main__":
    running=True
    while running:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        for i,planet in enumerate(planets):
            planet.draw()
            planet.move(speeds[i])
        
        pygame.draw.circle(screen, WHITE, (sun_x, sun_y), 40)
        pygame.display.flip()
        clock.tick(60)