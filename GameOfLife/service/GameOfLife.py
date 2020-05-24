import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) for x in range(columns)] for y in range(rows)]
        self.neighbours = self.create_neighbour_dict()
        self.fig, self.ax = plt.subplots()
        self.mat = self.ax.matshow(self.grid)

    def go_to_next_generation(self, img):
        new_grid = self.grid
        for row in range(self.rows):
            for column in range(self.columns):
                alive_neighbours = self.calculate_alive_neighbours(row, column)
                if self.grid[row][column] == 1 and (alive_neighbours == 2 or alive_neighbours == 3):
                    continue
                elif self.grid[row][column] == 0 and alive_neighbours == 3:
                    new_grid[row][column] = 1
                else:
                    new_grid[row][column] = 0

        self.grid = new_grid
        self.mat.set_data(new_grid)
        return self.mat

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

    def calculate_alive_neighbours(self, row, column):
        alive_neighbours = 0
        list_of_neighbours = self.neighbours[(row, column)]
        for neighbour in list_of_neighbours:
            x, y = neighbour
            alive_neighbours += self.grid[x][y]

        return alive_neighbours

    def plot_game(self, time_interval):
        plt.colorbar(self.mat)
        ani = animation.FuncAnimation(self.fig, self.go_to_next_generation, interval = time_interval, save_count=50)
        plt.show()