import pygame

pygame.init()

pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя первая программа на pygame")
pygame.display.set_icon(pygame.image.load(("ico.bmp")))
clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
