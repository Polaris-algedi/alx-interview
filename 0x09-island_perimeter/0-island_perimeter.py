#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (list of list of int): A 2D list of integers
            representing the island in a grid of water and land

    Returns:
        int: The perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check if left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check if right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check if up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check if down
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
