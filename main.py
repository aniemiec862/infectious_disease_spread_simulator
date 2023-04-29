import pygame
from engine.Engine import Engine

WAIT_TIME = 100
WIDTH, HEIGHT = 640, 480
STATS_WIDTH = 300
PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT, WITH_MASK_COUNT, IMMUNE_COUNT, PREGNANT_COUNT = \
    100, 10, 1, 10, 0, 0, 0, 3
DISEASE_SPREAD_RADIUS, INCUBATION_TIME, DISEASE_DURATION = 10, 100, 200
MAX_PERSON_SPEED = 20


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
    sim = Engine(WIDTH, STATS_WIDTH, HEIGHT, PEOPLE_COUNT, DISEASED_COUNT, INFECTED_COUNT, MALE_COUNT, VACCINATED_COUNT, WITH_MASK_COUNT, IMMUNE_COUNT, PREGNANT_COUNT, DISEASE_SPREAD_RADIUS, MAX_PERSON_SPEED, INCUBATION_TIME, DISEASE_DURATION)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused()
        sim.update()
        sim.draw(screen)

        pygame.display.flip()
        pygame.time.wait(WAIT_TIME)
    pygame.quit()


run()
