import pygame
from pygame.locals import *

class Mover:
    def __init__(self, location):
        self.location = pygame.math.Vector2(location)
        self.velocity = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.mass = 1
        self.radius = 10
        self.dampening = 0.98
        self.dragging = False
        self.drag_offset = pygame.Vector2(0, 0)

    def draw(self, win):
        pygame.draw.circle(win, pygame.Color("grey"), self.location, self.radius)
        if self.dragging:
            pygame.draw.circle(win, pygame.Color("dimgrey"), self.location, self.radius)

    def update(self):
        self.velocity += self.acceleration
        self.velocity *= self.dampening
        self.location += self.velocity
        self.acceleration *= 0

    def applyforce(self, force):
        f = force/self.mass
        self.acceleration += f

    def clicked(self, mpos):
        mpos = pygame.Vector2(mpos)
        d = mpos.distance_to(self.location)
        if d < self.radius:
            self.dragging = True
            self.drag_offset.x = self.location.x - mpos[0]
            self.drag_offset.y = self.location.y - mpos[1]
        self.velocity *= 0

    def drag(self, mpos):
        if self.dragging:
            self.location.x = mpos[0] + self.drag_offset.x
            self.location.y = mpos[1] + self.drag_offset.y
