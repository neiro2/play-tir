from turtledemo.nim import SCREENWIDTH

import  pygame
import random

pygame.init()

SCREEN_WIDTH = 800 # ширина экрана
SCREEN_HEIGHT = 600 # длина экрана

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT )) # установили экран с размерами

pygame.display.set_caption('Игра Тир') # название игры

icon = pygame.image.load('img/icon.png') # загрузили иконку
pygame.display.set_icon(icon) # установили иконку

target_image = pygame.image.load('img/target.png') # создаем переменную изображение иконки

target_width = 80 # ширина
target_height = 80 # высота

#target_x = random.randint (0,SCREEN_WIDTH - target_width)
target_y = random.randint (0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




running = True
while running:
    pass

pygame.quit()