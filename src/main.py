import pygame
import sys
import random
from background import Background
from player import Player
from enemy import Enemy
from arrow import Arrow

#  НАСТРОЙКИ
SCREEN_W, SCREEN_H = 800, 600
FPS            = 60           # кадры в секунду
SPAWN_INTERVAL = 2_000        # мс между появлениями врагов
MAX_ENEMIES    = 5            # максимум одновременно
SPAWN_OFFSET   = 100          # насколько «за экраном» спавнить / удалять

#  ИНИЦИАЛИЗАЦИЯ PYGAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Аркадная игра")
clock = pygame.time.Clock()

#  ЗАГРУЗКА РЕСУРСОВ
raw_bg       = pygame.image.load("assets/images/fon.png").convert()
bg           = Background(raw_bg, zoom=0.8)

player_img   = "assets/images/valorant.png"
skeleton_img = "assets/images/skelet.png"
pumpkin_img  = "assets/images/tikva.png"

arrow_img    = pygame.image.load("assets/images/arrow.png").convert_alpha()
fire_sound   = pygame.mixer.Sound("assets/sounds/fire1.ogg")

#  ПАТЧИМ Enemy: движение без «рикошета»
def _move_straight(self):
    """Простое горизонтальное движение; без смены направления на границах."""
    self.rect.x += self.speed * self.dir
Enemy.update = _move_straight   # применяем ко всем врагам

#  СПРАЙТ-ГРУППЫ
player      = Player(player_img)
all_sprites = pygame.sprite.Group(player)
enemy_group = pygame.sprite.Group()
arrows      = pygame.sprite.Group()

# счётчик времени до следующего спавна
spawn_timer = 0

#  ГЛАВНЫЙ ЦИКЛ
running = True
while running:
    dt = clock.tick(FPS)
    spawn_timer += dt

    # — обработка событий —
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            arrow = Arrow(arrow_img, player.rect.centerx, player.rect.centery)
            arrows.add(arrow)
            all_sprites.add(arrow)
            fire_sound.play()

    # — спавн врагов —
    if spawn_timer >= SPAWN_INTERVAL and len(enemy_group) < MAX_ENEMIES:
        spawn_timer = 0

        side = random.choice(["left", "right"])
        if side == "left":
            x, direction = -SPAWN_OFFSET, 1     # летит вправо
        else:
            x, direction = SCREEN_W + SPAWN_OFFSET, -1  # летит влево

        y   = random.randint(50, SCREEN_H - 50)
        img = random.choice([skeleton_img, pumpkin_img])

        enemy      = Enemy(img, (x, y))
        enemy.dir  = direction
        enemy_group.add(enemy)
        all_sprites.add(enemy)

    # — обновление спрайтов —
    keys = pygame.key.get_pressed()
    player.update(keys, bg)

    arrows.update()

    for enemy in enemy_group.sprites():
        enemy.update()
        # удаляем, когда совсем ушёл за край
        if enemy.rect.right < -SPAWN_OFFSET or enemy.rect.left > SCREEN_W + SPAWN_OFFSET:
            enemy.kill()

    # — столкновения стрел с врагами —
    pygame.sprite.groupcollide(arrows, enemy_group, True, True)

    # — отрисовка —
    bg.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()