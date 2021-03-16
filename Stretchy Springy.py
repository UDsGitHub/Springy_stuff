import pygame, sys
from pygame.locals import *
from Springs2 import *
from Mover import *
from Particles import *

# setup
width = 720
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
run = True

def updatescr():
    screen.fill(pygame.Color("white"))

    # display and update springs
    for s in springs:
        s.update()
        s.draw(screen)

    # display and update particles
    for p in particles:
        p.applyforce(gravity)
        p.update()
        p.draw(screen)

    clock.tick(fps)
    pygame.display.update()


gravity = pygame.Vector2(0, 0.1)
k = 0.1

particles = []
springs = []
spacing = 20

dragging = False

for i in range(20):
    particles.append(Particle((200, i * spacing)))
    if i != 0:
        a = particles[i]
        b = particles[i - 1]
        spring = Spring(k, spacing, a, b)
        springs.append(spring)

particles[0].locked = True

while run:
    mouse_pos = pygame.mouse.get_pos()

    tail = particles[len(particles) - 1]

    if dragging:
        tail.location = mouse_pos
        tail.velocity *= 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

    updatescr()
