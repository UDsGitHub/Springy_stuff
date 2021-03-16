import pygame, random
from pygame.locals import *


class Particle:
    def __init__(self, location):
        self.locked = False
        self.location = pygame.Vector2(location)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.radius = 2
        self.mass = 1

    def draw(self, win):
        pygame.draw.circle(win, pygame.Color("limegreen"), self.location, self.radius)

    def update(self):
        if not self.locked:
            self.velocity *= 0.99
            self.velocity += self.acceleration
            self.location += self.velocity
            self.acceleration *= 0

    def applyforce(self, force):
        f = force/self.mass
        self.acceleration += f
