from random import randint

#base_structure_start___________________________________________________________________________________

def base_grid(n):

    """create the background grid as the basic str of the game"""

    map=[[0 for row in range(n)] for column in range(n)]
    
    add_bombs(map,n)
    

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
        

def add_bombs(map,n, k = 9):

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
     print_grid(map)

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
            else:
                return True

def game(n):
    while True:
        mine_map=base_grid(n)
        player_map=player_grid(n)
        score = 0
        while True:
            if check_won(n,player_map)==False:
                print('enter the cell u want to open :' )
                x = int(input("X (1 to",n-1," : "))
                x -= 1
                y = int(input("Y (1 to" , n-1 ,": "))
                y -= 1

                if mine_map[x][y] == "X":
                    cont_game(n,score)
                    break
                else:
                    player_map[x][y] = mine_map[x][y]
                    score += 1
                    print_grid(player_map)
            else:
                DisplayMap(player_map)
                print("You have Won!!")
                GameStatus = cont_game(n,score)
                break

#game_end_____________________________________________________________________________________________

#__main__

# Start of Program
if __name__ == "__main__":
    try:
        game(10)
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
