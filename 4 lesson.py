import pygame

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя четвёртая программа на pygame")
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

t = 20
t2 = 5
C = 100
surf = pygame.Surface((W, C))
bita = pygame.Surface((t, 100))
prita = pygame.Surface((t, t2))

surf.fill(BLUE)
bita.fill(RED)
prita.fill(GREEN)

bx, by = 0, 0
x, y = 0, 0
x2, y2 = 0, 0
W0 = W
H0 = H
C0 = C
A = [[0, 0]]
while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if y2 < C0:
        y2 += 2
        C0 = C - t2
    else:
        y2 -= 2
        C0 = 0
    print(y2)
    bita.fill(RED)
    bita.blit(prita, (x2, y2))

    if bx < W0:
        bx += 5
        W0 = W - t
    else:
        bx -= 5
        W0 = 0
    surf.fill(BLUE)
    surf.blit(bita, (bx, by))

    if y < H0:
        y += 1
        H0 = H - 100
    else:
        y -= 1
        H0 = 0
    sc.fill(WHITE)
    sc.blit(surf, (x, y))

    A.append([x + bx + x2, y + by + y2])

    print(x + bx + x2, y + by + y2, A)
    pygame.draw.lines(sc, BLACK, False, A)

    pygame.display.flip()
    clock.tick(FPS)
