import pygame
import pygame.surface
import random

Harry = pygame.image.load("HarryPotter.png")
Title = pygame.image.load("Title.png")
StartMenu = pygame.image.load("Start Menu.png")
Rule = pygame.image.load("Rule.png")
GoBack = pygame.image.load("GoBack.png")
Controls = pygame.image.load("Controls.png")
ClicktoBegin = pygame.image.load("Clicktobegin.png")
Gameover = pygame.image.load("GameOver.png")
Boss = pygame.image.load("boss.png")
bossbar_full = pygame.image.load("boss_bar_full.png")
bossbar_dead = pygame.image.load("boss_bar_dead.png")
bossbar_1 = pygame.image.load("boss_bar1.png")
bossbar_2 = pygame.image.load("boss_bar2.png")
bossbar_3 = pygame.image.load("boss_bar3.png")
bossbar_4 = pygame.image.load("boss_bar4.png")
bossbar_5 = pygame.image.load("boss_bar5.png")
bossbar_6 = pygame.image.load("boss_bar6.png")
bossbar_7 = pygame.image.load("boss_bar7.png")
bossbar_8 = pygame.image.load("boss_bar8.png")
bossbar_9 = pygame.image.load("boss_bar9.png")
Win = pygame.image.load("win.png")
shooting_event = pygame.USEREVENT + 1
enemy_moving_event = pygame.USEREVENT + 2
screen_flip_event = pygame.USEREVENT + 3
spritegroup = pygame.sprite.Group()
color = (70, 250, 70)
enemy_move = 2000
shoot = 1000
screen_reload = 2000
key_up_delay = 1000
transparent = (0, 0, 0, 0)
screen = pygame.display.set_mode((1600, 1000))
screenWidth = 1600
ScreenHeight = 1000
screen.fill((255, 255, 255))
screen.blit(Harry, (150, 300))
screen.blit(Title, (500, 50))
screen.blit(StartMenu, (800, 400))
pygame.display.flip()


