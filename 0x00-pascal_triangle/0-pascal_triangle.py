#!/usr/bin/python3
'''Pascal triangle module'''


def pascal_triangle(n):
    '''
    create and  list of lists of integers
    representing the Pascal’s triangle of n
    '''

    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = []

        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                current_row.append(
                        triangle[row - 1][col] + triangle[row - 1][col - 1]
                        )

        triangle.append(current_row)

    return triangle
