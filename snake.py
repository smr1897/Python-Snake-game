import pygame as pg
from random import randrange
import button as button

WINDOW = 700
screen = pg.display.set_mode([WINDOW]*2)

#Load button images
start_img = pg.image.load('start_btn.png').convert_alpha()
exit_img = pg.image.load('exit_btn.png').convert_alpha()

snake_img = pg.image.load('snakef.png').convert_alpha()
snake_rect = snake_img.get_rect(center=(400,500))

#Create button instance
start_button = button.Button(100,200,start_img,0.8)
exit_button = button.Button(500,200,exit_img,0.8)

while True:

    screen.fill((202,228,241))
    screen.blit(snake_img,(snake_rect))

    if start_button.draw(screen):
        TILE_SIZE  = 40
        RANGE = (TILE_SIZE//2,WINDOW-TILE_SIZE//2,TILE_SIZE)
        get_random_position = lambda: [randrange(*RANGE),randrange(*RANGE)]
        snake = pg.rect.Rect([0,0,TILE_SIZE-2,TILE_SIZE-2])
        snake.center = get_random_position()
        length = 1
        segments = [snake.copy()]
        snake_direction = (0,0)
        time,time_step = 0,100
        food = snake.copy()
        food.center = get_random_position()

        clock = pg.time.Clock()
        #Avoiding to move to opposite direction when there is only two segments
        dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}

        while True:
            for event in pg.event.get():
                if event.type ==  pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and dirs[pg.K_w]:
                        snake_direction = (0,-TILE_SIZE)
                        dirs = {pg.K_w : 1,pg.K_s : 0,pg.K_a : 1,pg.K_d : 1}
                    if event.key == pg.K_s and dirs[pg.K_s]:
                        snake_direction = (0,TILE_SIZE)
                        dirs = {pg.K_w : 0,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}
                    if event.key == pg.K_a and dirs[pg.K_a]:
                        snake_direction = (-TILE_SIZE,0)
                        dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 0}
                    if event.key == pg.K_d and dirs[pg.K_d]:
                        snake_direction = (TILE_SIZE,0)
                        dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 0,pg.K_d : 1}
                screen.fill('black')
                #Checking if the snake is out of bounds
                self_eating = pg.Rect.collidelist(snake,segments[:-1]) != -1
                if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
                    snake.center , food.center = get_random_position(),get_random_position()
                    length , snake_direction = 1 , (0,0)
                    segments = [snake.copy()]
                #Checking if the food location and snake location is a match
                if snake.center == food.center:
                    food.center = get_random_position()
                    length += 1
                #Draw food
                pg.draw.rect(screen,'green',food)
                # Draw snake
                [pg.draw.rect(screen,'red',segment)for segment in segments]
                #Move snake
                time_now = pg.time.get_ticks()
                if time_now-time > time_step:
                    time = time_now
                    snake.move_ip(snake_direction)
                    segments.append(snake.copy())
                    segments = segments[-length:]#Keeps the last element in the list
                pg.display.flip()
                clock.tick(60)
    if exit_button.draw(screen):
        exit()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()            
    pg.display.update()



# TILE_SIZE  = 30
# RANGE = (TILE_SIZE//2,WINDOW-TILE_SIZE//2,TILE_SIZE)
# get_random_position = lambda: [randrange(*RANGE),randrange(*RANGE)]
# snake = pg.rect.Rect([0,0,TILE_SIZE-2,TILE_SIZE-2])
# snake.center = get_random_position()
# length = 1
# segments = [snake.copy()]
# snake_direction = (0,0)
# time,time_step = 0,100
# food = snake.copy()
# food.center = get_random_position()

# clock = pg.time.Clock()
# #Avoiding to move to opposite direction when there is only two segments
# dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}

# while True:
#     for event in pg.event.get():
#         if event.type ==  pg.QUIT:
#             exit()
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_w and dirs[pg.K_w]:
#                 snake_direction = (0,-TILE_SIZE)
#                 dirs = {pg.K_w : 1,pg.K_s : 0,pg.K_a : 1,pg.K_d : 1}
#             if event.key == pg.K_s and dirs[pg.K_s]:
#                 snake_direction = (0,TILE_SIZE)
#                 dirs = {pg.K_w : 0,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}
#             if event.key == pg.K_a and dirs[pg.K_a]:
#                 snake_direction = (-TILE_SIZE,0)
#                 dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 0}
#             if event.key == pg.K_d and dirs[pg.K_d]:
#                 snake_direction = (TILE_SIZE,0)
#                 dirs = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 0,pg.K_d : 1}
#         screen.fill('black')
#         #Checking if the snake is out of bounds
#         self_eating = pg.Rect.collidelist(snake,segments[:-1]) != -1
#         if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
#             snake.center , food.center = get_random_position(),get_random_position()
#             length , snake_direction = 1 , (0,0)
#             segments = [snake.copy()]
#         #Checking if the food location and snake location is a match
#         if snake.center == food.center:
#             food.center = get_random_position()
#             length += 1
#         #Draw food
#         pg.draw.rect(screen,'green',food)
#         # Draw snake
#         [pg.draw.rect(screen,'red',segment)for segment in segments]
#         #Move snake
#         time_now = pg.time.get_ticks()
#         if time_now-time > time_step:
#             time = time_now
#             snake.move_ip(snake_direction)
#             segments.append(snake.copy())
#             segments = segments[-length:]#Keeps the last element in the list
#         pg.display.flip()
#         clock.tick(60)