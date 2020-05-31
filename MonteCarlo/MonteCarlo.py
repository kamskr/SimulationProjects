import numpy as np
import matplotlib.pyplot as plt


size = 1000000
randomX = np.random.uniform(0.0, np.pi, size)
randomY = np.random.uniform(0.0, 1.0, size)

insideSin = 0
for x, y in zip(randomX, randomY):
    if np.sin(x) >= y:
        insideSin += 1



print(np.pi * insideSin / size)