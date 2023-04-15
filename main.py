import pygame
from engine.Engine import Engine

WAIT_TIME = 100
WIDTH, HEIGHT = 640, 480
NO_PEOPLE, NO_DISEASED_PEOPLE = 20, 1

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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    sim = Engine(WIDTH, HEIGHT, NO_PEOPLE, NO_DISEASED_PEOPLE)

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
