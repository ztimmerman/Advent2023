
symbolSet = {'*', '=', '-', '&', '+', '#', '/', '@', '%', '$'}
grid = []

def hasAdjacentSymbol(posX,posY):
    global symbolSet, grid
    if posX == 0:
        xMinusOne = 0
    else:
        xMinusOne = posX - 1
    if posY == 0:
        yMinusOne = 0
    else:
        yMinusOne = y - 1
    miniGrid = [x[xMinusOne:posX+2] for x in grid[yMinusOne:posY+2]]
    print(miniGrid)
    for line in miniGrid:
        for c in line:
            if c in symbolSet:
                return True
    return False


with open("day3.txt",'r') as f:
    for line in f.readlines():
        grid.append([x for x in line])

#Bad hack to ensure that the last line has a newline so that the currentNumber will always be resolved.
grid[-1].append('\n')

numberSum = 0
for y in range(len(grid)):
    print(grid[y])
    currentNumber = 0
    numberHasAdjacentSymbol = False
    for x in range(len(grid[y])):
        if grid[y][x].isdigit():
            currentNumber = currentNumber * 10 + int(grid[y][x])
            if numberHasAdjacentSymbol == False and hasAdjacentSymbol(x,y):
                numberHasAdjacentSymbol = True
        else:
            if numberHasAdjacentSymbol:
                print(currentNumber)
                numberSum += currentNumber
            currentNumber = 0
            numberHasAdjacentSymbol = False

print("sum: ",numberSum)
