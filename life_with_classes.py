import pygame
import random
from pygame.locals import *
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
        self.cell_list()

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_cell_list()
            self.draw_grid()
            self.clist.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self):
        self.clist = CellList(self.cell_width, self.cell_height, True)

    def draw_cell_list(self):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        a = self.cell_size
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.clist[(j, i)].is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'), (j * a, i * a, a, a))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (j * a, i * a, a, a))


class Cell:

    def __init__(self, row, col, state=False):
        self.life = state
        self.row = row
        self.col = col

    def is_alive(self):
        return self.life


class CellList:

    def __init__(self, nrows, ncols, randomize=True):
        self.nrows = nrows
        self.ncols = ncols
        if randomize:
            self.cell_grid = list()
            for i in range(self.nrows):
                self.cell_grid.append(list())
                for j in range(self.ncols):
                    self.cell_grid[-1].append(Cell(i, j, random.randint(0, 1)))
        else:
            self.cell_grid = list()
            for i in range(self.nrows):
                self.cell_grid.append(list())
            for j in range(self.ncols):
                self.cell_grid[-1].append(Cell(i, j))

    def get_neighbours(self, cell):
        neighbours = []
        positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
        for r, c in positions:
            if 0 <= cell[0] + r < self.nrows and 0 <= cell[1] + c < self.ncols:
                neighbours.append(self.cell_grid[cell[0] + r][cell[1] + c].life)
        return neighbours

    def update(self):
        new_clist = deepcopy(self.cell_grid)
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[0])):
                summary = sum(c for c in self.get_neighbours((i, j)))
                if 2 <= summary <= 3 and self.cell_grid[i][j].life:
                    new_clist[i][j].life = 1
                elif summary == 3 and not self.cell_grid[i][j].life:
                    new_clist[i][j].life = 1
                else:
                    new_clist[i][j].life = 0
        self.cell_grid = new_clist

    def __iter__(self):
        self.row_num = 0
        self.col_num = 0
        return self

    def __next__(self):
        if self.row_num == self.nrows:
            raise StopIteration
        cell = self.cell_list[self.row_num][self.col_num]
        self.col_num += 1
        if self.col_num == self.ncols:
            self.col_num = 0
            self.row_num += 1
        return cell

    def __str__(self):
        string = ''
        for i in range(self.nrows):
            for j in range(self.ncols):
                string += str(Cell(i, j).is_alive())
                if len(string) == self.ncols:
                    string += '\n'
        return string

    def __getitem__(self, pos):
        return self.cell_grid[pos[0]][pos[1]]

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            new_grid = [[Cell(i, j, int(value)) for j, value in enumerate(line) if value in '01'] for i, line in enumerate(f)]
        clist_class = cls(len(new_grid), len(new_grid[0]), False)
        clist_class.clist = new_grid
        return clist_class


if __name__ == '__main__':
    game = GameOfLife(640, 480, 10)
    game.run()
