import pygame, sys
from pygame.locals import *
from Springs import *
from Mover import *

# setup
width = 720
height = 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
run = True

def updatescr():
    screen.fill(pygame.Color("white"))
    spring.line(screen, bob.location)
    spring.draw(screen)
    bob.update()
    bob.drag(mouse_pos)
    bob.draw(screen)
    clock.tick(fps)
    pygame.display.update()


gravity = pygame.Vector2(0, 2)

spring = Spring(width//2, 0, 200)
bob = Mover((width//2, 240))


while run:
    mouse_pos = pygame.mouse.get_pos()

    spring.connect(bob)

    bob.applyforce(gravity)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                bob.clicked(mouse_pos)
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                # stop dragging
                bob.dragging = False

    updatescr()
