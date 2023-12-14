seeds = []
mappingList = []
sourceFile = "day5.txt"

def generateRangeTuple(line):
    arr = [int(x) for x in line.strip().split(" ") if len(x) > 0]
    #       Source start    Source End       Destination Start
    return (arr[1],         arr[1]+arr[2]-1, arr[0])

def getMappedValue(n,mappingTuple):
    if mappingTuple[0] <= n and n <= mappingTuple[1]:
        return (n - mappingTuple[0]) + mappingTuple[2]
    else:
        return n

def readFile():
    global mappingList,seeds,sourceFile
    f = open(sourceFile,'r')
    lines = [x.strip() for x in f.readlines()]
    seeds = [int(x) for x in lines[0].split(" ")[1:]]
    lines = lines[2:] + [""]
    #List of mapping tuples for the current processing step
    stepList = []
    for line in lines:
        if len(line) == 0:
            mappingList.append(stepList)
        elif line.endswith("map:"):
            stepList = []
        else:
            stepList.append(generateRangeTuple(line))

def findLowestFinalValue(seedsIterable,eList=[]):
    print(seedsIterable)
    for seed in seedsIterable:
        transformedVal = seed
        #print(f"seed: {seed}")
        for stepList in mappingList:
            for mappingTuple in stepList:
                possibleNewValue = getMappedValue(transformedVal,mappingTuple=mappingTuple)
                #print(f"possibleNewValue: {possibleNewValue}")
                if possibleNewValue != transformedVal:
                    transformedVal = possibleNewValue
                    break
            #print(f'transformedVal: {transformedVal}')
        
        if len(eList) == 0:
            eList.append(transformedVal)
        elif eList[0] > transformedVal:
            eList[0] = transformedVal       
        #print()
    return eList

readFile()
#print(mappingList)

print("part1:",findLowestFinalValue(seeds))

# endingList = []
# for x in range(0,len(seeds),2):
#     print(x)
#     endingList += findLowestFinalValue(range(seeds[x],seeds[x]+seeds[x+1]))

# print(endingList)