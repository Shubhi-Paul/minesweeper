import random


def base_grid(n):

    """create the background grid as the basic str of the game"""

    arr=[[0 for row in range(n)] for column in range(n)]
    
    bomb(arr,n)

def print_grid(arr):

    """prints the grid with bombs and numbers"""

    for row in arr:
        for cell in row:
            print(cell, end = ' ')
            #print('#'.join(str(cell) for cell in row))
        print()
        print()


def bomb(arr,n):

    """add bombs randomly in the grid """
    
    x=random.randint(0,n-1)
    y=random.randint(0,n-1)
    arr[x][y] = "X"
    number(x,y,n,arr)

def number(x,y,n,arr):
    
    """increment numbers around the bomb"""

    if y == 0:
        arr[x][y+1] = +1 #centre right
    elif y == (n-1):
        arr[x][y-1] = +1 #centre left
    elif y > 0 and y < (n-1) :
        arr[x][y+1] = +1 #centre right
        arr[x][y-1] = +1 #centre left

    if x < (n-1) and ( y > 0 and y < (n-1)):
         arr[x+1][y+1] = +1 #bottom right
         arr[x+1][y-1] = +1 #bottom left
         arr[x+1][y] = +1 #bottom centre
    elif  x < (n-1) and y == 0:
        arr[x+1][y+1] = +1 #bottom right
        arr[x+1][y] = +1 #bottom centre
    elif x < (n-1) and y == (n-1):
        arr[x+1][y-1] = +1 #bottom left
        arr[x+1][y] = +1 #bottom centre

    if x > 0 and ( y > 0 and y < (n-1)):
         arr[x-1][y+1] = +1 #top right
         arr[x-1][y-1] = +1 #top left
         arr[x-1][y] = +1 #top centre
    elif  x > 0 and y == 0:
        arr[x-1][y+1] = +1 #top right
        arr[x-1][y] = +1 #top centre
    elif x > 0 and y == (n-1):
        arr[x-1][y-1] = +1 #top left
        arr[x-1][y] = +1 #top centre

    
    print_grid(arr)








#__main__


base_grid(5)

input("press any key... ")
