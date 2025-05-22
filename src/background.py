import pygame

class Background:
    def __init__(self, bg_image):
        self.image = bg_image
        self.x = 0
        self.y = 0
        self.speed = 5

    def scroll(self, dx, dy):
        width = self.image.get_width()
        height = self.image.get_height()
        self.x = max(min(self.x + dx, 0), 800 - width)
        self.y = max(min(self.y + dy, 0), 600 - height)

    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))