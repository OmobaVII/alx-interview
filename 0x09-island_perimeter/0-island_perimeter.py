#!/usr/bin/python3
""" Provides a function island_perimeter that returns
    the perimeter of the island described in grid:

    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
        The grid is completely surrounded by water
        There is only one island (or nothing).
        The island doesn’t have “lakes”
        (water inside that isn’t connected to the water surrounding island).
"""


def island_perimeter(grid):
    """ returns the perimeter of the island in the grid
    """

    # keeps track of the perimeter
    perimeter = 0

    # Interates each row of the grid
    for row in range(len(grid)):
        # interates each column of the grid
        for col in range(len(grid[0])):

            # checks if the current position is  land
            if grid[row][col] == 1:
                perimeter += 4

                # checks if the position by the left is land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                # checks if the position by the right is land
                if col < (len(grid[0]) - 1) and grid[row][col + 1] == 1:
                    perimeter -= 1

                # checks if the position on the top is land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                # checks if the position below is land
                if row < (len(grid) - 1) and grid[row + 1][col] == 1:
                    perimeter -= 1
    return perimeter
