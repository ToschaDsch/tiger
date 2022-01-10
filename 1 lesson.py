import pygame

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя первая программа на pygame")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()

# constant
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60  # FPS
PI = 3.14

pygame.draw.rect(sc, BLUE, (10, 10, 50, 100), 2)

pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 5)
pygame.draw.aaline(sc, GREEN, (200, 40), (350, 70), 5)

pygame.draw.lines(sc, RED, False, [(200, 180), (250, 180), (300, 200)])
pygame.draw.aalines(sc, RED, True, [(250, 80), (200, 80), (350, 200)], 1)
                            #  closed

pygame.draw.polygon(sc, WHITE, [(400, 280), (350, 280), (400, 300)])
pygame.draw.polygon(sc, RED, [(350, 80), (100, 180), (450, 100), (50, 60)], 5)

pygame.draw.circle(sc, BLUE, (300, 250), 40)
pygame.draw.ellipse(sc, RED, (300, 300, 100, 50), 1)

pygame.draw.arc(sc, RED, (450, 30, 50, 150), PI, 2+PI, 5)

pygame.display.flip()

while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
