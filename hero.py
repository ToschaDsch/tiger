import pygame.sprite


class Hero:
    def __init__(self, x, y, speed, surf, W, H, W2, H2):
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.W = W
        self.H = H
        self.W2 = W2
        self.H2 = H2

        self.hero_up = pygame.transform.rotate(surf, -90)
        self.hero_down = pygame.transform.rotate(surf, 90)
        self.hero_left = pygame.transform.flip(surf, False, False)
        self.hero_right = pygame.transform.flip(surf, True, False)
        self.hero_surf = self.hero_left

    def update1(self, bt, x2, y2) -> None:
        if bt[pygame.K_LEFT]:
            self.hero_surf = self.hero_left
            if self.rect.x > 3 / 8 * self.W - self.rect.width:
                self.rect.x -= self.speed
            elif self.rect.x + x2 + self.rect.width > 230:
                x2 -= self.speed
            else:
                self.rect.x = 3 / 8 * self.W - self.rect.width
        elif bt[pygame.K_RIGHT]:
            self.hero_surf = self.hero_right
            if self.rect.x < 5 / 8 * self.W:
                self.rect.x += self.speed
            elif self.rect.x + x2 < self.W2 - self.rect.width - 120:
                x2 += self.speed
            else:
                self.rect.x = 5 / 8 * self.W
        elif bt[pygame.K_UP]:
            self.hero_surf = self.hero_up
            if self.rect.y > 3 / 8 * self.H - self.rect.height:
                self.rect.y -= self.speed
            elif self.rect.y + y2 + self.rect.height > 150:
                y2 -= self.speed
            else:
                self.rect.y = 3 / 8 * self.H - self.rect.height
        elif bt[pygame.K_DOWN]:
            self.hero_surf = self.hero_down
            if self.rect.y < 5 / 8 * self.H:
                self.rect.y += self.speed
            elif self.rect.y + y2 < self.H2 - 160:
                y2 += self.speed
            else:
                self.rect.y = 5 / 8 * self.H
        return x2, y2

    def draw2(self, surf1):
        surf1.blit(self.hero_surf, (self.rect.x, self.rect.y))