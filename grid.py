import pygame
import time
import numpy as np

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 192, 255)
GREY = (192, 192, 192)
FONT_400 = pygame.font.SysFont('Calibri', 18)
FONT_600 = pygame.font.SysFont('Calibri', 32)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
NUM_COL = 15
NUM_ROW = 10
GRID = []
GRID = np.zeros((NUM_ROW, NUM_COL))
# for i in range(NUM_ROW):
#     GRID.append([])
#     for j in range(NUM_COL):
#         GRID[i].append(0)
window_size = [380, 400]
WIN = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid Search Visual")
clock = pygame.time.Clock()
modes = {
    1: False,
    2: False,
    3: False
}


def update_grid(curr_mode=None):
    WIN.fill(BLACK)
    for row in range(NUM_ROW):
        for column in range(NUM_COL):
            color = WHITE
            if GRID[row][column] == 1:
                color = RED
            if GRID[row][column] == 2:
                color = GREEN
            if GRID[row][column] == 3:
                color = BLUE
            if GRID[row][column] == 4:
                color = LIGHT_BLUE
            pygame.draw.rect(WIN,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    draw_controls(curr_mode)


def draw_controls(mode=None):
    x = 0
    y = (MARGIN + HEIGHT) * NUM_ROW + MARGIN
    w = window_size[0]
    h = window_size[1] - y
    ctrl_box = (x, y, w, h)
    title = FONT_600.render("Controls:  ", 1, RED)
    controls = FONT_400.render("S + Click - Starting Point || E + Click - Ending Point ||", 1, BLACK)
    controls2 = FONT_400.render("R - Reset Grid", 1, BLACK)
    controls3 = FONT_400.render("1 - Shortest Path || 2 - A Star", 1, BLACK)
    controls4 = FONT_400.render(f"Spacebar - Begin                            Mode: {mode if mode else 'None'}", 1,
                                BLACK)
    pygame.draw.rect(WIN, GREY, ctrl_box)
    WIN.blit(title, (0, y))
    WIN.blit(controls, (0, y + 40))
    WIN.blit(controls2, (0, y + 60))
    WIN.blit(controls3, (0, y + 90))
    WIN.blit(controls4, (0, y + 110))
    pygame.display.flip()

def draw_message():
    x = window_size[0] // 14
    y = window_size[1] // 4
    w = window_size[0] // 1.1
    h = window_size[1] // 10
    box = (x, y, w, h)
    words = FONT_400.render('Please Choose a Starting and Ending Position', 1, BLACK)
    pygame.draw.rect(WIN, YELLOW, box)
    WIN.blit(words, (x+10, y))
    pygame.display.flip()
    time.sleep(3)

def get_distance(pointA, pointB):
    # Using Manhattan Distance for "H"
    # "G" will always be 1
    column = pointA[0] // (WIDTH + MARGIN)
    row = pointA[1] // (HEIGHT + MARGIN)
    GRID[row][column] = 3
    print('Coloring Grid ', column, ' ', row)
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


def isGoal(pos, goal):
    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)
    g_column = goal[0] // (WIDTH + MARGIN)
    g_row = goal[1] // (HEIGHT + MARGIN)
    if column == g_column and row == g_row:
        return True
    else:
        return False


def a_star(current, end):
    distances = []
    mode = 'A Star'
    if isGoal(current, end):
        print("YESS")
        return True
    top = (current[0], current[1] - (HEIGHT + MARGIN))
    bottom = (current[0], current[1] + (HEIGHT + MARGIN))
    left = (current[0] - (WIDTH + MARGIN), current[1])
    right = (current[0] + (WIDTH + MARGIN), current[1])
    directions = [right, left, bottom, top]

    for i in directions:
        if i[0] < 0 or i[1] < 0 or i[0] > ((MARGIN + WIDTH) * NUM_COL + MARGIN) or i[1] > (
                (MARGIN + HEIGHT) * NUM_ROW + MARGIN):
            continue
        distances.append(get_distance(i, end))
        update_grid(mode)
        time.sleep(0.2)

    new_curr_pos = distances.index(min(distances))
    new_curr_pos = directions[new_curr_pos]
    new_column = new_curr_pos[0] // (WIDTH + MARGIN)
    new_row = new_curr_pos[1] // (HEIGHT + MARGIN)

    for row in range(NUM_ROW):
        for column in range(NUM_COL):
            if GRID[row][column] == 3:
                GRID[row][column] = 0
    GRID[new_row][new_column] = 4
    update_grid(mode)
    time.sleep(0.2)
    GRID[new_row][new_column] = 1
    return new_curr_pos


def end_sequence(visited, reset=False):
    if reset == True:
        visited.clear()
        GRID.fill(0)
    for i in modes:
        modes[i] = False
    return 'None', False


def main():
    run = True
    searching = False
    curr_mode = ''
    visited = []
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if keys[pygame.K_s]:
                    try:
                        visited.clear()
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        for i in range(NUM_ROW):
                            for j in range(NUM_COL):
                                if GRID[i][j] == 1:
                                    GRID[i][j] = 0
                        GRID[row][column] = 1
                        current_pos = pos
                        print("Click ", pos, "Grid coordinates: ", column, row)
                    except IndexError:
                        continue
                if keys[pygame.K_e]:
                    try:
                        visited.clear()
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        for i in range(NUM_ROW):
                            for j in range(NUM_COL):
                                if GRID[i][j] == 2:
                                    GRID[i][j] = 0
                        GRID[row][column] = 2
                        end_pos = pos
                        print("Click ", pos, "Grid coordinates: ", column, row)
                    except IndexError:
                        continue
            if keys[pygame.K_r]:

                update_grid(end_sequence(visited, True))

            if keys[pygame.K_SPACE] and not searching:
                searching = True

            if keys[pygame.K_1]:
                modes[1] = True
                modes[2] = False
                curr_mode = 'Shortest Path'
            elif keys[pygame.K_2]:
                modes[1] = False
                modes[2] = True
                curr_mode = 'A Star'

        try:
            if searching and modes[2] and current_pos and end_pos:
                visited.append(current_pos)
                current_pos = a_star(current_pos, end_pos)
        except UnboundLocalError:
            draw_message()
            print('Please choose a starting and ending position')
            curr_mode, searching = end_sequence(visited)

        except TypeError:
            curr_mode, searching = end_sequence(visited)
        try:
            if searching:
                for i in visited:
                    column = i[0] // (WIDTH + MARGIN)
                    row = i[1] // (HEIGHT + MARGIN)
                    GRID[row][column] = 1
        except TypeError:
            curr_mode, searching = end_sequence(visited)
        update_grid(curr_mode)
    pygame.quit()


if __name__ == "__main__":
    main()
