import pygame.sprite
from math import sin
from math import cos
from math import pi


class Cats(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.__direction = direction
        self.speed = speed
        self.add(group)

    def update(self, w1, h1, dx, dy, x0, y0) -> None:
        if self.rect.y + y0 - dy < 100 or self.rect.y + y0 - dy > h1 - self.rect.height - 100 or \
                self.rect.x + x0 - dx < 100 or self.rect.x + x0 + - dx > w1 - self.rect.width - 100:
            self.__direction = (self.__direction + 180) % 360
        self.rect.y += int(self.speed * sin(self.__direction*pi/180)) - dy
        self.rect.x += int(self.speed * cos(self.__direction*pi/180)) - dx

    def redirection(self, direction) -> None:
        self.__direction = direction
