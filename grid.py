import pygame
import numpy as np

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
NUM_COL = 15
NUM_ROW = 10
grid = np.zeros((NUM_ROW, NUM_COL))
grid[1][5] = 1
pygame.init()
window_size = [400, 400]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()


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
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
        scr.fill(black)
        for row in range(NUM_ROW):
            for column in range(NUM_COL):
                color = white
                if grid[row][column] == 1:
                    color = red
                pygame.draw.rect(scr,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
