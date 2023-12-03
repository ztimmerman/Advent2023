from collections import defaultdict

class gridNumber:
    def __init__(self,val,startX,endX,posY):
        self.val = val
        self.startX = startX
        self.endX = endX
        self.posY = posY

    def isAdjacent(self,x,y):
        if abs(self.posY-y) > 1:
            return False
        if x not in range(self.startX -1,self.endX +2):
            return False
        return True

    def __str__(self) -> str:
        return  f"{self.val} -> ({self.startX}:{self.endX},{self.posY})" 

grid = []
fileName = "day3.txt"

with open(fileName,'r') as f:
    for line in f.readlines():
        grid.append(list(line))

numbersList = []
currentNumber = 0
startX = 0
endX = 0
posY = 0
numberScan = False
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x].isdigit():
            if numberScan == False:
                numberScan = True
                startX = x
                endX = x
                posY = y
                currentNumber = int(grid[y][x])
            else:
                endX = x
                currentNumber = currentNumber * 10 + int(grid[y][x])
        else:
            if numberScan:
                numberScan = False
                numbersList.append(gridNumber(currentNumber,startX,endX,posY))
[print(str(x)) for x in numbersList]

starDict = defaultdict(list)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '*':
            starDict[(x,y)] = [n.val for n in filter(lambda n: n.isAdjacent(x,y),numbersList)]

numberSum = 0
for x in starDict.keys():
    if len(starDict[x]) == 2:
        numberSum += starDict[x][0] * starDict[x][1]
print(numberSum)