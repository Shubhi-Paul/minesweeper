from random import randint

#base_structure_start___________________________________________________________________________________

def base_grid(n):

    """create the background grid as the basic str of the game"""

    arr=[[0 for row in range(n)] for column in range(n)]
    
    add_bombs(arr,n)
    

def print_grid(arr):

    """prints the grid with bombs and numbers"""

    for row in arr:
        for cell in row:
            if cell == 0:
                print("." , end = "  ")
            else:
                print(cell, end = '  ')
        print()
        

def add_bombs(arr,n, k = 9):

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
                arr[row][column] = "X"
                number(row,column,n,arr)

    print_grid(arr)       

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


#__main__

base_grid(25)

input("press any key... ")
