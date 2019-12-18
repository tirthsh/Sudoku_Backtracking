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
    board = 
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
