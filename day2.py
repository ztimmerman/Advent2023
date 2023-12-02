[maxRed, maxGreen, maxBlue] = [12,13,14]
with open("day2.txt",'r') as f:
   lines = f.readlines()
# with open("d2demo.txt",'r') as f:
#     lines = f.readlines()

bagDict = {"red":0,"green":1,"blue":2}
correctGameSum = 0
powerSum = 0

for line in lines:
    bagGuess = [0,0,0]

    [gameLabel,rounds] = line.split(":")
    print([gameLabel,rounds])
    gameNum = int(gameLabel.split(" ")[1])
    print(gameNum)
    rounds = [x.strip() for x in rounds.split(";")]
    print(rounds)
    for round in rounds:
        colorLabels = [x.strip() for x in round.split(",")]
        print(colorLabels)
        for colorLabel in colorLabels:
            colorNum = int(colorLabel.split(" ")[0])
            colorType = bagDict[colorLabel.split(" ")[1].strip()]
            if bagGuess[colorType] < colorNum:
                bagGuess[colorType] = colorNum
    print(bagGuess)

    if bagGuess[0] > maxRed or bagGuess[1] > maxGreen or bagGuess[2] > maxBlue:
        print("Game {} is incorrect".format(gameNum))
    else:
        correctGameSum += gameNum
    powerSum += bagGuess[0] * bagGuess[1] * bagGuess[2]

    print()

print("Sum of correct game IDs: {}".format(correctGameSum))
print("Power sum: {}".format(powerSum))