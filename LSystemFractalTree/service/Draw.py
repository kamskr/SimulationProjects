import turtle
import random
import os

class Draw:
    def __init__(self, instruction: str):
        print(os.getcwd())
        print(os.listdir())
        self.window = turtle.Screen()
        self.window.bgcolor("#f5eae1")
        self.window.title("Fractal Tree")
        self.robot = turtle.Turtle()
        self.stack = []
        self.distance = 5
        self.instruction = instruction

    def drawTree(self):
        self.robot.hideturtle()
        self.robot.penup()
        self.robot.setpos(0, -self.window.window_height()/2)
        self.robot.showturtle()
        self.robot.left(90)
        self.robot.pendown()
        self.robot.speed(0)
    
        print(self.instruction)
        for move in self.instruction:
            print(move)
            if move == "F":
                self.robot.pencolor("brown")
                self.robot.forward(self.distance)
            elif move == "+":
                self.robot.left(random.randint(15,35))
            elif move == "-":
                self.robot.right(random.randint(15,35))   
            elif move == "[":
                self.stack.append((self.robot.heading(), self.robot.pos()))
            elif move == "]":
                heading, position = self.stack.pop()
                self.robot.pencolor("#ffb5f9")
                self.robot.dot()
                self.robot.penup()
                self.robot.goto(position)
                self.robot.setheading(heading)
                self.robot.pendown()
        turtle.done()






    



# v = "[", "]", "X"] #Forward, left, right, push, pop, x is not a command - robot will ignore it, but it will help to generate next program based on the previous one

# robot = {
#     'x': 0,
#     'y' : 0,
#     'a' : random(15,35)
# }