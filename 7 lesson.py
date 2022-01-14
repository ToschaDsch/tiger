import pygame
from random import randint
from ball import Ball

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Тайгер в лесу")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100)

# constants
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
cross_surf = pygame.image.load("cross.bmp").set_colorkey((255, 255, 255))
cross_rect = cross_surf.get_rect(center=(200, 400))
bg_surf = pygame.image.load("wood.bmp")
car_surf = pygame.image.load("tiger.bmp")
car_surf.set_colorkey((255, 255, 255))
car_surf = pygame.transform.scale(car_surf, (car_surf.get_width() // 2, car_surf.get_height() // 2))
car_rect = car_surf.get_rect(center=(W // 2, H // 2))

balls_images = ["snow1.bmp", "snow2.bmp", "snow3.bmp", "snow4.bmp"]
balls_surf = [pygame.image.load(path) for path in balls_images]
for i in range(len(balls_surf)):
    balls_surf[i].set_colorkey((0, 0, 0))
    balls_surf[i] = pygame.transform.scale(balls_surf[i], (50, 50))


def create_ball(group):
    index = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed2 = randint(1, 4)

    return Ball(x, speed2, balls_surf[index], group)


car_up = pygame.transform.rotate(car_surf, -90)
car_down = pygame.transform.rotate(car_surf, 90)
car_left = pygame.transform.flip(car_surf, 0, 0)
car_right = pygame.transform.flip(car_surf, 1, 0)

bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width() // 1, bg_surf.get_height() // 1))

car = car_left

balls = pygame.sprite.Group()

flag = 0

while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.USEREVENT and flag == 1:
            create_ball(balls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag = 1 if flag == 0 else 0

    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > W - car_rect.height:
            car_rect.x = W - car_rect.height
    elif bt[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > H - car_rect.width/2:
            car_rect.y = H - car_rect.width/2
    sc.blit(bg_surf, (0, 0))
    sc.blit(cross_surf, cross_rect)
    sc.blit(car, car_rect)
    balls.draw(sc)
    balls.update(H)
    pygame.display.update()
    clock.tick(FPS)
