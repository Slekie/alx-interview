def island_perimeter(grid):
  """
  Calculates the perimeter of an island in a 2D grid

  Args:
    grid: A 2D list of integers representing the grid.

  Returns:
    The perimeter of the island.
  """

  perimeter = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        # Check the four sides of the cell
        perimeter += 4
        if i > 0 and grid[i - 1][j] == 1:
          perimeter -= 2
        if j > 0 and grid[i][j - 1] == 1:
          perimeter -= 2

  return perimeter
