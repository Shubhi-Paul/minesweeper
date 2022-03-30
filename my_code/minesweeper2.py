# open multiple cells which a cell with 0 value is clicked
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
                print(cell, end = "  ")
               
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

#open_empty_cells_together____________________________________________________________________________
def display_null(x,y,n,mine_map,player_map,score):
    mine_map[x][y] = " "
    if x>0 :
        if mine_map[x-1][y] == 0:
            player_map[x-1][y]=mine_map[x-1][y]
            score +=1
            display_null(x-1,y,n,mine_map,player_map,score) #left
            score += 1
        elif mine_map[x-1][y] != " ":
            player_map[x-1][y]=mine_map[x-1][y]
            score += 1
    
    if x> 0 and y>0:
        if mine_map[x-1][y-1] == 0:
            player_map[x-1][y-1]=mine_map[x-1][y-1]
            score +=1        
            display_null(x-1,y-1,n,mine_map,player_map,score) #top left
        elif mine_map[x-1][y-1] != " ":
            player_map[x-1][y-1]=mine_map[x-1][y-1]
            score += 1
    
    if x > 0 and y < n-1:
        if mine_map[x-1][y+1] == 0:
            player_map[x-1][y+1]=mine_map[x-1][y+1]
            score += 1
            display_null(x-1,y+1,n,mine_map,player_map,score) #bottom left
        if mine_map[x-1][y+1] != " ":
            player_map[x-1][y+1]=mine_map[x-1][y+1]
            score += 1

    if x < n-1 :
        if mine_map[x+1][y] == 0:
            player_map[x+1][y]=mine_map[x+1][y]
            score += 1
            display_null(x+1,y,n,mine_map,player_map,score) #right
        elif mine_map[x+1][y] != " ":
            player_map[x+1][y]=mine_map[x+1][y]
            score += 1
    
    if x < n-1 and y >0:
        if mine_map[x+1][y-1] == 0:
            player_map[x+1][y-1]=mine_map[x+1][y-1]
            score += 1
            display_null(x+1,y-1,n,mine_map,player_map,score) #top right
        elif mine_map[x+1][y-1] != " ":
            player_map[x+1][y-1]=mine_map[x+1][y-1]
            score += 1
    
    if x < n-1 and y < n-1:
        if mine_map[x+1][y+1] == 0:
            player_map[x+1][y+1]=mine_map[x+1][y+1]
            score += 1
            display_null(x+1,y+1,n,mine_map,player_map,score) #bottom right
        elif mine_map[x+1][y+1] != " ":
            player_map[x+1][y+1]=mine_map[x+1][y+1]
            score += 1
    
    if y > 0:
        if mine_map[x][y-1] == 0:
            player_map[x][y-1]=mine_map[x][y-1]
            score += 1
            display_null(x,y-1,n,mine_map,player_map,score) #top
        elif mine_map[x][y-1] != " ":
           player_map[x][y-1]=mine_map[x][y-1]
           score += 1
    
    if y < n-1:
        if mine_map[x][y+1] == 0:
            player_map[x][y+1]=mine_map[x][y+1]
            score += 1
            display_null(x,y+1,n,mine_map,player_map,score) #bottom
        elif mine_map[x][y+1] != " ":
           player_map[x][y+1]=mine_map[x][y+1]
           score += 1
    
    
    return player_map , score

#game_start___________________________________________________________________________________________
def player_grid(n):
     map=[["-" for row in range(n)] for column in range(n)]
     return map

def cont_game(n,score):
    print('your score is :', score,"/", n*n,'!!')
    again = input("\n\nWant to play again (y/n) ? : ")
    if again == 'n':
        input('\nPress any key to exit....')
        return False
    else:
        os.system("cls")
        return True

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
        print_grid(player_map)
        while True:
            if check_won(n,player_map)==False:
                print('Enter the cell u want to open :' )
                print ("Enter value X and Y (1 to",n,")")
                x = int(input("X : "))
                x -= 1
                y = int(input("Y : "))
                y -= 1
                if mine_map[x][y] == "X":
                    os.system("cls")
                    print("Game Over :(")
                    print_grid(mine_map)
                    Game_status = cont_game(n,score)
                    break
                
                elif mine_map[x][y] == 0: #ITS NOT '0' STUPID BITCH!!
                    player_map[x][y] = mine_map[x][y]
                    player_map , score = display_null(x,y,n,mine_map,player_map,score)
                    os.system("cls")
                    print_grid(player_map)
                   
                else:
                    os.system("cls")
                    print(mine_map[x][y])
                    player_map[x][y] = mine_map[x][y]
                    score += 1
                    print_grid(player_map)
            else:
                os.system("cls")
                print_grid(player_map)
                print("\nYou have Won!!")
                GameStatus =  cont_game(n,score)
                break
        

def grid_size():
    print("GRID SIZE AVAILABE \n1. 10x10 \n2. 15x15")
    grid= int(input('\nChoose grid size (1/2) : '))
    if grid == 1:
        n = 10
    elif grid == 2:
        n = 15
    else:
        print('Choosen option unavailable. TIP: CHOOSE CORRECTLY !')
        grid_size()
    return n

def difficulty():
    print("DIFICULTY LEVELS AVAILABLE \n1. Easy \n2. Medium \n3. Hard \n4. Very Hard")
    diff= int(input('\nChoose grid size (1/2/3/4) : '))
    if diff == 1:
        k = 10
    elif diff == 2:
        k = 15
    elif diff == 3:
        k = 20
    elif diff == 4:
        k = 25
    else:
        print('Choosen option unavailable. TIP: CHOOSE CORRECTLY !')
        difficulty()
    return k
        
#__main__

# Start of Program
if __name__ == "__main__":
    try:
        print("\t\tWELCOME TO MINESWEEPER :)\n")
        n = grid_size()
        print()
        k = difficulty()
        os.system("cls")
        game(n,k) #game(matrix,difficulty)
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
