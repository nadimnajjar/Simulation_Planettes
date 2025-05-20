import pygame
from Button import Button
from constantes import *

class Home:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = [
            Button("Start", screen, GREEN, 300, 500, 200, 100),
            Button("Exit", screen, RED, 300, 700, 200, 100)
        ]
        self.font = pygame.font.SysFont(None, 48)
        self.title = self.font.render("Simulation du système solaire", True, WHITE)
        try:
            self.image = pygame.image.load("planets1.jpg")
        except:
            self.image = pygame.Surface((500, 300))
            self.image.fill(BLUE)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.buttons[0].is_clicked(pos):
                        return "start"
                    elif self.buttons[1].is_clicked(pos):
                        return "exit"

            self.screen.fill(GRAY)
            self.screen.blit(self.image, (150, 100))
            self.screen.blit(self.title, (150, 50))
            for button in self.buttons:
                button.draw()

            pygame.display.flip()
            clock.tick(60)
