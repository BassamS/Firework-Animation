import pygame
import time
pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks!")

FPS = 60

COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 255, 255),
    (230, 230, 250),
    (255, 192, 203)
]


class Projectile:
    pass


class Firework:
    pass


class luncher:
    WIDTH = 20
    HEIGHT = 20
    COLOR = 'grey'

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency
        self.start_time = time.time()
        self.fireworks = []

    def draw(self, win):
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))


def draw():
    win.fill("black")

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
