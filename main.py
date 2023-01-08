import os
import pygame

# screen
screen = pygame.display.set_mode((1000, 650))

# wallpapers
background = pygame.image.load('bg_cursor_images/bg.png')
land_background = pygame.image.load('bg_cursor_images/land_monster.png')
mouse = pygame.image.load('bg_cursor_images/cursor.png')
hp_bar = pygame.image.load('bg_cursor_images/hp.png')
mine = pygame.image.load('bg_cursor_images/mine.jpg')
bg_for_upgrade = pygame.image.load('bg_cursor_images/bg_upgrade.jpg')

# title and game icon
pygame.display.set_caption('Clicker game')

# append monster/ worker/ boss
# monster
monsters = []

for filename in os.listdir('monster_wallpaper'):
    if filename.endswith('.png'):
        monsters.append(pygame.image.load(f'monster_wallpaper/{filename}'))


# boss
boss = []
for filename in os.listdir('boss_wallpaper'):
    if filename.endswith('.png'):
        boss.append(pygame.image.load(f'boss_wallpaper/{filename}'))

# worker
worker = []
worker.append(pygame.image.load(f'worker_wallpaper/worker.png'))


run = True
while run:

    # background
    screen.blit(background, (0, 0))

    # background for upgrades
    screen.blit(bg_for_upgrade, (0, 100))

    # land background
    screen.blit(land_background, (550, 250))

    # monsters test
    # screen.blit(monsters[6], (680, 330))

    # mine test
    screen.blit(mine, (700, 0))

    # worker test
    # screen.blit(worker[0], (850, 60))

    # hp bar
    screen.blit(hp_bar, (665, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # mouse settings
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    if x <= 0:
        x = 0
    elif x >= 970:
        x = 970
    elif y >= 620:
        y = 620

    screen.blit(mouse, (x, y))







    pygame.display.update()

pygame.quit()
