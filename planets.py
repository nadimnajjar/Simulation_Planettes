import pygame
from math import *
class Planets:
    def __init__(self, screen, color, centre_x, centre_y, orbit_radius, planet_radius, theta=0):
        self.screen = screen
        self.color = color
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.orbit_radius = orbit_radius 
        self.planet_radius = planet_radius 
        self.theta = theta  

        #Positions initiales de mes planetes
        self.x = self.centre_x + self.orbit_radius * cos(self.theta)
        self.y = self.centre_y + self.orbit_radius * sin(self.theta)

    def draw(self):
        #Dessiner l'orbite
        pygame.draw.circle(self.screen, (50, 50, 50), (self.centre_x, self.centre_y), 
                          self.orbit_radius, 1)
        #Dessiner la planète
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.planet_radius)


    def move(self,speed):
        self.theta+=speed
        self.x=self.centre_x+self.orbit_radius*cos(self.theta)
        self.y=self.centre_y+self.orbit_radius*sin(self.theta)