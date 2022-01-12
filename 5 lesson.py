import pygame

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя пятая программа на pygame")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()

# constant
H = 400
W = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60  # FPS
PI = 3.14
speed = 5

ground = H - 70
jump_forge = 20
move = jump_forge + 1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)
rect.bottom = ground

dx = 0

while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = - jump_forge
            elif event.key == pygame.K_LEFT:
                dx = - 2
            elif event.key == pygame.K_RIGHT:
                dx = 2

    if move <= jump_forge:
        if rect.bottom + move <= ground:
            rect.bottom += move
            if move < jump_forge:
                move += 1
                rect.centerx += dx
            else:
                rect.bottom = ground
                move = jump_forge + 1

    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.flip()

    clock.tick(FPS)
