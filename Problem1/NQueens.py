class NQueens:

    def __init__(self, n):
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]

    def is_safe(self, row, col):

        # Same column
        for i in range(row):
            if self.board[i][col] == "Q":
                return False

        # Upper-left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False

            i -= 1
            j -= 1

        # Upper-right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < self.n:
            if self.board[i][j] == "Q":
                return False

            i -= 1
            j += 1

        return True

    def solve(self, row):

        # Base case
        if row == self.n:
            self.print_board()
            return True

        # Try every column
        for col in range(self.n):

            if self.is_safe(row, col):

                # Choose
                self.board[row][col] = "Q"

                # Explore
                if self.solve(row + 1):
                    return True

                # Undo / Backtrack
                self.board[row][col] = "."

        return False

    def print_board(self):

        for row in self.board:
            print(" ".join(row))


n = int(input("Enter N: "))

queens = NQueens(n)

if not queens.solve(0):
    print("No solution exists!")