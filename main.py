import os
import pygame
from monster import Monster
from click_buff import ClickBuff
from collections import deque
from statistics import Statistics
from worker import Worker
import button_upgrade

# screen
screen = pygame.display.set_mode((1000, 650))
pygame.font.init()
font = pygame.font.SysFont('arial bold', 32)
# title and game icon
pygame.display.set_caption('Clicker game')
##### Classes ######
monster_test = Monster()
click_test = ClickBuff()
statistics_test = Statistics()
work = Worker()


clock = pygame.time.Clock()
time_elapsed_since_last_gold_given = 0

# worker
worker = [pygame.image.load(f'worker_wallpaper/worker.png')]


def numbers_format(num):
    num = float(f'{num:.3g}')
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return f"{str(num).rstrip('0').rstrip('.')}{['', 'K', 'M', 'B', 'T'][magnitude]}"


def static_function():
    # statistics
    stats = font.render(f"STATISTICS", True, (255, 255, 255))
    screen.blit(stats, (140, 120))

    # current_gold
    cur_gold_text = font.render(f"Current Gold:", True, (210, 210, 210))
    screen.blit(cur_gold_text, (5, 170))

    # total_gold_earned
    total_gold_text = font.render(f"Total Gold Earned:", True, (210, 210, 210))
    screen.blit(total_gold_text, (5, 210))

    # monster stats
    total_monster_kill = font.render(f"Total monsters kills:", True, (210, 210, 210))
    screen.blit(total_monster_kill, (5, 250))

    # boss stats
    total_boss_kill = font.render(f"Total boss kills:", True, (210, 210, 210))
    screen.blit(total_boss_kill, (5, 290))

    # upgrade cost
    upgrade = font.render(f"UPGRADES", True, (210, 210, 210))
    upgrade_dmg = font.render(f"Upgrade damage", True, (210, 210, 210))
    cost_upgrade = font.render(f"Cost:", True, (210, 210, 210))
    screen.blit(upgrade_dmg, (5, 500))
    screen.blit(cost_upgrade, (255, 500))
    screen.blit(upgrade, (140, 450))

    # worker cost
    upgrade = font.render(f"Upgrade worker", True, (210, 210, 210))
    worker_up_cost = font.render(f"Cost:", True, (210, 210, 210))
    screen.blit(upgrade, (5, 550))
    screen.blit(worker_up_cost, (255, 550))

    # dps and gold
    curr_dps = font.render(f"Current DPC:", True, (210, 210, 210))
    curr_gold_from_worker = font.render(f"Current gold making:", True, (210, 210, 210))
    screen.blit(curr_dps, (10, 360))
    screen.blit(curr_gold_from_worker, (10, 400))

    # lvl
    lvl_dpc = font.render(f"  lvl: {click_test.current_level}", True, (180, 180, 210))
    lvl_worker = font.render(f"  lvl: {work.current_level}", True, (180, 180, 210))
    screen.blit(lvl_dpc, (360, 500))
    screen.blit(lvl_worker, (360, 550))


def load_wallpapers():
    wallpapers = ('bg_cursor_images/bg.png',
                  'bg_cursor_images/land_monster.png',
                  'bg_cursor_images/hp.png',
                  'bg_cursor_images/mine.jpg',
                  'bg_cursor_images/bg_upgrade.jpg')
    loaded_wallpapers = []
    for wallpaper in wallpapers:
        loaded_wallpapers.append(pygame.image.load(wallpaper))
    monsters_pictures = []
    for filename in os.listdir('monster_wallpaper'):
        if filename.endswith('.png'):
            monsters_pictures.append(pygame.image.load(f'monster_wallpaper/{filename}'))
    bosses_pictures = []
    for filename in os.listdir('boss_wallpaper'):
        if filename.endswith('.png'):
            bosses_pictures.append(pygame.image.load(f'boss_wallpaper/{filename}'))
    return loaded_wallpapers, deque(monsters_pictures), deque(bosses_pictures)


def update_wallpapers(loaded_wallpapers, loaded_monsters, loaded_bosses):
    positions_of_pictures = (
        ("background", 0, 0),
        ("land_monster", 550, 250),
        ("hp", 665, 500),
        ("mine", 700, 0),
        ("bg_upgrade", 0, 100))
    for picture, (pic_name, x, y) in zip(loaded_wallpapers, positions_of_pictures):
        screen.blit(picture, (x, y))
    if monster_test.check_for_boss():
        screen.blit(loaded_bosses[0], (680, 330))
    else:
        screen.blit(loaded_monsters[0], (680, 330))


