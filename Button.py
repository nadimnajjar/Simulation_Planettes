import pygame
import sys
from constantes import *


class Button:
    def __init__(self, text, screen, color, left, top, width, height, text_color=WHITE):
        self.text = text
        self.screen = screen
        self.color = color
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.text_color = text_color
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        
        Button.font = pygame.font.SysFont(None, 48)
    
    def draw(self):

        pygame.draw.rect(self.screen, self.color, self.rect)
        
        text_surface = Button.font.render(self.text, True, self.text_color)
        
        text_x = self.left + (self.width - text_surface.get_width()) // 2
        text_y = self.top + (self.height - text_surface.get_height()) // 2
        
        self.screen.blit(text_surface, (text_x, text_y))

    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)