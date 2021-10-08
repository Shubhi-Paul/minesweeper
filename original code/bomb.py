import random
def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    x = random.randint(0,4)
    y = random.randint(0,4)
    arr[y][x] = 'X'
    if (x >= 1 and x <= 3):
        arr[y][x+1] += 1 # center right
        arr[y][x-1] += 1 # center left
    elif (x == 0):
        arr[y][x+1] += 1 # center right
    elif (x == 4):
        arr[y][x-1] += 1 # center left

    if (x >= 1 and x <= 4) and (y >= 1 and y <= 4):
        arr[y-1][x-1] += 1 # top left
    elif (x >= 0 and x <= 3) and (y >= 1 and y <= 4):
        arr[y-1][x+1] += 1 # top right
    elif (x >= 0 and x <= 4) and (y >= 1 and y <= 4):
        arr[y-1][x] += 1 # top center
 
    if (x >=0 and x <= 3) and (y >= 0 and y <= 3):
        arr[y+1][x+1] += 1 # bottom right
    elif (x >= 1 and x <= 4) and (y >= 0 and y <= 3):
        arr[y+1][x-1] += 1 # bottom left
    elif (x >= 0 and x <= 4) and (y >= 0 and y <= 3):
        arr[y+1][x] += 1 # bottom center
    
    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print("")

if __name__ == "__main__":
    minesweeper(5)

input("press any key... ")