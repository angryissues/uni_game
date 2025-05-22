import pygame

class Background:
    def __init__(self, bg_image, zoom=1.0):
        if zoom != 1.0:
            w = int(bg_image.get_width() * zoom)
            h = int(bg_image.get_height() * zoom)
            self.image = pygame.transform.smoothscale(bg_image, (w, h))
        else:
            self.image = bg_image
        self.x = 0
        self.y = 0
        self.speed = 5

    def scroll(self, dx, dy=0):
        # Фон двигается только по горизонтали
        width = self.image.get_width()
        self.x = max(min(self.x + dx, 0), 800 - width)

    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))