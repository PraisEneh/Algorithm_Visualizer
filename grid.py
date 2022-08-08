import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
NUM_COL = 15
NUM_ROW = 10
GRID = np.zeros((NUM_ROW, NUM_COL))
GRID[0][0] = 1
pygame.init()
window_size = [400, 400]
WIN = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()


def update_grid():
    WIN.fill(BLACK)
    for row in range(NUM_ROW):
        for column in range(NUM_COL):
            color = WHITE
            if GRID[row][column] == 1:
                color = RED
            pygame.draw.rect(WIN,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
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
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    GRID[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
        update_grid()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
