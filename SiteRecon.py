#array of int need to print second largest

import sys

def maxer(arr):
    largest = -sys.maxsize
    second_largest = -sys.maxsize

    for e in arr:
        if e > largest:
            second_largest = largest
            largest = e
        elif e > second_largest:
            second_largest = e
#array of int +/-  given target, n1+n2 = target

ARR = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]

]

def grid_island(grid,r,c) -> int:
    r = len(grid)
    c = len(grid[0])
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != 1:
                continue
            else:
                count += 1
                grid[i][j] = 0
                expand(grid,i,j)

def expand(grid,r,c):
    if grid[r][c] == 0:
        return
    expand(grid,r-1,c)
    expand(grid,r+1,c)
    expand(grid,)