class Magic(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Magic.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        pygame.sprite.Sprite.__init__(self, spritegroup)

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def kill(self):
        self.image.fill(transparent)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Enemy1.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        pygame.sprite.Sprite.__init__(self, spritegroup)

    def render(self):
        screen.blit(self.image, (self.x, self.y))


def main():
    pygame.init()
    logo = pygame.image.load("HarryPotter.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Wizard Game")
    enemy1_alive = True
    enemy2_alive = True
    enemy3_alive = True
    enemy4_alive = True
    enemy5_alive = True
    space_key_pressed = False
    win = False
    boss_damage = 0
    not_run = True
    not_game_over = True
    reloaded = True
    play = False
    running = True
    ready = False
    boss_damage_cool_down = True
    score = 0
    y_value = 450
    boss_x = 1200
    boss = False
    my_font = pygame.font.SysFont("Times New Roman", 50)
    magic = Magic(500, y_value)
    movable_tiles = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850,
                     900]
    random_tiles = random.choice(movable_tiles)
    enemy1 = Enemy(1400, random_tiles)
    movable_tiles.remove(random_tiles)
    enemy1_y_value = random_tiles
    random_tiles = random.choice(movable_tiles)
    enemy2 = Enemy(1400, random_tiles)
    movable_tiles.remove(random_tiles)
    enemy2_y_value = random_tiles
    random_tiles = random.choice(movable_tiles)
    enemy3 = Enemy(1400, random_tiles)
    movable_tiles.remove(random_tiles)
    enemy3_y_value = random_tiles
    random_tiles = random.choice(movable_tiles)
    enemy4 = Enemy(1400, random_tiles)
    movable_tiles.remove(random_tiles)
    enemy4_y_value = random_tiles
    random_tiles = random.choice(movable_tiles)
    enemy5 = Enemy(1400, random_tiles)
    movable_tiles.remove(random_tiles)
    enemy5_y_value = random_tiles
    harry_shoot = pygame.transform.scale(Harry, (50, 70))
    Boss_bar_full = pygame.transform.scale(bossbar_full, (900, 100))
    Boss_bar_dead = pygame.transform.scale(bossbar_dead, (900, 100))
    Boss_bar_1 = pygame.transform.scale(bossbar_1, (900, 100))
    Boss_bar_2 = pygame.transform.scale(bossbar_2, (900, 100))
    Boss_bar_3 = pygame.transform.scale(bossbar_3, (900, 100))
    Boss_bar_4 = pygame.transform.scale(bossbar_4, (900, 100))
    Boss_bar_5 = pygame.transform.scale(bossbar_5, (900, 100))
    Boss_bar_6 = pygame.transform.scale(bossbar_6, (900, 100))
    Boss_bar_7 = pygame.transform.scale(bossbar_7, (900, 100))
    Boss_bar_8 = pygame.transform.scale(bossbar_8, (900, 100))
    Boss_bar_9 = pygame.transform.scale(bossbar_9, (900, 100))
    pygame.time.set_timer(enemy_moving_event, enemy_move)
    pygame.time.set_timer(screen_flip_event, screen_reload)
    score_display = my_font.render(str(score), True, color)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == shooting_event:
                reloaded = True
                boss_damage_cool_down = True
                pygame.time.set_timer(shooting_event, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if reloaded:
                        space_key_pressed = True
                        pygame.time.set_timer(shooting_event, shoot)
                        screen.blit(magic.image, (150, y_value))
                        if y_value == enemy1_y_value and enemy1_alive:
                            enemy1.kill()
                            enemy1_alive = False
                            score += 1
                            score_display = my_font.render(str(score), True, color)
                        if y_value == enemy2_y_value and enemy2_alive:
                            enemy2.kill()
                            enemy2_alive = False
                            score += 1
                            score_display = my_font.render(str(score), True, color)
                        if y_value == enemy3_y_value and enemy3_alive:
                            enemy3.kill()
                            enemy3_alive = False
                            score += 1
                            score_display = my_font.render(str(score), True, color)
                        if y_value == enemy4_y_value and enemy4_alive:
                            enemy4.kill()
                            enemy4_alive = False
                            score += 1
                            score_display = my_font.render(str(score), True, color)
                        if y_value == enemy5_y_value and enemy5_alive:
                            enemy5.kill()
                            enemy5_alive = False
                            score += 1
                            score_display = my_font.render(str(score), True, color)
                        if boss and boss_damage_cool_down:
                            if y_value == 250 or y_value == 300 or y_value == 350 or y_value == 400 or y_value == 450:
                                boss_damage_cool_down = False
                                boss_damage += 1
                        pygame.display.flip()
                        reloaded = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    space_key_pressed = False
            if event.type == enemy_moving_event:
                if not boss and ready:
                    enemy1.x -= 150
                    enemy2.x -= 150
                    enemy3.x -= 150
                    enemy4.x -= 150
                    enemy5.x -= 150
                if boss:
                    boss_x -= 100

            if event.type == screen_flip_event and play and not_game_over:
                if space_key_pressed:
                    screen.blit(magic.image, (150, y_value))
                if not boss:
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(enemy1.image, (enemy1.x, enemy1.y))
                    screen.blit(enemy2.image, (enemy2.x, enemy2.y))
                    screen.blit(enemy3.image, (enemy3.x, enemy3.y))
                    screen.blit(enemy4.image, (enemy4.x, enemy4.y))
                    screen.blit(enemy5.image, (enemy5.x, enemy5.y))
                    screen.blit(score_display, (1500, 30))
                if boss:
                    screen.fill((52, 61, 82))
                    screen.blit(Boss, (boss_x, 200))
                    screen.blit(harry_shoot, (50, y_value))
                    if boss_damage == 0:
                        screen.blit(Boss_bar_full, (350, 30))
                    if boss_damage == 1:
                        screen.blit(Boss_bar_1, (350, 30))
                    if boss_damage == 2:
                        screen.blit(Boss_bar_2, (350, 30))
                    if boss_damage == 3:
                        screen.blit(Boss_bar_3, (350, 30))
                    if boss_damage == 4:
                        screen.blit(Boss_bar_4, (350, 30))
                    if boss_damage == 5:
                        screen.blit(Boss_bar_5, (350, 30))
                    if boss_damage == 6:
                        screen.blit(Boss_bar_6, (350, 30))
                    if boss_damage == 7:
                        screen.blit(Boss_bar_7, (350, 30))
                    if boss_damage == 8:
                        screen.blit(Boss_bar_8, (350, 30))
                    if boss_damage == 9:
                        screen.blit(Boss_bar_9, (350, 30))
                    if boss_damage == 10:
                        screen.blit(Boss_bar_dead, (350, 30))
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if reloaded:
                        pygame.time.set_timer(shooting_event, shoot)
                        screen.blit(magic.image, (150, y_value))
                        reloaded = False
                if event.key == pygame.K_w and ready and not_game_over and not boss:
                    y_value -= 50
                    if y_value <= 50:
                        y_value = 50
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(enemy1.image, (enemy1.x, enemy1.y))
                    screen.blit(enemy2.image, (enemy2.x, enemy2.y))
                    screen.blit(enemy3.image, (enemy3.x, enemy3.y))
                    screen.blit(enemy4.image, (enemy4.x, enemy4.y))
                    screen.blit(enemy5.image, (enemy5.x, enemy5.y))
                    screen.blit(score_display, (1500, 30))
                    pygame.display.flip()
                    pygame.time.delay(100)
                if event.key == pygame.K_s and ready and not_game_over and not boss:
                    y_value += 50
                    if y_value >= 900:
                        y_value = 900
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(enemy1.image, (enemy1.x, enemy1.y))
                    screen.blit(enemy2.image, (enemy2.x, enemy2.y))
                    screen.blit(enemy3.image, (enemy3.x, enemy3.y))
                    screen.blit(enemy4.image, (enemy4.x, enemy4.y))
                    screen.blit(enemy5.image, (enemy5.x, enemy5.y))
                    screen.blit(score_display, (1500, 30))
                    pygame.display.flip()
                    pygame.time.delay(100)
                if event.key == pygame.K_w and not_game_over and boss:
                    y_value -= 50
                    if y_value <= 50:
                        y_value = 50
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(Boss, (boss_x, 200))
                    if boss_damage == 0:
                        screen.blit(Boss_bar_full, (350, 30))
                    if boss_damage == 1:
                        screen.blit(Boss_bar_1, (350, 30))
                    if boss_damage == 2:
                        screen.blit(Boss_bar_2, (350, 30))
                    if boss_damage == 3:
                        screen.blit(Boss_bar_3, (350, 30))
                    if boss_damage == 4:
                        screen.blit(Boss_bar_4, (350, 30))
                    if boss_damage == 5:
                        screen.blit(Boss_bar_5, (350, 30))
                    if boss_damage == 6:
                        screen.blit(Boss_bar_6, (350, 30))
                    if boss_damage == 7:
                        screen.blit(Boss_bar_7, (350, 30))
                    if boss_damage == 8:
                        screen.blit(Boss_bar_8, (350, 30))
                    if boss_damage == 9:
                        screen.blit(Boss_bar_9, (350, 30))
                    if boss_damage == 10:
                        screen.blit(Boss_bar_dead, (350, 30))
                    pygame.display.flip()
                    pygame.time.delay(100)
                if event.key == pygame.K_s and not_game_over and boss:
                    y_value += 50
                    if y_value >= 900:
                        y_value = 900
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(Boss, (boss_x, 200))
                    if boss_damage == 0:
                        screen.blit(Boss_bar_full, (350, 30))
                    if boss_damage == 1:
                        screen.blit(Boss_bar_1, (350, 30))
                    if boss_damage == 2:
                        screen.blit(Boss_bar_2, (350, 30))
                    if boss_damage == 3:
                        screen.blit(Boss_bar_3, (350, 30))
                    if boss_damage == 4:
                        screen.blit(Boss_bar_4, (350, 30))
                    if boss_damage == 5:
                        screen.blit(Boss_bar_5, (350, 30))
                    if boss_damage == 6:
                        screen.blit(Boss_bar_6, (350, 30))
                    if boss_damage == 7:
                        screen.blit(Boss_bar_7, (350, 30))
                    if boss_damage == 8:
                        screen.blit(Boss_bar_8, (350, 30))
                    if boss_damage == 9:
                        screen.blit(Boss_bar_9, (350, 30))
                    if boss_damage == 10:
                        screen.blit(Boss_bar_dead, (350, 30))
                    pygame.display.flip()
                    pygame.time.delay(100)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r and not play:
                    screen.fill((255, 255, 255))
                    screen.blit(Rule, (500, 500))
                    screen.blit(Title, (500, 50))
                    screen.blit(GoBack, (500, 800))
                    pygame.display.flip()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not play:
                    screen.fill((255, 255, 255))
                    screen.blit(Harry, (150, 300))
                    screen.blit(Title, (500, 50))
                    screen.blit(StartMenu, (800, 400))
                    pygame.display.flip()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not play:
                    play = True
                    screen.fill((255, 255, 255))
                    screen.blit(Controls, (1250, 10))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    screen.blit(ClicktoBegin, (500, 500))
                    pygame.display.flip()
                    while not ready:
                        event = pygame.event.wait()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            ready = True
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    pygame.display.flip()
                    y_value = 450
                    screen.fill((52, 61, 82))
                    screen.blit(harry_shoot, (50, y_value))
                    screen.blit(enemy1.image, (1400, enemy1.y))
                    screen.blit(enemy2.image, (1400, enemy2.y))
                    screen.blit(enemy3.image, (1400, enemy3.y))
                    screen.blit(enemy4.image, (1400, enemy4.y))
                    screen.blit(enemy5.image, (1400, enemy5.y))
                    screen.blit(score_display, (1500, 30))
                    pygame.display.flip()
            if not enemy1_alive and not boss:
                movable_tiles.append(enemy1_y_value)
                random_tiles = random.choice(movable_tiles)
                enemy1 = Enemy(1400, random_tiles)
                movable_tiles.remove(random_tiles)
                enemy1_y_value = random_tiles
                enemy1_alive = True
            if not enemy2_alive and not boss:
                movable_tiles.append(enemy2_y_value)
                random_tiles = random.choice(movable_tiles)
                enemy2 = Enemy(1400, random_tiles)
                movable_tiles.remove(random_tiles)
                enemy2_y_value = random_tiles
                enemy2_alive = True
            if not enemy3_alive and not boss:
                movable_tiles.append(enemy3_y_value)
                random_tiles = random.choice(movable_tiles)
                enemy3 = Enemy(1400, random_tiles)
                movable_tiles.remove(random_tiles)
                enemy3_y_value = random_tiles
                enemy3_alive = True
            if not enemy4_alive and not boss:
                movable_tiles.append(enemy4_y_value)
                random_tiles = random.choice(movable_tiles)
                enemy4 = Enemy(1400, random_tiles)
                movable_tiles.remove(random_tiles)
                enemy4_y_value = random_tiles
                enemy4_alive = True
            if not enemy5_alive and not boss:
                movable_tiles.append(enemy5_y_value)
                random_tiles = random.choice(movable_tiles)
                enemy5 = Enemy(1400, random_tiles)
                movable_tiles.remove(random_tiles)
                enemy5_y_value = random_tiles
                enemy5_alive = True
            if enemy1.x <= 50 or enemy2.x <= 50 or enemy3.x <= 50 or enemy4.x <= 50 or enemy5.x <= 50 or boss_x <= 50:
                not_game_over = False
            if not not_game_over:
                if win:
                    screen.fill((52, 61, 81))
                    screen.blit(Win, (400, 500))
                    pygame.display.flip()
                else:
                    screen.fill((52, 61, 81))
                    screen.blit(Gameover, (400, 500))
                    pygame.display.flip()
            if score == 25 and not_run and not_game_over:
                not_run = False
                boss = True
                enemy1.kill()
                enemy2.kill()
                enemy3.kill()
                enemy4.kill()
                enemy5.kill()
                screen.fill((52, 61, 82))
                screen.blit(Boss, (1200, 200))
                screen.blit(harry_shoot, (50, 450))
                screen.blit(Boss_bar_full, (350, 30))
                pygame.display.flip()
            if boss_damage == 10 and reloaded:
                win = True
                not_game_over = False


if __name__ == "__main__":
    main()
