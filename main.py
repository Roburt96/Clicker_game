import os
import pygame

# screen / background
screen = pygame.display.set_mode((1000, 650))
background = pygame.image.load('bg_cursor_images/background.png')
land_background = pygame.image.load('bg_cursor_images/land_monster.png')
mouse = pygame.image.load('bg_cursor_images/cursor1.png')

# title and game icon
pygame.display.set_caption('Clicker game')

# append monster/ worker/ boss
# monster
monsters = []
for filename in os.listdir('monster_wallpaper'):
    if filename.endswith('.png'):
        monsters.append(filename)
# boss
boss = []
for filename in os.listdir('boss_wallpaper'):
    if filename.endswith('.png'):
        boss.append(filename)
# worker
worker = []
for filename in os.listdir('worker_wallpaper'):
    if filename.endswith('.png'):
        boss.append(filename)


run = True
while run:

    # background
    screen.blit(background, (0, 0))

    # land background
    screen.blit(land_background, (550, 250))

    # monsters test
    # screen.blit(monster, (680, 330))
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
