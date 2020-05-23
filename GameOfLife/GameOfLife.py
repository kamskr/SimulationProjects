import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[random.choice([0, 1]) for x in range(columns)] for y in range(rows)]

    def go_to_next_generation(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print()

    def calculate_alive_neighbours(self, i, j):
        if self.grid[i][j] == 0:
            return False
            alive_neighbours = 0

        if i != 0 and i != (len(self.grid) - 1) and j != 0 and j != (len(self.grid[i]) - 1):
            neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                                      for y2 in range(y - 1, y + 2)
                                      if (-1 < x <= self.columns and
                                          -1 < y <= self.rows and
                                          (x != x2 or y != y2) and
                                          (0 <= x2 <= self.columns) and
                                          (0 <= y2 <= self.rows))]

            alive_neighbours += self.grid[i - 1][j]
            alive_neighbours += self.grid[i - 1][j + 1]
            alive_neighbours += self.grid[i][j + 1]
            alive_neighbours += self.grid[i + 1][j + 1]
            alive_neighbours += self.grid[i + 1][j]
            alive_neighbours += self.grid[i + 1][j - 1]
            alive_neighbours += self.grid[i][j - 1]
            alive_neighbours += self.grid[i - 1][j - 1]
        elif i != 0 and j != 0 and j != (len(self.grid[i]) - 1):
            alive_neighbours += self.grid[len(grid) - 1][j]
            alive_neighbours += self.grid[len(grid) - 1][j + 1]
            alive_neighbours += self.grid[i][j + 1]
            alive_neighbours += self.grid[i + 1][j + 1]
            alive_neighbours += self.grid[i + 1][j]
            alive_neighbours += self.grid[i + 1][j - 1]
            alive_neighbours += self.grid[i][j - 1]
            alive_neighbours += self.self.grid[len(grid) - 1][j - 1]
