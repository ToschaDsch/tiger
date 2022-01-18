import pygame.sprite
from math import sin
from math import cos
from math import pi


class Butterfly(pygame.sprite.Sprite):
    def __init__(self, x, y, butter_body, butter_wings, direction, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(butter_body, (50, 100))
        self.butter_wings = butter_wings
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.direction = direction
        self.add(group)
        self.speed = 5

    def update(self, w1, h1, dx, dy, x0, y0) -> None:
        if self.rect.y + y0 - dy < 0 or self.rect.y + y0 - dy > h1 - self.rect.height or \
                self.rect.x + x0 - dx < 0 or self.rect.x + x0 + - dx > w1 - self.rect.width - 0:
            self.kill()
        else:
            self.rect.y += int(self.speed * sin(self.direction*pi/180)) - dy
            self.rect.x += int(self.speed * cos(self.direction*pi/180)) - dx