import os
print(os.getcwd())

numbersDict = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def scanLine(line):
    numberArr = []
    for cursor in range(len(line)):
        if line[cursor].isdigit():
            numberArr.append(int(line[cursor]))
            continue
        for numberText in numbersDict:
            if numberText in line[cursor:cursor+len(numberText)]:
                numberArr.append(numbersDict[numberText])
                break
    return numberArr


            


calibrationSum=0
with open("C:/Users/xploy/Documents/Hobby/Python/Advent2023",'r') as f:
    lines = f.readlines()
for x in range(len(lines)):
    # line = [int(y) for y in lines[x] if y.isdigit()]
    line = scanLine(lines[x])
    if len(line) > 0:
        calibrationSum += line[0] * 10 + line[-1]


#print(lines)
print(calibrationSum)