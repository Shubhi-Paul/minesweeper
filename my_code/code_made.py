def base_grid(n):
    arr=[[0 for row in range(n)] for column in range(n)]

    for row in arr:
        for cell in row:
            print(cell, end = ' ')
            #print('#'.join(str(cell) for cell in row))
        print()
        print()

base_grid(5)
input("press any key... ")