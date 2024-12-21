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

target_x = random.randint (0,SCREEN_WIDTH - target_width)
target_y = random.randint (0, SCREEN_HEIGHT - target_height)
speed_x = random.choice ([0,5])
speed_y = random.choice ([0,5])


color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
  screen.fill(color)  # заливаем экран рондомным цветом
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # условие для завершения игры при нажатии на крестик
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:  # условия для обработки клика мышью
            mouse_x, mouse_y = pygame.mouse.get_pos()  # определения места на экране, в котором была нажата кнопка мыши.
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:  # условие, определяющее, попал ли клик мышки по мишени
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_image,(target_x, target_y))  # Таким образом мы прописали отрисовку мишени в рандомных координатах.
    pygame.display.update()  # С этой командой в цикле while будет происходить обновление экрана с новым расположением мишени.


pygame.quit()