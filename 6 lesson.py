import pygame

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Моя шэшая программа на pygame")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()

# constant
H = 400
W = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (239, 228, 176)
RED = (255, 0, 0)
FPS = 60  # FPS
PI = 3.14
speed = 5

f = pygame.font.SysFont("Century Gothic", 20)
sc_text = f.render("  Hallo Welt  ", 1, RED, YELLOW)

pos = sc_text.get_rect(center=(W//2, H//2))

def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text, pos)
    pygame.display.update()

draw_text()

while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.mouse.get_rel()

    if pygame.mouse.get_focused() and pos.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            rel = pygame.mouse.get_rel()
            pos.move_ip(rel)
            draw_text()

    clock.tick(FPS)
