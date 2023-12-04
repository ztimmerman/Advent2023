with open("day4.txt",'r') as f:
    lines = [x for x in f.readlines() if len(x) > 0]

#Part 1

def getWinningNumbers(line):
    return [int(x) for x in line.split(":")[1].split("|")[0].split(" ") if len(x) > 0]

def getMyNumbers(line):
    return [int(x) for x in line.split(":")[1].split("|")[1].split(" ") if len(x) > 0]

pointsSum = 0
for line in lines:
    winningNumbers = getWinningNumbers(line)
    myNumbers = getMyNumbers(line)
    myWinningPower = len([x for x in myNumbers if x in winningNumbers])
    if myWinningPower > 0:
        pointsSum += 2 ** (myWinningPower - 1)
print("points:",pointsSum)

#Part 2
scratchCardPile = dict()
#Initial Population
for line in lines:
    cardNumber = int(line.split(":")[0].split(" ")[-1])
    myWinningScore = len([x for x in getMyNumbers(line) if x in getWinningNumbers(line)])
    scratchCardPile[cardNumber] = [myWinningScore,1]

for k in scratchCardPile:
    print(k,scratchCardPile)
    for x in range(k+1,k+1+scratchCardPile[k][0]):
        scratchCardPile[x][1] += scratchCardPile[k][1]

print("scratchCards:",sum(scratchCardPile[x][1] for x in scratchCardPile))