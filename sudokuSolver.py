#this method valdiates the board, in other words whether the new number filled in follows the rules of sudoku
# 3 cases
# 1. no same value on the same row
# 2. no same value on the same col
# 3. no same value in the same board
def validateBoard(board, num, pos):
    #check row
    for row in range(len(board[0])):
        if board[pos[0]][row] == num and pos[1] != row:
            return False

    #check col
    for col in range(len(board)):
        if board[col][pos[1]] == num and pos[0] != col:
            return False

    #check square
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for row in range(boxY * 3, boxY * 3 + 3):
        for col in range(boxX * 3, boxX * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False

#this method finds the next empty space, in other words the next 0 which needs to be filled in
#returns a tuple of (row, col) coordinate of the 0 found, returns None if no 0s found (i.e. board is filled)
def findNextEmptySpace(board):
    for row in range (len(board)):
        for col in range (len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    return None

def printBoard(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            #after every 3 rows, print a line to help outline each box in the board
            print("- - - - - - - - - - -")

        for col in range(len(board[0])):
             #after every 3 columns, print a straight line to help outline each box in the board
            if col % 3 == 0 and col != 0:
                print("| ", end="")
                
            #for spacing
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")



if __name__ == "__main__":
    #sample board
    #0 represents blank space in which the solver will fill by backtracking
    board = \
    [
      [7,8,0,4,0,0,1,2,0],
      [6,0,0,0,7,5,0,0,9],
      [0,0,0,6,0,1,0,7,8],
      [0,0,7,0,4,0,2,6,0],
      [0,0,1,0,5,0,9,3,0],
      [9,0,4,0,6,0,0,0,5],
      [0,7,0,3,0,0,0,1,2],
      [1,2,0,0,0,7,4,0,0],
      [0,4,9,2,0,6,0,0,7]
    ]

    printBoard(board)
