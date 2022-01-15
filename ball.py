import pygame.sprite


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, H, sx, dx, dy) -> None:
        if self.rect.y < H - 20:
            self.rect.y += self.speed - dy
            self.rect.x += -dx + sx
        else:
            self.kill()

    def draw2(self, surf1):
        surf1.blit(self.image, (self.rect.x, self.rect.y))
