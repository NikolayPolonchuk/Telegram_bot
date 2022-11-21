import pygame
import time
import random


snake_speed = 7

plus_speed = 0

plus_score = 10

size = 20


# Размер окна
window_x = 720
window_y = 480

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

crush = pygame.Color(0, 255, 255)

# Запуск pygame и установка параметров
pygame.init()

pygame.display.set_caption("Snakes PvP")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# Начальные позиции голов
green_snake_position = [100, 60]

blue_snake_position = [600, 420]

# первые 3 (или 6) блоков змей
green_snake_body = [[100, 60], [80, 60], [60, 60]]  # , [40, 60], [20, 60], [0, 60]]


blue_snake_body = [[600, 420], [620, 420], [640, 420]]  # , [40, 420], [20, 420], [0, 420]]


# позиция яблока
fruit_position = [
    random.randrange(1, (window_x // size)) * size,
    random.randrange(1, (window_y // size)) * size,
]

fruit_spawn = True

# Начальные направления
green_direction = "RIGHT"
green_change_to = green_direction

blue_direction = "LEFT"
blue_change_to = blue_direction


# Счёт
green_score = 0

blue_score = 0

# показывает Счёт
def show_score(choice, color, font, size):\

    global players_choise
    global green_score
    global blue_score

    score_font = pygame.font.SysFont(font, size)

    if players_choise:
        score_surface = score_font.render(
            "Score green: " + str(green_score) + "     Score blue: " + str(blue_score),
            True,
            color,
        )
    else:
        score_surface = score_font.render(
            "Score green: " + str(green_score),
            True,
            color,
        )

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)


# game over
def game_over(X, Y, color):

    global snake_speed

    snake_speed = 5

    global green_snake_body
    global green_snake_position
    global green_change_to
    global green_direction
    global green_score

    global blue_snake_body
    global blue_snake_position
    global blue_change_to
    global blue_direction
    global blue_score


    while True:

        for pos in green_snake_body:
            pygame.draw.rect(
                game_window, green, pygame.Rect(pos[0] + 1, pos[1] + 1, size - 2, size - 2)
            )

        for pos in blue_snake_body:
            pygame.draw.rect(
                game_window, blue, pygame.Rect(pos[0] + 1, pos[1] + 1, size - 2, size - 2)
            )

        pygame.draw.rect(
        game_window,
        crush,
        pygame.Rect(X + 1, Y + 1, size - 2, size - 2),
        )

        

        my_font = pygame.font.SysFont("arial", 50)

        # Создание конечного текста
        if green_score > blue_score:
            game_over_surface1 = my_font.render(
                "Green WINS with score: "
                + str(green_score),
                True,
                color,
            )

            game_over_surface2 = my_font.render(
                "  Blue score: "
                + str(blue_score),
                True,
                color,
            )

        elif green_score < blue_score:
            game_over_surface1 = my_font.render(
                "Blue WINS with score: "
                + str(blue_score),
                True,
                color,
            )

            game_over_surface2 = my_font.render(
                "  Green score: "
                + str(green_score),
                True,
                color,
            )

        else:
            game_over_surface1 = my_font.render(
                "DRAW score: " + str(green_score), True, color
            )

            game_over_surface2 = my_font.render(
                "  ",
                True,
                color,
            )
        
        little_font = pygame.font.SysFont("arial", 35)

        game_over_surface0 = little_font.render(
            "Q - exit    R - restart",
            True,
            color,
        )


        action = "nothing"

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    action = "quit"

                elif event.key == pygame.K_r:
                    action = "restart"


        game_over_rect = game_over_surface1.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface1, game_over_rect)

        game_over_rect = game_over_surface2.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 2)
        game_window.blit(game_over_surface2, game_over_rect)

        game_over_rect = game_over_surface0.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4 * 3)
        game_window.blit(game_over_surface0, game_over_rect)
        
        pygame.display.flip()

        if action == "quit":
            pygame.quit()

            quit()
        
        if action == "restart":
            green_snake_position = [100, 60]

            blue_snake_position = [600, 420]

            # первые 3 (или 6) блоков змей
            green_snake_body.clear()
            green_snake_body.append([100, 60])
            green_snake_body.append([80, 60])
            green_snake_body.append([60, 60])


            blue_snake_body.clear()
            blue_snake_body.append([600, 420])
            blue_snake_body.append([620, 420])
            blue_snake_body.append([640, 420])


            # позиция яблока
            fruit_position = [
                random.randrange(1, (window_x // size)) * size,
                random.randrange(1, (window_y // size)) * size,
            ]

            fruit_spawn = True

            # Начальные направления
            green_direction = "RIGHT"
            green_change_to = green_direction

            blue_direction = "LEFT"
            blue_change_to = blue_direction


            # Счёт
            green_score -= green_score

            blue_score -= blue_score

            break
        
        pygame.display.flip()

        fps.tick(1)




# Выбор количества игроков
players_choise = False
press = True
while press:

    game_window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_1:
                players_choise = False
                press = False
            elif event.key == pygame.K_2:
                players_choise = True
                press = False


    my_font = pygame.font.SysFont("arial", 50)

    players1 = my_font.render(
        "1. One player",
        True,
        red,
    )

    players2 = my_font.render(
        "2. Two players",
        True,
        red,
    )

    game_over_rect = players1.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(players1, game_over_rect)

    game_over_rect = players2.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(players2, game_over_rect)

    pygame.display.flip()

    fps.tick(snake_speed)



# Выбор уровня сложности
press = True
while press:

    game_window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_1:
                press = False
            elif event.key == pygame.K_2:
                plus_score += 10
                plus_speed += 1
                press = False
            elif event.key == pygame.K_3:
                plus_score += 30
                plus_speed += 2
                press = False


    my_font = pygame.font.SysFont("arial", 50)

    game_mode1 = my_font.render(
        "1. Easy",
        True,
        red,
    )

    game_mode2 = my_font.render(
        "2. Medium",
        True,
        red,
    )

    game_mode3 = my_font.render(
        "3. Hard",
        True,
        red,
    )

    game_over_rect = game_mode1.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 6)
    game_window.blit(game_mode1, game_over_rect)

    game_over_rect = game_mode2.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 3)
    game_window.blit(game_mode2, game_over_rect)

    game_over_rect = game_mode3.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(game_mode3, game_over_rect)

    pygame.display.flip()

    fps.tick(snake_speed)



# Режимы
if players_choise:
    
    # Основное тело для двух игроков
    while True:

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_w:
                    green_change_to = "UP"
                elif event.key == pygame.K_s:
                    green_change_to = "DOWN"
                elif event.key == pygame.K_a:
                    green_change_to = "LEFT"
                elif event.key == pygame.K_d:
                    green_change_to = "RIGHT"

                if event.key == pygame.K_UP:
                    blue_change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    blue_change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    blue_change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    blue_change_to = "RIGHT"

        # Обработка нажатия в противоположную сторону
        if green_change_to == "UP" and green_direction != "DOWN":
            green_direction = "UP"
        elif green_change_to == "DOWN" and green_direction != "UP":
            green_direction = "DOWN"
        elif green_change_to == "LEFT" and green_direction != "RIGHT":
            green_direction = "LEFT"
        elif green_change_to == "RIGHT" and green_direction != "LEFT":
            green_direction = "RIGHT"

        if blue_change_to == "UP" and blue_direction != "DOWN":
            blue_direction = "UP"
        elif blue_change_to == "DOWN" and blue_direction != "UP":
            blue_direction = "DOWN"
        elif blue_change_to == "LEFT" and blue_direction != "RIGHT":
            blue_direction = "LEFT"
        elif blue_change_to == "RIGHT" and blue_direction != "LEFT":
            blue_direction = "RIGHT"

        # Передвижение зелёной змеи
        if green_direction == "UP":
            green_snake_position[1] -= size
        elif green_direction == "DOWN":
            green_snake_position[1] += size
        elif green_direction == "LEFT":
            green_snake_position[0] -= size
        elif green_direction == "RIGHT":
            green_snake_position[0] += size

        # Передвижение синей
        if blue_direction == "UP":
            blue_snake_position[1] -= size
        elif blue_direction == "DOWN":
            blue_snake_position[1] += size
        elif blue_direction == "LEFT":
            blue_snake_position[0] -= size
        elif blue_direction == "RIGHT":
            blue_snake_position[0] += size

        # Поедание фрукта (длина увеличивается на 1, счёт на 10)
        # В сложном режиме возрастает скорость
        green_snake_body.insert(0, list(green_snake_position))
        if (
            green_snake_position[0] == fruit_position[0]
            and green_snake_position[1] == fruit_position[1]
        ):
            snake_speed += plus_speed
            green_score += 10
            fruit_spawn = False
        else:
            green_snake_body.pop()

        blue_snake_body.insert(0, list(blue_snake_position))
        if (
            blue_snake_position[0] == fruit_position[0]
            and blue_snake_position[1] == fruit_position[1]
        ):
            snake_speed += plus_speed
            blue_score += 10
            fruit_spawn = False
        else:
            blue_snake_body.pop()

        while not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // size)) * size,
                random.randrange(1, (window_y // size)) * size,
            ]
            if not (
                fruit_position in green_snake_body or fruit_position in blue_snake_body
            ):
                break

        fruit_spawn = True
        game_window.fill(black)
            
        pygame.draw.rect(
        game_window,
        white,
        pygame.Rect(fruit_position[0] + 1, fruit_position[1] + 1, size - 2, size - 2),
        )


        for pos in green_snake_body:
            pygame.draw.rect(
                game_window, green, pygame.Rect(pos[0] + 1, pos[1] + 1, size - 2, size - 2)
            )

        for pos in blue_snake_body:
            pygame.draw.rect(
                game_window, blue, pygame.Rect(pos[0] + 1, pos[1] + 1, size - 2, size - 2)
            )



        # Обработка выхода за границу
        if green_snake_position[0] < 0 or green_snake_position[0] > window_x - size:
            if green_score > 50:
                green_score -= 50
            else:
                green_score = 0
            game_over(green_snake_position[0], green_snake_position[1], red)
        elif green_snake_position[1] < 0 or green_snake_position[1] > window_y - size:
            if green_score > 50:
                green_score -= 50
            else:
                green_score = 0
            game_over(green_snake_position[0], green_snake_position[1], red)

        if blue_snake_position[0] < 0 or blue_snake_position[0] > window_x - size:
            if blue_score > 50:
                blue_score -= 50
            else:
                blue_score = 0
            game_over(blue_snake_position[0], blue_snake_position[1], red)
        elif blue_snake_position[1] < 0 or blue_snake_position[1] > window_y - size:
            if blue_score > 50:
                blue_score -= 50
            else:
                blue_score = 0
            game_over(blue_snake_position[0], blue_snake_position[1], red)

        # Столкновение голов
        if (
            green_snake_position[0] == blue_snake_position[0]
            and green_snake_position[1] == blue_snake_position[1]
        ):
            game_over(green_snake_position[0], green_snake_position[1], red)

        # Столкновение с зелёной змеёй
        for block in green_snake_body[1:]:
            if green_snake_position[0] == block[0] and green_snake_position[1] == block[1]:
                if green_score < 50:
                    green_score = 0
                else:
                    green_score -= 50

                game_over(green_snake_position[0], green_snake_position[1], red)

            if blue_snake_position[0] == block[0] and blue_snake_position[1] == block[1]:
                green_score += 10

                game_over(blue_snake_position[0], blue_snake_position[1], red)

        # Столкновение с синей змеёй
        for block in blue_snake_body[1:]:
            if green_snake_position[0] == block[0] and green_snake_position[1] == block[1]:
                blue_score += 10

                game_over(green_snake_position[0], green_snake_position[1], red)

            if blue_snake_position[0] == block[0] and blue_snake_position[1] == block[1]:
                if blue_score < 50:
                    blue_score = 0
                else:
                    blue_score -= 50

                game_over(blue_snake_position[0], blue_snake_position[1], red)


        show_score(1, white, "arial", 20)

        pygame.display.flip()

        fps.tick(snake_speed)


else:

# Основное тело для одного игрока
    while True:

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    green_change_to = "UP"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    green_change_to = "DOWN"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    green_change_to = "LEFT"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    green_change_to = "RIGHT"


        # Обработка нажатия в противоположную сторону
        if green_change_to == "UP" and green_direction != "DOWN":
            green_direction = "UP"
        elif green_change_to == "DOWN" and green_direction != "UP":
            green_direction = "DOWN"
        elif green_change_to == "LEFT" and green_direction != "RIGHT":
            green_direction = "LEFT"
        elif green_change_to == "RIGHT" and green_direction != "LEFT":
            green_direction = "RIGHT"

        # Передвижение зелёной змеи
        if green_direction == "UP":
            green_snake_position[1] -= size
        elif green_direction == "DOWN":
            green_snake_position[1] += size
        elif green_direction == "LEFT":
            green_snake_position[0] -= size
        elif green_direction == "RIGHT":
            green_snake_position[0] += size


        # Поедание фрукта (длина увеличивается на 1, счёт на 10)
        # В сложном режиме возрастает скорость
        green_snake_body.insert(0, list(green_snake_position))
        if (
            green_snake_position[0] == fruit_position[0]
            and green_snake_position[1] == fruit_position[1]
        ):
            snake_speed += plus_speed
            green_score += 10
            fruit_spawn = False
        else:
            green_snake_body.pop()

        while not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // size)) * size,
                random.randrange(1, (window_y // size)) * size,
            ]
            if not (
                fruit_position in green_snake_body
            ):
                break

        fruit_spawn = True
        game_window.fill(black)
            
        pygame.draw.rect(
        game_window,
        white,
        pygame.Rect(fruit_position[0] + 1, fruit_position[1] + 1, size - 2, size - 2),
        )

        for pos in green_snake_body:
            pygame.draw.rect(
                game_window, green, pygame.Rect(pos[0] + 1, pos[1] + 1, size - 2, size - 2)
            )


        # Обработка выхода за границу
        if green_snake_position[0] < 0 or green_snake_position[0] > window_x - size:
            game_over(green_snake_position[0], green_snake_position[1], red)

        elif green_snake_position[1] < 0 or green_snake_position[1] > window_y - size:
            game_over(green_snake_position[0], green_snake_position[1], red)


        # Столкновение с хвост
        for block in green_snake_body[1:]:
            if green_snake_position[0] == block[0] and green_snake_position[1] == block[1]:
                game_over(green_snake_position[0], green_snake_position[1], red)


        show_score(1, white, "arial", 20)

        pygame.display.flip()

        fps.tick(snake_speed)
