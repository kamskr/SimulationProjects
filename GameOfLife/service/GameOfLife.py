import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[random.choice([0, 1]) for x in range(columns)] for y in range(rows)]
        self.neighbours = self.create_neighbour_dict()

    def go_to_next_generation(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print()

    def create_neighbour_dict(self):
        neighbours_dict = dict()
        for row in range(self.rows):
            for column in range(self.columns):
                neighbours = []
                x = -1
                for _ in range(3):
                    y = -1
                    for _ in range(3):
                        if x == 0 and y == 0:
                            y += 1
                            continue
                        neighbour_i = row + x
                        neighbour_j = column + y
                        if neighbour_i == -1:
                            neighbour_i = self.rows - 1
                        if neighbour_i == self.rows:
                            neighbour_i = 0
                        if neighbour_j == -1:
                            neighbour_j = self.columns - 1
                        if neighbour_j == self.columns:
                            neighbour_j = 0
                        y += 1
                        neighbours.append((neighbour_i, neighbour_j))
                    x += 1
                neighbours_dict[(row, column)] = neighbours
        return neighbours_dict

