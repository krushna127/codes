# Code-A5: N-Queens using Backtracking
# First queen position uses zero-based row and column indices.

def is_safe(board, row, col, n):
    for r in range(row):
        if board[r][col] == 1:
            return False
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1
    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def solve_n_queens(board, row, n, fixed_row, fixed_col, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return

    if row == fixed_row:
        # Keep the user-specified queen in its fixed position.
        if is_safe(board, row, fixed_col, n):
            board[row][fixed_col] = 1
            solve_n_queens(board, row + 1, n, fixed_row, fixed_col, solutions)
            board[row][fixed_col] = 0
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, fixed_row, fixed_col, solutions)
            board[row][col] = 0

def main():
    try:
        n = int(input("Enter size of board (N): "))
        if n <= 0:
            print("N must be a positive integer.")
            return
        fixed_row, fixed_col = map(
            int, input("Enter position of first queen (row and column index starting from 0): ").split()
        )
        if not (0 <= fixed_row < n and 0 <= fixed_col < n):
            print("Queen position must be within the board.")
            return

        board = [[0] * n for _ in range(n)]
        solutions = []
        solve_n_queens(board, 0, n, fixed_row, fixed_col, solutions)

        print("\nAll possible solutions:")
        if not solutions:
            print("No solution exists for the given first-queen position.")
        else:
            for solution in solutions:
                print_board(solution)

        print("Time Complexity: O(N!) in the worst case")
        print("Space Complexity: O(N^2) for the board, excluding stored solutions")
    except ValueError:
        print("Invalid input. Enter integers in the requested format.")

if __name__ == "__main__":
    main()
