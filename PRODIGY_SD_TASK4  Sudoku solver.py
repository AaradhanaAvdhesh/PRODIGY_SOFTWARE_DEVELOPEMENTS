def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_safe(grid, row, col, num):
    # Check if 'num' is not present in the current row and column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check if 'num' is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(grid):
    row, col = find_empty_location(grid)

    # If there is no empty location, the Sudoku puzzle is solved
    if row is None:
        return True

    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            # Place the number if it's safe
            grid[row][col] = num

            # Recursively solve the rest of the puzzle
            if solve_sudoku(grid):
                return True

            # If placing 'num' leads to an invalid solution, backtrack
            grid[row][col] = 0

    # No valid number found, backtrack
    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_grid(puzzle)
    else:
        print("\nNo solution exists.")
