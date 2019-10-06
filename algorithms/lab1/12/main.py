def ranking_queens(col, solution, width):
    if len(solution) == width:
        print(solution)
    else:
        for row in range(width):
            if save_queen(row, col, solution):
                ranking_queens(col + 1, solution + [row], width)

def save_queen(upd_row, upd_col, solution):
    for col in range(len(solution)):
        if solution[col] == upd_row or abs(col - upd_col) == abs(solution[col] - upd_row):
            return 0
    return 1


if __name__ == "__main__":

    field = int(input("Введите ширину поля:\n"))
    for n in range(field):
        ranking_queens(1, [n], field)
