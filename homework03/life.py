import pygame
from pygame.locals import *
import random
from pprint import pprint as pp


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.cgrid = self.cell_list()
        self.speed = speed

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
        gen = 0
        pygame.display.set_caption('Game of Life: {} generation'.format(gen))
        self.screen.fill(pygame.Color('white'))
        self.clist = self.cell_list()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list(self.clist)
            pygame.display.set_caption('Game of Life: {} generation'.format(gen))
            gen += 1
            pygame.display.flip()
            clist2 = self.clist.copy()
            self.clist = self.update_cell_list(clist2)
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        if randomize:
            self.clist = [[random.randrange(0, 2) for x in range(self.width // self.cell_size)] for y in range(self.height // self.cell_size)]
        else:
            self.clist = [[0 for x in range(self.width // self.cell_size)] for y in range(self.height // self.cell_size)]
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if clist[i][j]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, a, b))

    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row, col = cell
        n = self.cell_height - 1
        m = self.cell_width - 1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if not (0 <= i <= n and 0 <= j <= m) or (i == row and j == col):
                    continue
                neighbours.append(self.clist[i][j])
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        y, x = 0, 0
        new_clist = []
        clist = cell_list.copy()
        for i in range(len(cell_list)):
            new_clist.append([])
            for j in range(len(cell_list[i])):
                new_clist[i].append(0)
        for row in cell_list:
            for col in row:
                if (col == 1):
                    if (1 < self.get_neighbours((y, x)).count(1) < 4):
                        new_clist[y][x] = 1
                    else:
                        new_clist[y][x] = 0
                else:
                    if (self.get_neighbours((y, x)).count(1) == 3):
                        new_clist[y][x] = 1
                    else:
                        new_clist[y][x] = 0
                x += 1
            x = 0
            y += 1
        return new_clist


if __name__ == '__main__':
    game = GameOfLife(640, 480, 10)
    game.run()
