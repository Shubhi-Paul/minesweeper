from random import randint
import os

#base_structure_start___________________________________________________________________________________

def base_grid(n,k):

    """create the background grid as the basic str of the game"""

    map=[[0 for row in range(n)] for column in range(n)]
    
    add_bombs(map,n,k)
    return map
    

def print_grid(map):

    """ prints the grids """

    for row in map:
        for cell in row:
            if cell == 0:
                print("." , end = "  ")
            else:
                print(cell, end = '  ')
        print()
        print()
        

def add_bombs(map,n, k = 10):

    """
    add bombs randomly in the grid accoring to percentage.
    05% easy
    10% medium 
    15% hard 
    20% very hard

    """
    for column in range(n):
        for row in range(n):
            if randint(1,100) < k:
                map[row][column] = "X"
                number(row,column,n,map)
       

def number(x,y,n,arr):
    
    """increment numbers around the bomb"""

    if y > 0:
        if arr[x][y-1] != "X":
            arr[x][y-1] += 1 #centre right
    if y < (n-1):
        if arr[x][y+1] != "X":
            arr[x][y+1] += 1 #centre right
   
    if x < (n-1) and  y < (n-1):
        if arr[x+1][y+1] != "X" :
            arr[x+1][y+1] += 1 #bottom right
    if x < (n-1) and y > 0:
        if arr[x+1][y-1] != "X":
            arr[x+1][y-1] += 1 #bottom left 
    if  x < (n-1) :
        if arr[x+1][y] !="X":
            arr[x+1][y] += 1 #bottom centre
   
    if x > 0 and y < (n-1):
        if arr[x-1][y+1] != "X":
            arr[x-1][y+1] += 1 #top right
    if  x > 0 and y > 0:
        if arr[x-1][y-1] != 'X':
            arr[x-1][y-1] += 1 #top left
    if x > 0 :
        if arr[x-1][y] != 'X':
            arr[x-1][y] += 1 #top centre

#base_structure_end___________________________________________________________________________________

#game_start___________________________________________________________________________________________
def player_grid(n):
     map=[["-" for row in range(n)] for column in range(n)]
     return map

def cont_game(n,score):
    print('your score is :', score,"/", n*n,'!!')
    again = input("\n\nWant to play again (y/n) ? : ")
    if again == "y":
        game()
    else:
        input('press any key to quit')

def check_won(n,map):
    for column in range(n):
        for row in range(n):
            if map[row][column] == "-":
                return False
    return True

def game(n,k):
    Game_status = True
    while Game_status:
        mine_map=base_grid(n,k)
        player_map=player_grid(n)
        score = 0
        while True:
            if check_won(n,player_map)==False:
                print('Enter the cell u want to open :' )
                print ("Enter value X (1 to",n,")")
                x = int(input("X :"))
                x -= 1
                print ("Enter value Y (1 to",n,")")
                y = int(input("Y : "))
                y -= 1

                if mine_map[x][y] == "X":
                    os.system("cls")
                    print("Game Over :(")
                    print_grid(mine_map)
                    Game_status = cont_game(n,score)
                    break
                else:
                    player_map[x][y] = mine_map[x][y]
                    score += 1
                    print_grid(player_map)
            else:
                os.system("cls")
                print_grid(player_map)
                print("\nYou have Won!!")
                GameStatus = cont_game(n,score)
                break

#game_end_____________________________________________________________________________________________

#__main__

# Start of Program
if __name__ == "__main__":
    try:
        #ask difficulty
        game(10,10) #game(matrix,difficulty)
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
