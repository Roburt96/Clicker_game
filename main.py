import os
import pygame
from monster import Monster
from click_buff import ClickBuff
from collections import deque

# screen
screen = pygame.display.set_mode((1000, 650))


def numbers_format(num):
    num = float(f'{num:.3g}')
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return f"{str(num).rstrip('0').rstrip('.')}{['', 'K', 'M', 'B', 'T'][magnitude]}"


# print(numbers_format(999999999999))


def load_wallpapers():
    wallpapers = ('bg_cursor_images/bg.png',
                  'bg_cursor_images/land_monster.png',
                  'bg_cursor_images/hp.png',
                  'bg_cursor_images/mine.jpg',
                  'bg_cursor_images/bg_upgrade.jpg',
                  'bg_cursor_images/cursor.png')
    loaded_wallpapers = []
    for wallpaper in wallpapers:
        loaded_wallpapers.append(pygame.image.load(wallpaper))
    monsters_pictures = []
    for filename in os.listdir('monster_wallpaper'):
        if filename.endswith('.png'):
            monsters_pictures.append(pygame.image.load(f'monster_wallpaper/{filename}'))
    monsters_pictures = monsters_pictures * len(os.listdir('boss_wallpaper'))
    position_boss_every_10_levels = 9
    for filename in os.listdir('boss_wallpaper'):
        if filename.endswith('.png'):
            monsters_pictures.insert(position_boss_every_10_levels, pygame.image.load(f'boss_wallpaper/{filename}'))
            position_boss_every_10_levels += 10
    return loaded_wallpapers, deque(monsters_pictures)


def update_wallpapers(loaded_wallpapers, loaded_monsters):
    pygame.mouse.set_visible(False)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x <= 0:
        mouse_x = 0
    elif mouse_x >= 970:
        mouse_x = 970
    elif mouse_y >= 620:
        mouse_y = 620
    positions_of_pictures = (
        ("background", 0, 0),
        ("land_monster", 550, 250),
        ("hp", 665, 500),
        ("mine", 700, 0),
        ("bg_upgrade", 0, 100),
        ("cursor", mouse_x, mouse_y)
         )
    for picture, (pic_name, x, y) in zip(loaded_wallpapers, positions_of_pictures):
        screen.blit(picture, (x, y))
    screen.blit(loaded_monsters[0], (680, 330))
    screen.blit(loaded_wallpapers[-1], (mouse_x, mouse_y))  # mouse must blit last to overlap all the other pictures


# title and game icon
pygame.display.set_caption('Clicker game')


# worker
worker = [pygame.image.load(f'worker_wallpaper/worker.png')]
monster_test = Monster()
click_test = ClickBuff()

all_wallpapers, all_monsters = load_wallpapers()
######################### TEST ###################################
mobs = deque(["normal"] * 9 + ["boss"] + ["normal"] * 9 + ["boss"])
####################################################################
run = True
while run:
    update_wallpapers(all_wallpapers, all_monsters)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ################# MOST LIKELY WILL BE REMOVED #########################
    rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(200, 200)
    rect = pygame.Rect.move(rect, 250, 70)
    point = pygame.mouse.get_pos()
    collide = rect.collidepoint(point)
    ########################################################################
    pygame.font.init()
    font = pygame.font.SysFont('arial bold', 40)
    text = font.render(f'{monster_test.attacked_monster} / {monster_test.monster_hp}', True, (255, 255, 255))
    screen.blit(text, (690, 537))
    if collide:
        if pygame.mouse.get_pressed()[0] and pygame.event.wait():
            monster_test.attack_monster(click_test)
            if monster_test.check_if_dead():
                all_monsters.rotate(-1)
                mobs.rotate(-1)


    ######################## TESTING ###########################
    mob_name = font.render(f"{mobs[0]}", True, (200, 200, 200))
    screen.blit(mob_name, (690, 450))
    level = font.render(f"{monster_test.current_level}", True, (200, 200, 200))
    screen.blit(level, (720, 580))
    ##################################################################

    pygame.display.update()
pygame.quit()
