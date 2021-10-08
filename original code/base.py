def minesweeper(n):

    """create the background grid as the basic str of the game"""
    
    #def minesweeper(n,m):
    #n=m
    #arr = [[0 for row in range(n)] for column in range(m)]
    #arr=[row1,row2,row3]
    #arr=[[R1_cell1,R1_cell2],[R2_cell1,R2_cell2],[R3_cell1,R3_cell2]]
    #n=2,m=3 then arr=[[0,0],[0,0],[0,0]]
   
    arr = [[0 for row in range(n)] for column in range(n)]
    
    for  in arr:
        print(" ".join(str(cell) for cell in n))
        print()

    '''for row in arr:
        for cell in row:
            print(cell, end = ' ')
        print()
        print()'''


a = int(input("enter number : "))

if __name__ == "__main__":
    minesweeper(a)

input("press any key... ")

