#!/usr/bin/python3
"""NO Imported Module"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    :return: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Assume 4 sides initially
                perimeter += 4

                # Subtract sides that are shared with other land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
