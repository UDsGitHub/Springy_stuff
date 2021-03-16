import pygame, sys
from pygame.locals import *
from Springs2 import *
from Particles import *

# setup
width = 720
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
run = True


def updatescr():
    screen.fill(pygame.Color("white"))

    # display and update springs
    for i in range(len(springs)):
        springs[i].update()
        springs[i].draw(screen)

    # display and update particles
    for i in range(len(particles)):
        for j in range(len(particles[0])):
            particles[i][j].applyforce(gravity)
            particles[i][j].update()
            particles[i][j].draw(screen)

    clock.tick(fps)
    pygame.display.update()

# scene physics stuff
gravity = pygame.Vector2(0, 0.1)
k = 0.4  # spring constant (stretchyness or stiffness)


# stuff
rows = 30
cols = 30
particles = [[[]for j in range(cols)]for i in range(rows)]
springs = []
spacing = 10

dragging = False

# create and append particles and springs to their respective lists
px = 100
for i in range(cols):
    py = 10
    for j in range(rows):
        p = Particle((px, py))
        particles[i][j] = p
        py += spacing
    px += spacing

# spring connections
for i in range(cols-1):
    for j in range(rows-1):
        a = particles[i][j]
        b1 = particles[i+1][j]
        b2 = particles[i][j+1]
        b3 = particles[i+1][j+1]
        s1 = Spring(k, spacing, a, b1)
        springs.append(s1)
        s2 = Spring(k, spacing, a, b2)
        springs.append(s2)
        # s3 = Spring(k, spacing, a, b3)
        # springs.append(s3)


# pin a point to its position
particles[0][0].locked = True  # topleft
particles[cols-1][0].locked = True  # topright
particles[0][rows//2 - 1].locked = True  # midleft
# particles[cols//2 - 1][0].locked = True  # midtop
particles[cols-1][rows//2].locked = True  # midright
particles[cols-1][rows - 2].locked = True  # bottomright
particles[0][rows - 1].locked = True  #bottomleft

wind = pygame.Vector2(3, 0)

while run:
    mouse_pos = pygame.mouse.get_pos()

    tail = particles[len(particles) - 1][len(particles) - 2]

    # follow mouse drag
    if dragging:
        tail.location = mouse_pos
        tail.velocity *= 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(cols):
                    for j in range(rows):
                        particles[i][j].applyforce(wind)
                # dragging = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

    updatescr()
