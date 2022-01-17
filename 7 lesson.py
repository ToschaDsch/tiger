import pygame
from random import randint
from random import random
from ball import Ball
from cats import Cats
from caterpillar import Caterpillar
import sys

pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Тайгер в лесу")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 50)  # there is a event for the snow

# constants
H = 400  # height for the window
W = 600  # bright

# tehre are colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (239, 228, 176)
RED = (255, 0, 0)

FPS = 60  # FPS

speed = 5  # speed for the hero

# there is a cross with light
cross_surf = pygame.image.load("cross.bmp")
cross_rect = cross_surf.get_rect(center=(150, 350))  # take center
cross_surf.set_colorkey((181, 230, 29))  # clean away background

# there is a light for th cross
light_surf = pygame.image.load("light2.bmp")
light_surf.set_alpha(150)       # set transparent
light_rect = light_surf.get_rect()      # make a rect

# there is the background
bg_surf = pygame.image.load("wood.bmp")
W2 = bg_surf.get_width()    # height for the background
H2 = bg_surf.get_height()   # bright

# there is the hero
car_surf = pygame.image.load("tiger.bmp")
car_surf.set_colorkey((255, 255, 255))  # clean away background
car_surf = pygame.transform.scale(car_surf, (car_surf.get_width() // 2, car_surf.get_height() // 2))  # minimize
car_rect = car_surf.get_rect(center=(W // 2, H // 2))   # make a rect

# there are a lot of caterpillars
cater_images = ["circle1.bmp", "circle2.bmp"]
cater_surf = [pygame.image.load(path) for path in cater_images]
for i in range(len(cater_surf)):
    cater_surf[i].set_colorkey((255, 255, 255))
    cater_surf[i] = pygame.transform.scale(cater_surf[i], (20, 20))

nim = [3, 5, 7, 9, 11]

caters = pygame.sprite.Group()


def create_caters(group):
    index = randint(0, len(cater_images) - 1)
    index2 = randint(0, 4)
    x = randint(200, W2 - 200)
    y = randint(200, H2 - 200)
    direct = randint(0, 360)
    n = nim[index2]
    r = randint(10, 20)
    return Caterpillar(n, r, x, y, direct, 5, cater_surf[index], caters)
                # (self, n, r, x9, y9, direction, speed, image, group):


cats_images = ["cat1.bmp", "cat2.bmp", "cat3.bmp", "cat4.bmp", "cat5.bmp", "cat6.bmp"]
cats_surf = [pygame.image.load(path) for path in cats_images]
for i in range(len(cats_surf)):
    cats_surf[i].set_colorkey((181, 230, 29))
    cats_surf[i] = pygame.transform.scale(cats_surf[i], (100, 100))

balls_images = ["snow1.bmp", "snow2.bmp", "snow3.bmp", "snow4.bmp"]
balls_surf = [pygame.image.load(path) for path in balls_images]
for i in range(len(balls_surf)):
    balls_surf[i].set_colorkey((0, 0, 0))
    balls_surf[i] = pygame.transform.scale(balls_surf[i], (50, 50))


def create_ball(group):         # make a snowflake
    index = randint(0, len(balls_surf) - 1)
    x = randint(0, W2)
    speed2 = randint(1, 4)

    return Ball(x, speed2, balls_surf[index], group)


cats = pygame.sprite.Group()
ii = 0
cats_a = [Cats] * len(cats_surf)
for surf_i in cats_surf:
    x = randint(200, W2 - 200)
    y = randint(150, H2 - 150)
    dir = randint(0, 360)
    speed_c = randint(1, 5)
    cats_a[ii] = Cats(x, y, dir, speed_c, surf_i, cats)
    ii += 1

car_up = pygame.transform.rotate(car_surf, -90)
car_down = pygame.transform.rotate(car_surf, 90)
car_left = pygame.transform.flip(car_surf, False, False)
car_right = pygame.transform.flip(car_surf, True, False)

bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width() // 1, bg_surf.get_height() // 1))

car = car_left

balls = pygame.sprite.Group()

flag = 0
x2 = 0
y2 = 0
dx = 0
dy = 0
x0 = 0
y0 = 0
sx = 0

flag_wait = 5
while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.USEREVENT:
            if flag == 1:
                create_ball(balls)

            nom = randint(0, len(cats_surf) - 1)
            dir_n = randint(0, 360)
            cats_a[nom].update2(dir_n)      # change direction the cats

            if flag_wait == 0:      # make a caterpillar
                flag_wait = 6       # it is the time!
                create_caters(caters)
            flag_wait -= 1           # wait please

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                flag = 1 if flag == 0 else 0
            elif event.key == pygame.K_a and flag == 1:
                sx -= 1
            elif event.key == pygame.K_d and flag == 1:
                sx += 1

    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        if car_rect.x > 3 / 8 * W - car_rect.width:
            car_rect.x -= speed
        elif car_rect.x + x2 + car_rect.width > 230:
            x2 -= speed
        else:
            car_rect.x = 3 / 8 * W - car_rect.width
    elif bt[pygame.K_RIGHT]:
        car = car_right
        if car_rect.x < 5 / 8 * W:
            car_rect.x += speed
        elif car_rect.x + x2 < W2 - car_rect.width - 120:
            x2 += speed
        else:
            car_rect.x = 5 / 8 * W
    elif bt[pygame.K_UP]:
        car = car_up
        if car_rect.y > 3 / 8 * H - car_rect.height:
            car_rect.y -= speed
        elif car_rect.y + y2 + car_rect.height > 150:
            y2 -= speed
        else:
            car_rect.y = 3 / 8 * H - car_rect.height
    elif bt[pygame.K_DOWN]:
        car = car_down
        if car_rect.y < 5 / 8 * H:
            car_rect.y += speed
        elif car_rect.y + y2 < H2 - 160:
            y2 += speed
        else:
            car_rect.y = 5 / 8 * H
    dx = x2 - x0
    dy = y2 - y0
    x0 = x2
    y0 = y2
    sc.blit(bg_surf, (-x2, -y2))
    cross_rect.x -= dx
    cross_rect.y -= dy
    sc.blit(cross_surf, (cross_rect.x, cross_rect.y))

    caters.update(W2, H2, dx, dy, x2, y2, sc)
    # caters.draw(sc)

    balls.draw(sc)
    cats.draw(sc)
    if pygame.Rect.colliderect(car_rect, cross_rect):
        sc.blit(light_surf, (-230, -100 - y2))

    for i in caters:
        if pygame.Rect.colliderect(car_rect, i):
            print(i.rect.x, i.rect.y)
            i.kill()
    sc.blit(car, car_rect)

    balls.update(H2, sx, dx, dy)
    cats.update(W2, H2, dx, dy, x2, y2)
    pygame.display.flip()
    clock.tick(FPS)
