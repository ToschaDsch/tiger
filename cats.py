import pygame.sprite
from math import sin
from math import cos
from math import pi


class Cats(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = speed
        self.add(group)

    def update(self, w1, h1, dx, dy, x0, y0) -> None:
        kx = sin(self.direction*pi)
        ky = cos(self.direction*pi)
        if self.rect.y + y0 - 100 > h1 or self.rect.y + y0 < 300 or self.rect.x + x0 > w1 or self.rect.x + x0 - 100 < 300:
            self.speed = - self.speed
        self.rect.y += self.speed * kx - dy
        self.rect.x += self.speed * ky - dx

    def update2(self, direction) -> None:
        self.direction = direction
