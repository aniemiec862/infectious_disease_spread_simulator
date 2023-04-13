import pygame
from engine.simulation import Simulation

WAIT_TIME = 100

pygame.init()

width, height = 640, 480
no_people, no_infected_people = 19, 1

screen = pygame.display.set_mode((width, height))

sim = Simulation(width, height, no_people, no_infected_people)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sim.update()
    sim.draw(screen)

    pygame.display.flip()
    pygame.time.wait(WAIT_TIME)

pygame.quit()
