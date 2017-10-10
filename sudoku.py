import time
import random


def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return print([values[n*i:n*i+n] for i in range(n)])


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos
    return values[row]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    return [values[i][col] for i in range(0, len(values))]


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    row, col = pos
    blockValues = []
    enRow = row // 3 * 3
    enCol = col // 3 * 3
    for i in range(enRow, enRow + 3):
        for j in range(enCol, enCol + 3):
            blockValues.append(values[i][j])
    return blockValues


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if values[i][j] == '.':
                return (i, j)
    return (-1, -1)


def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    posValues = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    posCol = set(get_col(grid, pos))
    posRow = set(get_row(grid, pos))
    posGetBlock = get_block(grid, pos)
    posValues -= posCol
    posValues -= posRow
    for i in range(3):
        posValues -= set(posGetBlock[i])
    return posValues


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    emptyPosValue = find_empty_positions(grid)
    if emptyPosValue == (-1, -1):
        return grid
    posValues = find_possible_values(grid, emptyPosValue)
    if not len(posValues):
        return
    col, row = posValues
    for i in range(len(posValues)):
        grid[col][row] = i
        solSud = solve(grid)
        grid[col][row] = '.'
        if solSud != -1:
            return grid
    return -1


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for i in range(9):
        correct = {1, 2, 3, 4, 5, 6, 7, 8, 9. '.'}
        if correct - set(get_row(solution, (i, 0))) != {'.'}:
            return False
        correct = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        if correct - set(get_col(solution, (0, i))) != {'.'}:
            return False
    for i in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6)):
        correct = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        for n in get_block(solution, i):
            correct -= set(n)
        if correct != {'.'}:
            return False
    return True

def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    40
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    N -= 81
    grid = [['.' for i in range(9)] for i in range(9)]
    grid = solve(grid)
    emptyElem = [(i, j) for i in range(9) for j in range(9)]
    for k in range(N):
        remElem = random.choice(emptyElem)
        emptyElem.remove(remElem)
        grid[remElem[0]][remElem[1]] = '.'
    return grid


if __name__ == '__main__':
    for fname in ('puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt'):
        grid = read_sudoku(fname)
        start = time.time()
        solve(grid)
        end = time.time()
        print(fname + ": " + str(end - start))
