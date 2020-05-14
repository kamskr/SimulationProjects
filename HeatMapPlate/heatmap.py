import numpy as np
import seaborn as sns;
import matplotlib.pylab as plt

temperatures = [200, 50, 150, 100]
columns = 40
rows = 40

heatmapMatrix = [[0 for x in range(columns)] for y in range(rows)] 

i = 0
for row in heatmapMatrix:
    j = 0
    for value in row:
        if i == 0:
            if j != 0 and j != columns - 1:
                heatmapMatrix[i][j] = temperatures[0]
        elif i == rows - 1:
            if j != 0 and j != columns - 1:
                heatmapMatrix[i][j] = temperatures[2]
        elif j == columns - 1: 
            heatmapMatrix[i][j] = temperatures[1]
        elif j == 0: 
            heatmapMatrix[i][j] = temperatures[3]
        j += 1
    i += 1

# zrób dictionary ktorego key będzie wspolrzedne a value to kolumna na którą ma wpierdolić
columnIndexDictionary = {}
unknownValues = [[0 for x in range(columns-2)] for y in range(rows-2)] 
answerArray = []
answerVector = []

for _ in range((columns-2) * (rows-2)):
    answerMatrixRow = []
    for row in unknownValues:
        for _ in row:
            answerMatrixRow.append(0)
            
    answerArray.append(answerMatrixRow)

numberOfAnswers = (columns - 2) * (rows - 2)
counter = 0
i = 1
for row in unknownValues:
    j = 1
    for _ in row:
        columnIndexDictionary[i,j] = counter
        counter += 1
        j += 1

    i += 1


i = 1
iAnswer = 0
counter = 0

for row in unknownValues:
    j = 1
    for value in row:
        answer = 0
        cell = heatmapMatrix[i][j-1]
        answer += cell
        if cell == 0:
            answerArray[counter][columnIndexDictionary.get((i,j-1))] = 1
        
        cell = -4*heatmapMatrix[i][j]
        answer += cell
        if cell == 0:
            answerArray[counter][columnIndexDictionary.get((i,j))] = -4

        cell = heatmapMatrix[i][j+1]
        answer += cell
        if cell == 0:
            answerArray[counter][columnIndexDictionary.get((i,j+1))] = 1
        cell = heatmapMatrix[i-1][j]
        answer += cell
        if cell == 0:
            answerArray[counter][columnIndexDictionary.get((i-1,j))] = 1    
        
        cell = heatmapMatrix[i+1][j]
        answer += cell
        if cell == 0:
            answerArray[counter][columnIndexDictionary.get((i+1,j))] = 1 
        answer = -answer
        answerVector.append(answer)
        j += 1
        counter += 1
    i += 1

# print(answerVector)

result = np.linalg.inv(answerArray).dot(answerVector)

counter = 0
i = 1
for row in unknownValues:
    j = 1
    for value in row:
        heatmapMatrix[i][j] = result[counter] 
        counter += 1
        j += 1
    i += 1

ax = sns.heatmap(heatmapMatrix, cmap="Reds")
plt.show()
