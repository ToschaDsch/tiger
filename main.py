import pygame
from random import randint
from random import random
from ball import Ball
from cats import Cats
from caterpillar import Caterpillar
from hero import Hero
from butterfly import Butterfly
import sys

pygame.init()
pygame.font.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Тайгер в лесу")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 50)  # there is an event for the snow

# constants
H = 400  # height for the window
W = 600  # bright

# there are colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (239, 228, 176)
RED = (255, 0, 0)

FPS = 60  # FPS

speed = 5  # speed for the hero

# all things for score
score = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)
flag_score = 0

# there is a cross with light
cross_surf = pygame.image.load("cross.bmp")
cross_rect = cross_surf.get_rect(center=(150, 350))  # take center
cross_surf.set_colorkey((181, 230, 29))  # clean away background

# there is a light for th cross
light_surf = pygame.image.load("light2.bmp")
light_surf.set_alpha(150)  # set transparent
light_rect = light_surf.get_rect()  # make a rect

# there is the background
bg_surf = pygame.image.load("wood.bmp")
W2 = bg_surf.get_width()  # height for the background
H2 = bg_surf.get_height()  # bright

# there is the hero
car_surf = pygame.image.load("tiger.bmp")
car_surf.set_colorkey((255, 255, 255))  # clean away background
car_surf = pygame.transform.scale(car_surf, (car_surf.get_width() // 2, car_surf.get_height() // 2))  # minimize
car_rect = car_surf.get_rect(center=(W // 2, H // 2))  # make a rect
tiger = Hero(W // 2, H // 2, 5, car_surf, W, H, W2, H2)  # make a tiger

# there are a lot of caterpillars
cater_images = ["circle1.bmp", "circle2.bmp", "circle3.bmp", "circle4.bmp", "circle5.bmp", "circle6.bmp"]
cater_surf = [pygame.image.load(path) for path in cater_images]
for i in range(len(cater_surf)):
    cater_surf[i].set_colorkey((255, 255, 255))  # clean away background

nim = [3, 5, 7, 9, 11]  # how much balls can a caterpillar contain

caters = pygame.sprite.Group()  # male a group for caterpillars (I need it for sprites)


def create_caters(group):  # the function make a caterpillar
    index = randint(0, len(cater_images) - 1)  # choose an image
    index2 = randint(0, 4)  # choose how much ball a caterpillar contains
    n = nim[index2]
    xc = randint(200, W2 - 200)  # coords for ball N0
    yc = randint(200, H2 - 200)
    direction1 = randint(0, 360)
    radius = randint(10, 30)  # radius of balls
    return Caterpillar(n, radius, xc, yc, direction1,  # number of balls in a caterpillar, radius, coords + direction
                       5, pygame.transform.scale(cater_surf[index],  # speed (I don't need it), minimization of images
                                                 (1 * radius, 1 * radius)), group)  # group


# there are butterflies
butt_body_images = ["butt1.bmp", "butt2.bmp"]
butt_wings_images = ["butt1_wings.bmp", "butt1_wings.bmp"]
butter_body_surf = [pygame.image.load(path) for path in butt_body_images]
butter_wings_surf = [pygame.image.load(path) for path in butt_wings_images]
for i in range(len(butter_body_surf)):
    butter_body_surf[i].set_colorkey((181, 230, 29))  # clean away background
    butter_wings_surf[i].set_colorkey((181, 230, 29))  # clean away background


def create_butterfly(xb, yb, group):  # the function make a butterfly
    index = randint(0, len(butter_body_surf) - 1)  # choose an image
    direction_b = randint(0, 360)
    return Butterfly(xb, yb, butter_body_surf[index], butter_wings_surf[index],  # coords + images (bodies + wings)
                     direction_b, group)  # direction, group


butterflies = pygame.sprite.Group()  # a group for the butterflies (sprite)

# make cats
cats_images = ["cat1.bmp", "cat2.bmp", "cat3.bmp", "cat4.bmp", "cat5.bmp", "cat6.bmp"]
cats_surf = [pygame.image.load(path) for path in cats_images]
for i in range(len(cats_surf)):
    cats_surf[i].set_colorkey((181, 230, 29))  # clean away background
    cats_surf[i] = pygame.transform.scale(cats_surf[i], (100, 100))  # minimize it

# make snowflakes
balls_images = ["snow1.bmp", "snow2.bmp", "snow3.bmp", "snow4.bmp"]
balls_surf = [pygame.image.load(path) for path in balls_images]
for i in range(len(balls_surf)):
    balls_surf[i].set_colorkey((0, 0, 0))  # clean away background
    balls_surf[i] = pygame.transform.scale(balls_surf[i], (50, 50))  # minimize it


def create_ball(group):  # make a snowflake
    index = randint(0, len(balls_surf) - 1)  # choose an image
    x = randint(0, W2)  # make the x coord
    speed2 = randint(1, 4)  # choose speed
    return Ball(x, speed2, balls_surf[index], group)


balls = pygame.sprite.Group()  # a group for the snowflakes (sprite)

# make a lot of cats
cats = pygame.sprite.Group()  # there is a group for cats (sprite)
ii = 0
cats_a = [Cats] * len(cats_surf)  # list of cats
for surf_i in cats_surf:
    x = randint(200, W2 - 200)  # make coords
    y = randint(150, H2 - 150)
    direction = randint(0, 360)  # direction at the beginning
    speed_c = randint(1, 5)  # speed at the beginning
    cats_a[ii] = Cats(x, y, direction, speed_c, surf_i, cats)
    ii += 1

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
            cats_a[nom].redirection(dir_n)  # change direction from a cat

            if flag_wait == 0:  # make a caterpillar
                flag_wait = 6  # it is the time!
                create_caters(caters)
            flag_wait -= 1  # wait please

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # let it snow
                flag = 1 if flag == 0 else 0
            elif event.key == pygame.K_a and flag == 1:
                sx -= 1  # snow flies left
            elif event.key == pygame.K_d and flag == 1:
                sx += 1  # snow flies right

    bt = pygame.key.get_pressed()
    x2, y2 = tiger.update1(bt, x2, y2)

    dx = x2 - x0
    dy = y2 - y0
    x0 = x2
    y0 = y2
    sc.blit(bg_surf, (-x2, -y2))  # show the background
    cross_rect.x -= dx
    cross_rect.y -= dy
    sc.blit(cross_surf, (cross_rect.x, cross_rect.y))  # show the cross

    caters.update(W2, H2, dx, dy, x2, y2, sc)  # upgrade caterpillars

    balls.draw(sc)  # show snowflakes
    cats.draw(sc)  # show cats

    if pygame.Rect.colliderect(tiger.rect, cross_rect):  # the hero stands on the cross
        sc.blit(light_surf, (-230 - dx - x2, -100 - y2))  # light on!

    for i in caters:  # collide with a caterpillar
        score, flag_score = i.collide(tiger.rect, score, flag_score)

    if flag_score < 0:  # show the score above
        my_font = pygame.font.SysFont('Comic Sans MS', 30)  # normal case
        text_surface = my_font.render(str(score), True, (55, 51, 14))  # black
        text_rect = text_surface.get_rect(center=(W // 2, 15))
    else:
        my_font = pygame.font.SysFont('Comic Sans MS', 40)  # the hero has eaten a caterpillar
        text_surface = my_font.render(str(score), False, (234, 46, 36))  # red
        text_rect = text_surface.get_rect(center=(W // 2, 15))
        flag_score -= 1

    tiger.draw2(sc)
    balls.update(H2, sx, dx, dy)  # update snow
    cats.update(W2, H2, dx, dy, x2, y2)  # update cats
    sc.blit(text_surface, text_rect)  # draw the score
    pygame.display.flip()  # draw all the things
    clock.tick(FPS)  # neu iteration
