import pygame
import sys
from math import sin
from math import cos
from math import pi


class Caterpillar():
    F0 = 0.5

    def __init__(self, n, r, x, y, direction, speed, image):
        self.n = n
        self.r = r
        self.image = image
        self.x = []
        self.y = []
        for i in range(self.n):
            self.x.append(r * i + x)
            self.y.append(0 + y)
        self.direction = direction
        self.speed = speed
        self.fi = [0] * self.n
        self.flag = 1

    def draw(self, surf):
        x2 = [0] * self.n
        y2 = [0] * self.n
        if self.flag == 1:  # up
            for i in range(1, self.n + 1):
                x2[i] = (self.x[i] - self.x[0]) * (cos(self.direction * pi / 180)) \
                     - (self.y[i] - self.y[0]) * (sin(self.direction * pi / 180))
                y2[i] = (self.x[i] - self.x[0]) * (sin(self.direction * pi / 180)) \
                     + (self.y[i] - self.y[0]) * (cos(self.direction * pi / 180))
        else:
            for i in range(0, self.n):
                x2[i] = (self.x[i] - self.x[self.n + 1]) * (cos(self.direction * pi / 180)) \
                     - (self.y[i] - self.y[self.n + 1]) * (sin(self.direction * pi / 180))
                y2[i] = (self.x[i] - self.x[self.n + 1]) * (sin(self.direction * pi / 180)) \
                     + (self.y[i] - self.y[self.n + 1]) * (cos(self.direction * pi / 180))

    for i in range(self.n):
        surf.blit(self.image, (x2[i], y2[i]))

    def update(self):
        if self.flag == 1 and self.fi[self.n // 2 - 1] > 90:
            self.flag = -1  # go down
        elif self.flag == -1 and self.fi[self.n // 2 - 1] <= 0:
            self.flag = 1  # go up
            for i in range(self.n // 2):
                self.fi[i] = 0
                print("1111")

        for i in range(self.n // 2):
            self.fi[i] = self.fi[self.n - 2 - i] = (self.fi[i] + self.flag * Caterpillar.F0 * (2 * i + 1)) % 180

        self.y[0] = self.y[self.n - 1]
        for i in range(1, self.n // 2):
            self.y[i] = self.y[self.n - i - 1] = self.y[i - 1] - self.r * sin(self.fi[i - 1] * pi / 180)
        self.y[self.n // 2] = self.y[self.n // 2 - 1] - self.r * sin(self.fi[self.n // 2 - 1] * pi / 180)
        if self.flag == 1:  # up!
            for i in range(1, self.n):
                self.x[i] = self.x[i - 1] + self.r * abs(cos(self.fi[i - 1] * pi / 180))

        else:  # down
            for i in range((self.n - 2), -1, -1):
                print("222")
                self.x[i] = self.x[i + 1] - self.r * abs(cos(self.fi[i] * pi / 180))


pygame.init()

# make a window
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Катерпиллар")
pygame.display.set_icon(pygame.image.load("ico.bmp"))
clock = pygame.time.Clock()
FPS = 60

bg_surf = pygame.image.load("wood.bmp")
cater_images = ["circle1.bmp", "circle2.bmp"]
cater_surf = [pygame.image.load(path) for path in cater_images]
for i in range(len(cater_surf)):
    cater_surf[i].set_colorkey((255, 255, 255))
    cater_surf[i] = pygame.transform.scale(cater_surf[i], (20, 20))
katia = [] * len(cater_surf)
for i in range(len(cater_surf)):
    katia.append(Caterpillar(5 + i * 4, 15 + i * 2, 200 + i * 10, 200 + i * 60, 80 + 10 * i, 0, cater_surf[i]))

while True:  # the main cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                for i in range(len(cater_surf)):
                    katia[i].update()
    sc.blit(bg_surf, (0, 0))
    for i in range(len(cater_surf)):
        katia[i].update()
        katia[i].draw(sc)

    pygame.display.flip()
    clock.tick(FPS)
