import pygame
from engine.Engine import Engine
import json
from operator import itemgetter

file = open('config.json')
config = json.load(file)

WAIT_TIME, WIDTH, HEIGHT, PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT, WITH_MASK_COUNT, \
    IMMUNE_COUNT, PREGNANT_COUNT, DISEASE_SPREAD_RADIUS, INCUBATION_TIME, DISEASE_DURATION, HYGIENE_LEVEL, MAX_PERSON_SPEED = \
    itemgetter("WAIT_TIME", "WIDTH", "HEIGHT", "PEOPLE_COUNT", "DISEASED_COUNT", "INFECTED_COUNT", "MALE_COUNT",
               "VACCINATED_COUNT", "WITH_MASK_COUNT", "IMMUNE_COUNT", "PREGNANT_COUNT", "DISEASE_SPREAD_RADIUS",
               "INCUBATION_TIME", "DISEASE_DURATION", "HYGIENE_LEVEL", "MAX_PERSON_SPEED")(config)

STATS_WIDTH = 300


def paused():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH + STATS_WIDTH, HEIGHT))
    sim = Engine(screen, WIDTH, HEIGHT, PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT,
                 WITH_MASK_COUNT, IMMUNE_COUNT, PREGNANT_COUNT, DISEASE_SPREAD_RADIUS, MAX_PERSON_SPEED,
                 INCUBATION_TIME, DISEASE_DURATION, HYGIENE_LEVEL)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused()
        sim.update()
        sim.draw()

        pygame.display.flip()
        pygame.time.wait(WAIT_TIME)
    pygame.quit()


run()
file.close()
