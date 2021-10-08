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

    """add bombs randomly in the grid and update the numbers around it"""
    
    x=random.randint(0,n-1)
    y=random.randint(0,n-1)
    arr[x][y] = "x"
    print_grid(arr)






#__main__


base_grid(5)

input("press any key... ")