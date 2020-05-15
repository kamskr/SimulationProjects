
import random
import turtle


class LSystem:
    def __init__(self):
        self.function = "X"

    def iterate(self, numberOfIterations):
        for _ in range(numberOfIterations):
            self.function = self.function.replace("F", self.rule1())
            self.function = self.function.replace("X", self.rule2())

    def rule1(self):
        return "FF"

    def rule2(self):
        return "F+[[X]-X]-F[-FX]+X"