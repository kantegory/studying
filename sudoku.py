def read_sudoku(filename):
    """ ��������� ������ �� ���������� ����� """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """����� ������ """
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
    """ ���������� ��� �������� ��� ������ ������, ��������� � pos

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
    """ ���������� ��� �������� ��� ������ �������, ���������� � pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    pass


def get_block(values, pos):
    """ ���������� ��� �������� �� ��������, � ������� �������� ������� pos """
    pass


def find_empty_positions(grid):
    """ ����� ������ ��������� ������� � �����

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    pass


def find_possible_values(grid, pos):
    """ ������� ��� ��������� �������� ��� ��������� ������� """
    pass


def solve(grid):
    """ ������� �����, ��������� � grid """
    """ ��� ������ ������?
        1. ����� ��������� �������
        2. ����� ��� ��������� ��������, ������� ����� ���������� �� ���� �������
        3. ��� ������� ���������� ��������:
            3.1. ��������� ��� �������� �� ��� �������
            3.2. ���������� ������ ���������� ����� �����
    """
    pass


def check_solution(solution):
    """ ���� ������� solution �����, �� ������� True, � ��������� ������ False """
    pass


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)