from random import *
totalScore = 0


def addShip(board, numShips):

    row = randint(0, len(board) - 1)
    col = randint(0, len(board) - 1)
    # rows = []
    # cols = []
    locations = []
    ship = 0
    while True:
        if locations.count((row,col)) == 0:
            locations.insert(ship, (row,col))
            # rows.append(row)
            # cols.append(col)
            ship += 1
        else:
            row = randint(0, len(board) - 1)
            col = randint(0, len(board) - 1)
        if ship == numShips:
            break
    for x in range(numShips):
        # board[rows[x]][cols[x]] = "S"
        board[locations[x][0]][locations[x][1]] = "S"
    return



def checkSetUpError(size, numShips):
    if  (size < 2 or size > 5):
        return True
    if  numShips > (size**2 - 2) or 0 >= numShips:
        return True
    return False

def checkFireError(board, row, col):
    width = len(board)
    # print(width)
    # print(board[row][col])

    if 0 <= row < width and 0 <= col < width:
        if board[row][col] == "X" or board[row][col] == "O":
            flag = True
        else:
            flag = False
    else:
        flag = True

    return flag

def createBoard(size):
    board = []
    for x in range(size):
        board.append([])
        for y in range(size):
            board[x].append("~")
    return board

def displayBoard(board, round=True):
    softList = []
    for seg in board:
        temp = []
        for item in seg:
            temp.append(item)
        softList.append(temp)
    
    if round == True:
        for row in softList:
            for block in row:
                if block == "S":
                    row.insert(row.index("S"), "~")
                    row.remove("S")
                    
    for row in softList:
        for block in row:
            print(block, end="")
        print()
    print()
    return

def fireShot(board, row, col):
    if board[row][col] == "S":
        board[row][col] = "X"
        flag = True
    else:
        board[row][col] = "O"
        flag = False

    return flag

def playRound(board, numShips):
    hits = 0
    round = 1
    while round <= numShips:
        while True:
            coords = input("Enter a row and column to take a shot (e.g., 2 3): ")
            row, column = coords.split(" ")
            row = int(row)
            column = int(column)
            if checkFireError(board,row,column) == False:
                break
            print("You will need to enter valid coordinates.")
        if fireShot(board,row,column):
            print(f"Shot {round} is a hit!")
            hits += 1
        else:
            print(f"Shot {round} is a miss!")
        round += 1
        displayBoard(board)
    print("End of Round: ")
    displayBoard(board,False)
    return hits

def main():    
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()
