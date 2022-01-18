import pygame.sprite


class Butterfly(pygame.sprite.Sprite):
    def __init__(self, x, y, butter_body, butter_wings, direction, group):
        pygame.sprite.Sprite.__init__(self)
        self.butter_body = butter_body
        self.butter_wings = butter_wings
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.direction = direction
        self.add(group)

    def update(self, w1, h1, dx, dy, x0, y0) -> None:
        if self.rect.y + y0 - dy < 100 or self.rect.y + y0 - dy > h1 - self.rect.height - 100 or \
                self.rect.x + x0 - dx < 100 or self.rect.x + x0 + - dx > w1 - self.rect.width - 100:
            self.__direction = (self.__direction + 180) % 360
        self.rect.y += int(self.speed * sin(self.__direction*pi/180)) - dy
        self.rect.x += int(self.speed * cos(self.__direction*pi/180)) - dx