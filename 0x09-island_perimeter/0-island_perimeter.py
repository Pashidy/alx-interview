#!/usr/bin/python3
"""
Iteration of a fxn that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """The main code"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract 1 for each shared side with adjacent land cells
                if i > 0 and grid[i-1][j] == 1:   # check the cell above
                    perimeter -= 2   # Shared side with the above cell
                if j > 0 and grid[i][j-1] == 1:   # Check cell to the left
                    perimeter -= 2   # Shared side with the left cell

    return perimeter
