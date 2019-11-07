class Board(object):

    def __init__(self, size):
        self.size = size
        self.board = [['-' for i in range(self.size)] for i in range(self.size)]

    def print_board(self):
        print("  ", end="")
        for i in range(self.size):
            print(i,end="  ")
        print()

        for i in range(self.size):
            print(i,end=" ")

            for j in range(self.size):
                print(self.board[i][j], end = "  ")
            print()

    #insere Raina 
    def place_queen(self, row, column):
        self.board[row][column] = 'Q'
        return board

    #remove raina
    def remove_queen(self, row, column):
        self.board[row][column] = '-'
        return board
    
    #checa posião
    def check_queen(self, row, column):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'Q':
                    if ((i == row) or
                        (j == column) or
                        (i - j == row - column) or
                        (i + j == row + column)):
                        return False
        return True
                            
    #returna soluao
    def nQueens(self, column = 0):
        if column >= self.size:
            self.print_board()
            return True
        else:
            for rows in range(self.size):
                if self.check_queen(rows, column): 
                    self.place_queen(rows, column)

                    solution = self.nQueens(column + 1)

                    if solution:
                        return True

                    self.remove_queen(rows, column)

            return False
    
board = Board(8)

board.nQueens()