import numpy as np
import matplotlib.pyplot as plt


size = 1000000
randomX = np.random.uniform(0.0, np.pi, size)
randomY = np.random.uniform(0.0, 1.0, size)
insideX = []
insideY = []
outsideX = []
outsideY = []
insideSin = 0

for x, y in zip(randomX, randomY):
    if np.sin(x) >= y:
        insideSin += 1
        insideX.append(x)
        insideY.append(y)
    else:
        outsideX.append(x)
        outsideY.append(y)

print("Area", str(np.pi * insideSin / size))
plt.scatter(insideX, insideY, color='blue')
plt.scatter(outsideX, outsideY, color='red')
plt.scatter(insideX, np.sin(insideX), color='black')

plt.show()


