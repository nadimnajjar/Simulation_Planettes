import pygame
from planets import Planets
from constantes import *

class Simulation:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.sun_x = SCREEN_WIDTH // 2
        self.sun_y = SCREEN_HEIGHT // 2

        self.planets = [
            Planets(screen, ORANGE, self.sun_x, self.sun_y, 100, 10),
            Planets(screen, YELLOW, self.sun_x, self.sun_y, 150, 15, theta=2),
            Planets(screen, BLUE, self.sun_x, self.sun_y, 200, 18, theta=4),
            Planets(screen, RED, self.sun_x, self.sun_y, 250, 14, theta=1),
            Planets(screen, ORANGE, self.sun_x, self.sun_y, 320, 30, theta=3)
        ]

        self.speeds = [0.03, 0.02, 0.015, 0.01, 0.005]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill(BLACK)
            for i, planet in enumerate(self.planets):
                planet.draw()
                planet.move(self.speeds[i])

            pygame.draw.circle(self.screen, WHITE, (self.sun_x, self.sun_y), 40)
            pygame.display.flip()
            self.clock.tick(60)
