class CheckersBoard:
    EMPTY = 0
    BLACK = 1
    RED = 2

    def __init__(self):
        # Initialize an 8x8 board with pieces in their initial positions
        self.board = [[CheckersBoard.EMPTY] * 8 for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = CheckersBoard.BLACK
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = CheckersBoard.RED

    def move(self, x1, y1, x2, y2):
        # Check if the move is within bounds
        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False

        # Check if the target square is empty
        if self.board[x2][y2] != CheckersBoard.EMPTY:
            return False

        # Determine the direction of the move based on piece color
        if self.board[x1][y1] == CheckersBoard.BLACK:
            direction = 1  # Black pieces advance down the board
        elif self.board[x1][y1] == CheckersBoard.RED:
            direction = -1  # Red pieces advance up the board
        else:
            return False  # Invalid piece

        # Check if it's a basic move (one square diagonally)
        if abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
            # Move the piece to the target square
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = CheckersBoard.EMPTY
            return True

        # Check if it's a capture move (jumping over an enemy piece)
        if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
            enemy_x = (x1 + x2) // 2
            enemy_y = (y1 + y2) // 2

            # Check if there's an enemy piece to capture
            if self.board[enemy_x][enemy_y] != (3 - self.board[x1][y1]):
                return False

            # Move the piece to the target square and remove the captured piece
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = CheckersBoard.EMPTY
            self.board[enemy_x][enemy_y] = CheckersBoard.EMPTY
            return True

        return False

    def count(self, color):
        # Count the number of pieces of the specified color on the board
        return sum(row.count(color) for row in self.board)

    def display(self):
        # Display the board and its current contents in ASCII art
        for row in self.board:
            print(" ".join(["  " if piece == CheckersBoard.EMPTY else "B " if piece == CheckersBoard.BLACK else "R " for piece in row]))
        print()


# Example usage:
board = CheckersBoard()
board.display()
print(board.move(2, 1, 3, 2))  # Move a black piece diagonally
board.display()
print(board.move(5, 2, 4, 3))  # Move a red piece diagonally
board.display()
print(board.move(3, 2, 5, 4))  # Attempt an invalid move
board.display()
print(board.move(3, 2, 4, 3))  # Capture a red piece
board.display()
print("Black pieces:", board.count(CheckersBoard.BLACK))
print("Red pieces:", board.count(CheckersBoard.RED))
