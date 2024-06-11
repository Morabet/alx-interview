#!/usr/bin/python3
""" Island Perimeter"""


def island_perimeter(grid):
    """ calculate the perimeter of the island"""
    n = len(grid)
    perimeter = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if j > n and grid[i][j + 1] == 0:
                    perimeter += 1
                if j > 0 and grid[i][j - 1] == 0:
                    perimeter += 1
                if i > n and grid[i + 1][j] == 0:
                    perimeter += 1
                if i > 0 and grid[i - 1][j] == 0:
                    perimeter += 1
    return perimeter

