import pygame
import numpy as np
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
start_pos = ()
end_pos = ()
# for i in range(NUM_ROW):
#     GRID.append([])
#     for j in range(NUM_COL):
#         GRID[i].append(0)
GRID[0][0] = 1
window_size = [380, 400]
WIN = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid Search Visual")
clock = pygame.time.Clock()
searching = False
modes = {
    1: False,
    2: False,
    3: False
}


def update_grid():
    WIN.fill(BLACK)
    for row in range(NUM_ROW):
        for column in range(NUM_COL):
            color = WHITE
            if GRID[row][column] == 1:
                color = RED
            if GRID[row][column] == 2:
                color = GREEN
            pygame.draw.rect(WIN,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

def draw_controls(mode=None):
    x = 0
    y = (MARGIN + HEIGHT) * NUM_ROW + MARGIN
    w = window_size[0]
    h = window_size[1] - y
    ctrl_box = (x, y, w, h)
    title = FONT_600.render("Controls:  ", 1, RED)
    controls = FONT_400.render("S+Click - Starting Point || E+Click - Ending Point", 1, BLACK)
    controls2 = FONT_400.render("1 - BFS || 2 - DFS || 3 - A Star", 1, BLACK)
    controls3 = FONT_400.render(f"Spacebar - Begin                                 Mode: {mode}", 1, BLACK)
    pygame.draw.rect(WIN, GREY, ctrl_box)
    WIN.blit(title, (0, y))
    WIN.blit(controls, (0, y+40))
    WIN.blit(controls2, (0, y+60))
    WIN.blit(controls3, (0, y+120))
    pygame.display.flip()


def main():
    run = True
    while run:
        clock.tick(50)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if keys[pygame.K_s]:
                    try:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        for i in range(NUM_ROW):
                            for j in range(NUM_COL):
                                if GRID[i][j] == 1:
                                    GRID[i][j] = 0
                        GRID[row][column] = 1
                        start_pos = (row, column)
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    except IndexError:
                        continue
                if keys[pygame.K_e]:
                    try:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        for i in range(NUM_ROW):
                            for j in range(NUM_COL):
                                if GRID[i][j] == 2:
                                    GRID[i][j] = 0
                        GRID[row][column] = 2
                        end_pos = (row, column)
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    except IndexError:
                        continue
        update_grid()
        draw_controls()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
