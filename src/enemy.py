import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, pos):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 2
        self.dir = 1

    def update(self):
        self.rect.x += self.speed * self.dir
        if self.rect.left < 0 or self.rect.right > 800:
            self.dir *= -1