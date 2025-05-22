import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = 5

    def update(self, keys, bg):
        dx = dy = 0
        if keys[pygame.K_LEFT]:  dx = -self.speed
        if keys[pygame.K_RIGHT]: dx = self.speed
        if keys[pygame.K_UP]:    dy = -self.speed
        if keys[pygame.K_DOWN]:  dy = self.speed

        self.rect.move_ip(dx, dy)

        # При выходе за границы экрана — прокрутка фона
        if self.rect.left < 0:
            bg.scroll(self.speed, 0)
            self.rect.left = 0
        if self.rect.right > 800:
            bg.scroll(-self.speed, 0)
            self.rect.right = 800
        if self.rect.top < 0:
            bg.scroll(0, self.speed)
            self.rect.top = 0
        if self.rect.bottom > 600:
            bg.scroll(0, -self.speed)
            self.rect.bottom = 600