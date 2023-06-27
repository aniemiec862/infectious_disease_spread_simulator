import pygame
from engine.Engine import Engine
import json
from operator import itemgetter

file = open('config.json')
config = json.load(file)

WAIT_TIME, WIDTH, HEIGHT, PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT, \
WITH_MASK_COUNT, IMMUNE_COUNT, PREGNANT_COUNT, DISEASE_SPREAD_RADIUS, INCUBATION_TIME, DISEASE_DURATION, \
HYGIENE_LEVEL, MAX_PERSON_SPEED, DISPLAY_GRAPH = \
    itemgetter("WAIT_TIME", "WIDTH", "HEIGHT", "PEOPLE_COUNT", "DISEASED_COUNT", "INFECTED_COUNT", "MALE_COUNT",
               "VACCINATED_COUNT", "WITH_MASK_COUNT", "IMMUNE_COUNT", "PREGNANT_COUNT", "DISEASE_SPREAD_RADIUS",
               "INCUBATION_TIME", "DISEASE_DURATION", "HYGIENE_LEVEL", "MAX_PERSON_SPEED", "DISPLAY_GRAPH")(config)

STATS_WIDTH = 300
GRAPH_WIDTH = 300
DAYS_TO_PAUSE = 200


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
    if DISPLAY_GRAPH:
        screen_width = WIDTH + STATS_WIDTH + GRAPH_WIDTH
    else:
        screen_width = WIDTH + STATS_WIDTH

    screen = pygame.display.set_mode((screen_width, max(HEIGHT, 500)))
    pygame.display.set_caption('Infectious disease spread simulator')
    sim = Engine(screen, WIDTH, HEIGHT, PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT,
                 WITH_MASK_COUNT, IMMUNE_COUNT, PREGNANT_COUNT, DISEASE_SPREAD_RADIUS, MAX_PERSON_SPEED,
                 INCUBATION_TIME, DISEASE_DURATION, HYGIENE_LEVEL, DISPLAY_GRAPH)

    running = True
    days_passed = 0
    while running:
        days_passed += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused()
        if days_passed == DAYS_TO_PAUSE:
            paused()

        sim.update()
        sim.draw()
        pygame.display.flip()
        pygame.time.wait(WAIT_TIME)
    pygame.quit()


run()
file.close()
