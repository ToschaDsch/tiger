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
        self.dx1 = 0
        self.dx2 = 0
        self.dy1 = 0
        self.dy2 = 0

    def draw(self, surf):
        C = 15
        if C == 15:
            x2 = [0] * (self.n)
            y2 = [0] * (self.n)
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
                    print(self.x[i], x2[i], self.y[i], y2[i])
                self.dx1 = x2[-1] - x2[0] - self.x[-1] + self.x[0]
                self.dy1 = y2[-1] - y2[0]
            else:
                if self.dx1 != 0 and self.dy1 != 0:
                    for i in range(self.n):
                        self.x[i] += self.dx1
                        self.y[i] += self.dy1
                    self.dy1 = 0
                    self.dx1 = 0

                x2[self.n-1] = self.x[self.n-1]
                y2[self.n-1] = self.y[self.n-1]

                for i in range(0, self.n - 1):
                    x2[i] = x2[-1] + (self.x[i] - self.x[-1]) * (cos(self.direction * pi / 180)) \
                         - (self.y[i] - self.y[-1]) * (sin(self.direction * pi / 180))
                    y2[i] = y2[-1] + (self.x[i] - self.x[-1]) * (sin(self.direction * pi / 180)) \
                         + (self.y[i] - self.y[-1]) * (cos(self.direction * pi / 180))

                self.dx2 = x2[-1] - x2[0] - self.x[-1] + self.x[0]
                self.dy2 = y2[-1] - y2[0]

            for i in range(self.n):
                surf.blit(self.image, (x2[i], y2[i]))
        else:
            for i in range(self.n):
                surf.blit(self.image, (self.x[i], self.y[i]))

    def update(self, w1, h1, dx, dy, x0, y0):
        if self.y[0] + y0 < 0 or self.y[0] + y0 > h1 - 100 or \
                self.x[0] + x0 < 0 or self.x[0] + x0 + 0 > w1 - 100:
            self.direction = (self.direction + 180) % 360
        self.rect.y += int(self.speed * sin(self.__direction*pi/180)) - dy
        self.rect.x += int(self.speed * cos(self.__direction*pi/180)) - dx

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