def dynamic_function():
    level = font.render(f"Level: {monster_test.current_level}", True, (255, 255, 255))
    screen.blit(level, (720, 580))

    # current_gold

    current_gold = font.render(f"{numbers_format(statistics_test.current_gold)}", True, (210, 210, 210))
    screen.blit(current_gold, (160, 170))

    # # total_gold_earned

    total_gold_display = font.render(f"{numbers_format(statistics_test.total_gold)}", True, (210, 210, 210))
    screen.blit(total_gold_display, (207, 210))

    # # monster stats

    total_monster_display = font.render(f"{numbers_format(statistics_test.total_monsters_kills)}", True,
                                        (210, 210, 210))
    screen.blit(total_monster_display, (230, 250))

    # # boss stats

    total_boss_display = font.render(f"{numbers_format(statistics_test.total_boss_kills)}", True, (210, 210, 210))
    screen.blit(total_boss_display, (180, 290))

    # # upgrade cost

    upgrade_gold = font.render(f"{numbers_format(click_test.start_gold_cost)}", True, (210, 210, 210))
    screen.blit(upgrade_gold, (315, 500))

    worker_cost = font.render(f"{numbers_format(work.start_gold_cost)}", True, (210, 210, 210))
    screen.blit(worker_cost, (315, 550))

    dps = font.render(f"{statistics_test.start_dmg}", True, (210, 210, 210))
    screen.blit(dps, (160, 360))
    worker_gold = font.render(f"{work.start_gold}", True, (210, 210, 210))
    screen.blit(worker_gold, (243, 400))


def buttons():
    upgrade_img = pygame.image.load('bg_cursor_images/blue.png')
    upgrade_button = button_upgrade.ButtonUpgrade(205, 485, upgrade_img, 0.8)

    worker_img = pygame.image.load('bg_cursor_images/yellow.png')
    worker_button = button_upgrade.ButtonUpgrade(205, 535, worker_img, 0.8)

    if upgrade_button.draw(screen) and pygame.event.wait():
        click_test.level_up(statistics_test)

    if worker_button.draw(screen) and pygame.event.wait():
        work.level_up(statistics_test)


def mouse_vis():
    mouse = pygame.image.load('bg_cursor_images/cursor.png')
    pygame.mouse.set_visible(False)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x <= 0:
        mouse_x = 0
    elif mouse_x >= 970:
        mouse_x = 970
    elif mouse_y >= 620:
        mouse_y = 620
    screen.blit(mouse, (mouse_x, mouse_y))


def worker_vis():
    global time_elapsed_since_last_gold_given

    worker = pygame.image.load('worker_wallpaper/worker.png')
    dt = clock.tick()
    if work.bought_worker:
        time_elapsed_since_last_gold_given += dt
        if time_elapsed_since_last_gold_given >= work.seconds_for_gold * 1000:
            work.add_gold_from_worker(statistics_test)
            time_elapsed_since_last_gold_given = 0
        screen.blit(worker, (850, 50))


all_wallpapers, all_monsters, all_bosses = load_wallpapers()
is_attacking = False
run = True
while run:

    update_wallpapers(all_wallpapers, all_monsters, all_bosses)
    dynamic_function()
    static_function()
    worker_vis()

    fps = pygame.time.Clock().tick(60)

    rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(200, 200)
    rect = pygame.Rect.move(rect, 250, 70)
    point = pygame.mouse.get_pos()
    collide = rect.collidepoint(point)

    text = font.render(f'{numbers_format(monster_test.attacked_monster)}', True, (255, 255, 255))
    screen.blit(text, (690, 537))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        left_click, middle_click, right_click = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN and left_click and collide and not is_attacking:
            is_attacking = True
            monster_test.attack_monster(click_test)
            if monster_test.check_if_dead():
                if monster_test.check_for_boss():
                    all_bosses.rotate(-1)
                    statistics_test.current_gold += monster_test.gold_per_boss_kill
                    statistics_test.total_gold += monster_test.gold_per_boss_kill
                    statistics_test.total_boss_kills += 1
                else:
                    statistics_test.current_gold += monster_test.gold_drop_normal_monster
                    statistics_test.total_gold += monster_test.gold_drop_normal_monster
                    statistics_test.total_monsters_kills += 1
                    all_monsters.rotate(-1)
                monster_test.prepare_next_level()
        elif event.type == pygame.MOUSEBUTTONUP:
            is_attacking = False

    buttons()
    mouse_vis()
    pygame.display.update()
pygame.quit()
