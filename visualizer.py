import math, time
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
HEIGHT = 400
WIDTH = 700
FPS = 25
lst_size = 25
rand_range = 50


class DrawDetails:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY_GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    PADDING = 100
    PADDING_TOP = 150

    FONT_400 = pygame.font.SysFont('Calibri', 18)
    FONT_600 = pygame.font.SysFont('Calibri', 32)

    def __init__(self, lst, width, height):
        self.width = width
        self.height = height
        self.WIN = pygame.display.set_mode([width, height])
        self.sort_WIN = (
            self.PADDING // 2, self.PADDING_TOP, self.width - (self.PADDING), self.height - self.PADDING_TOP)
        pygame.display.set_caption("Algorithm Visualizer")
        print(lst)
        self.set_list(lst)
        self.draw()

    def set_list(self, lst):
        self.lst = lst
        self.lst_min = min(lst)
        self.lst_max = max(lst)

        self.block_x = self.PADDING // 2
        self.block_height = math.floor((self.height - self.PADDING_TOP) / (self.lst_max - self.lst_min))
        self.block_width = round((self.width - self.PADDING_TOP) / len(lst))

    def draw(self):
        self.draw_controls()
        self.draw_list()

    def draw_controls(self, ascending=True):
        self.WIN.fill(self.WHITE)
        x = (self.width // 2) - (self.PADDING // 2)
        y = (self.PADDING_TOP // 2) - 50
        title = self.FONT_600.render("Controls:  ", 1, self.RED)
        controls = self.FONT_400.render("B - Bubble Sort || S - Stable Selection Sort || I - Insertion Sort"
                                        "", 1, self.BLACK)
        controls2 = self.FONT_400.render(f"R - New Random List || T - Toggle "
                                         f"{'Descending' if ascending else 'Ascending'} Order", 1, self.BLACK)
        self.WIN.blit(title, (0, y - 20))
        self.WIN.blit(controls, (0, y + 20))
        self.WIN.blit(controls2, (0, y + 50))

    def draw_list(self, colors={}, bg_error=True):
        lst = self.lst
        block_width = self.block_width
        block_height = self.block_height
        pygame.draw.rect(self.WIN, self.WHITE, self.sort_WIN)

        for i, value in enumerate(lst):
            x = self.block_x + i * block_width
            y = self.height - (2 + value - self.lst_min) * block_height
            block_color = self.GREY_GRADIENTS[i % 3]

            if i in colors:
                block_color = colors[i]

            pygame.draw.rect(self.WIN, block_color, (x, y, block_width, self.height))

        pygame.display.update()

    def new_ran_list(self, rand_range):
        self.lst = [random.randrange(1, rand_range) for i in range(len(self.lst))]
        print(self.lst)
        self.draw_list()

    def check_lst(self, lst):
        if lst == sorted(lst):
            return True
        else:
            return False

    def bubble_sort(self, ascending):
        lst = self.lst
        for i in range(len(lst)):
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j + 1] and ascending:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    self.draw_controls(ascending)
                    self.draw_list({j: self.BLUE, j + 1: self.GREEN})
                    yield True
                elif lst[j] < lst[j + 1] and not ascending:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    self.draw_controls(ascending)
                    self.draw_list({j: self.BLUE, j + 1: self.GREEN})
                    yield True
        self.draw_list()
        return self.lst

    def select_sort(self, ascending, base=0):
        lst = self.lst
        for i in range(len(lst)):
            clock.tick(FPS)
            i = base
            for j in range(i + 1, len(lst)):
                clock.tick(FPS)
                try:
                    if ascending:
                        target = min(lst[i + 1:]) if min(lst[i + 1:]) < lst[i] else lst[i]
                    else:
                        target = max(lst[i + 1:]) if max(lst[i + 1:]) > lst[i] else lst[i]
                except ValueError:
                    break
                self.draw_list({i: self.BLUE, j: self.GREEN})
                if lst[j] == target:
                    save = lst[j]
                    time.sleep(0.2)
                    self.draw_list({i: self.BLUE, j: self.RED})
                    time.sleep(0.2)
                    for k in reversed(range(i, j)):
                        clock.tick(FPS)
                        lst[k + 1] = lst[k]
                        self.draw_controls(ascending)
                        self.draw_list({i: self.BLUE, j: self.GREEN, k + 1: self.RED})
                    lst[i] = save
                    self.draw_list({i: self.GREEN, j: self.BLUE})
                    base += 1
                    j += 1
                    break
                elif lst[i] == target:
                    i += 1
                    self.draw_list({i: self.BLUE})
                    continue
            self.draw_list()
            if self.check_lst(lst):
                break
            yield base
        self.draw_list()
        return self.lst

    def insertion_sort(self, ascending):
        lst = self.lst
        while not self.check_lst(lst):
            for i in range(len(lst)):
                clock.tick(FPS)
                self.draw_list({i: self.BLUE, i + 1: self.GREEN})
                try:
                    if lst[i + 1] < lst[i] and ascending:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        self.draw_controls(ascending)
                        self.draw_list({i: self.GREEN, i + 1: self.BLUE})
                        yield True
                    elif lst[i + 1] > lst[i] and not ascending:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        self.draw_controls(ascending)
                        self.draw_list({i: self.GREEN, i + 1: self.BLUE})
                        yield True
                except IndexError:
                    print('NException')
        self.draw_list()


def check_sort_state(d, sort_states, ascending, b):
    if sort_states["sorting"] and sort_states["bubble_sort"]:
        try:
            next(d.bubble_sort(ascending))

        except StopIteration:
            print("Exception")
            sort_states["sorting"] = False
            sort_states["bubble_sort"] = False

    if sort_states["sorting"] and sort_states["select_sort"]:
        try:
            base = next(d.select_sort(ascending, b))
            return base
        except StopIteration:
            print('Exception')
            sort_states['sorting'] = False
            sort_states['select_sort'] = False

    if sort_states["sorting"] and sort_states["insertion_sort"]:
        try:
            next(d.insertion_sort(ascending))
        except StopIteration:
            print('Exception')
            sort_states['sorting'] = False
            sort_states['insertion_sort'] = False


def generate_list(size, rand_range):
    lst = [random.randrange(1, rand_range) for i in range(size)]
    return lst


def main():
    base = 0
    run = True
    ascending = True
    sort_states = {
        'sorting': False,
        'bubble_sort': False,
        'select_sort': False,
        'insertion_sort': False,
    }
    lst = generate_list(lst_size, rand_range)
    # lst = [9, 27, 44, 1, 7, 6, 1, 36, 24, 7]
    d = DrawDetails(lst, WIDTH, HEIGHT)
    while run:
        clock.tick(FPS)
        base = check_sort_state(d, sort_states, ascending, base)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_b:
                sort_states["bubble_sort"] = True
                sort_states["select_sort"] = False
                sort_states["insertion_sort"] = False
                sort_states["sorting"] = True
                d.bubble_sort(ascending)

            if event.key == pygame.K_s:
                sort_states["select_sort"] = True
                sort_states["bubble_sort"] = False
                sort_states["insertion_sort"] = False
                sort_states["sorting"] = True
                base = 0
                d.select_sort(ascending)

            if event.key == pygame.K_i:
                sort_states["insertion_sort"] = True
                sort_states["select_sort"] = False
                sort_states["bubble_sort"] = False
                sort_states["sorting"] = True
                d.insertion_sort(ascending)

            if event.key == pygame.K_r:
                d.draw_controls(ascending)
                d.new_ran_list(rand_range)
                sort_states["sorting"] = False
            if event.key == pygame.K_t:
                if ascending:
                    ascending = False
                    base = 0
                else:
                    ascending = True
                    base = 0
                d.draw_controls(ascending)

    pygame.quit()

    pass


if __name__ == '__main__':
    main()
