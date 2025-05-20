import pygame
import sys
from home import Home
from Simulation import Simulation
from constantes import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simulation du Système Solaire")

    def run(self):
        while True:
            home = Home(self.screen)
            result = home.run()

            if result == "start":
                simulation = Simulation(self.screen)
                simulation.run()
            elif result == "exit":
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
