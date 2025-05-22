import pygame
import sys
from background import Background
from player import Player
from enemy import Enemy
from arrow import Arrow

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Аркадная игра — ПЗ №3")
clock = pygame.time.Clock()

# Загрузка ресурсов
bg_img = pygame.image.load("assets/images/fon.png").convert()
player_img = "assets/images/valorant.png"
skeleton_img = "assets/images/skelet.png"
pumpkin_img = "assets/images/tikva.png"
arrow_img = pygame.image.load("assets/images/arrow.png").convert_alpha()
fire_sound = pygame.mixer.Sound("assets/sounds/fire1.ogg")

# Создание объектов
bg = Background(bg_img)
player = Player(player_img)
enemy1 = Enemy(skeleton_img, (200, 150))
enemy2 = Enemy(pumpkin_img, (600, 450))
all_sprites = pygame.sprite.Group(player, enemy1, enemy2)
arrows = pygame.sprite.Group()

# Главный цикл
running = True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            arrow = Arrow(arrow_img, player.rect.centerx, player.rect.centery)
            all_sprites.add(arrow)
            arrows.add(arrow)
            fire_sound.play()

    keys = pygame.key.get_pressed()
    player.update(keys, bg)
    enemy1.update()
    enemy2.update()
    arrows.update()

    # Проверка коллизий
    pygame.sprite.groupcollide(arrows, pygame.sprite.Group(enemy1, enemy2), True, True)

    # Отрисовка
    bg.draw(screen)
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
    pygame.display.flip()

pygame.quit()
sys.exit()