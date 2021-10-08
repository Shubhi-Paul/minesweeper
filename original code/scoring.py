def GeneratePlayerMap(n):
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr

def DisplayMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")
    
def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

def CheckContinueGame(score):
    print("Your score: ", score)
    isContinue = input("Do you want to try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True

def Game():

    GameStatus = True
    while GameStatus: 
        minesweeper_map = GenerateMineSweeperMap(n, k)
        player_map = GeneratePlayerMap(n)
        score = 0
        while True:
            if CheckWon(player_map) == False:
                print("Enter your cell you want to open :")
                x = input("X (1 to 5) :")
                y = input("Y (1 to 5) :")
                x = int(x) — 1 # 0 based indexing
                y = int(y) — 1 # 0 based indexing
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over!")
                    DisplayMap(minesweeper_map)
                    GameStatus = CheckContinueGame(score)
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    DisplayMap(player_map)
                    score += 1
 
            else:
                DisplayMap(player_map)
                print("You have Won!")
                GameStatus = CheckContinueGame(score)
                break
