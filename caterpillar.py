from math import sin
from math import cos
from math import pi

import pygame.sprite


class Caterpillar(pygame.sprite.Sprite):
    F0 = 0.5

    def __init__(self, n, r, x9, y9, direction, speed, image, group):
        pygame.sprite.Sprite.__init__(self)
        self.n = n
        self.r = r
        self.image = image
        self.x = []
        self.y = []
        for i in range(self.n):
            self.x.append(r * i + x9)
            self.y.append(0 + y9)
        self.direction = direction
        self.speed = speed
        self.fi = [0] * self.n
        self.flag = 1
        self.dx1 = 0
        self.dx2 = 0
        self.dy1 = 0
        self.dy2 = 0
        self.add(group)
        self.rect = self.image.get_rect(center=(self.x[0], self.y[0]))
        for i in range(1, self.n):
            self.rect.union_ip(self.image.get_rect(center=(self.x[i], self.y[i])))

    def turn_it(self):
        x2 = [0] * self.n
        y2 = [0] * self.n
        if self.flag == 1:  # up
            if self.dx2 != 0 and self.dy2 != 0:
                for i in range(self.n):
                    self.x[i] -= self.dx2
                    self.y[i] -= self.dy2
                self.dy2 = 0
                self.dx2 = 0

            x2[0] = self.x[0]
            y2[0] = self.y[0]
            for i in range(1, self.n):
                x2[i] = x2[0] + (self.x[i] - self.x[0]) * (cos(self.direction * pi / 180)) \
                        - (self.y[i] - self.y[0]) * (sin(self.direction * pi / 180))
                y2[i] = y2[0] + (self.x[i] - self.x[0]) * (sin(self.direction * pi / 180)) \
                        + (self.y[i] - self.y[0]) * (cos(self.direction * pi / 180))

            self.dx1 = x2[-1] - x2[0] - self.x[-1] + self.x[0]
            self.dy1 = y2[-1] - y2[0]
        else:
            if self.dx1 != 0 and self.dy1 != 0:
                for i in range(self.n):
                    self.x[i] += self.dx1
                    self.y[i] += self.dy1
                self.dy1 = 0
                self.dx1 = 0

            x2[self.n - 1] = self.x[self.n - 1]
            y2[self.n - 1] = self.y[self.n - 1]

            for i in range(0, self.n - 1):
                x2[i] = x2[-1] + (self.x[i] - self.x[-1]) * (cos(self.direction * pi / 180)) \
                        - (self.y[i] - self.y[-1]) * (sin(self.direction * pi / 180))
                y2[i] = y2[-1] + (self.x[i] - self.x[-1]) * (sin(self.direction * pi / 180)) \
                        + (self.y[i] - self.y[-1]) * (cos(self.direction * pi / 180))

            self.dx2 = x2[-1] - x2[0] - self.x[-1] + self.x[0]
            self.dy2 = y2[-1] - y2[0]

        self.rect = self.image.get_rect(center=(x2[0], y2[0]))
        for i in range(1, self.n):
            self.rect.union_ip(self.image.get_rect(center=(x2[i], y2[i])))

        return x2, y2

    def draw1(self, surf):
        x, y = self.turn_it()
        for i in range(self.n):
            surf.blit(self.image, (x[i], y[i]))

    def redirection(self, grad):
        self.direction = (self.direction + grad) % 360
        if self.flag == 1:
            x0 = self.dx1 + self.x[-1] - self.x[0]
            y0 = self.dy1
        else:
            x0 = - self.dx2 - self.x[-1] + self.x[0]
            y0 = -self.dy2

        for i in range(self.n):
            self.x[i] += x0
            self.y[i] += y0

    def update(self, w1, h1, dx1, dy1, x01, y01, surf):
        if self.y[-1] + y01 - dy1 < 50 or self.y[-1] + y01 - dy1 > h1 - 50 or \
                self.x[1] + x01 - dx1 < 50 or self.x[-1] + x01 - dx1 > w1 - 50:
            self.kill()
        else:
            for i in range(self.n):
                self.x[i] -= dx1
                self.y[i] -= dy1

            if self.flag == 1 and self.fi[self.n // 2 - 1] > 90:
                self.flag = -1  # go down
            elif self.flag == -1 and self.fi[self.n // 2 - 1] <= 1:
                self.flag = 1  # go up
                for i in range(self.n // 2):
                    self.fi[i] = 0

            for i in range(self.n // 2):
                self.fi[i] = self.fi[self.n - 2 - i] = (self.fi[i] + self.flag * Caterpillar.F0 * (i + 1)) % 180

            self.y[0] = self.y[self.n - 1]
            for i in range(1, self.n // 2):
                self.y[i] = self.y[self.n - i - 1] = self.y[i - 1] - self.r * sin(self.fi[i - 1] * pi / 180)
            self.y[self.n // 2] = self.y[self.n // 2 - 1] - self.r * sin(self.fi[self.n // 2 - 1] * pi / 180)

            if self.flag == 1:  # up!
                for i in range(1, self.n):
                    self.x[i] = self.x[i - 1] + self.r * abs(cos(self.fi[i - 1] * pi / 180))
            else:  # down
                for i in range((self.n - 2), -1, -1):
                    self.x[i] = self.x[i + 1] - self.r * abs(cos(self.fi[i] * pi / 180))

            x, y = self.turn_it()
            self.draw1(surf)

    def collide(self, car_rect, score, flag_score):
        if pygame.Rect.colliderect(car_rect, self.rect):
            score += self.r
            self.kill()
            flag_score = 5

        return self.rect.x, self.rect.y, score, flag_score
