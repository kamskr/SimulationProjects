from service.LSystem import LSystem
from service.Draw import Draw

lSystem = LSystem()
lSystem.iterate(6)
draw = Draw(lSystem.function)
draw.drawTree()
print(lSystem.function)