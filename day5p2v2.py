from collections import deque

seeds = []
mappingList = []
sourceFile = "day5.txt"

def getRangeTupleFromLine(line):
    [destinationRangeStart,sourceRangeStart,rangeLength] = [int(x) for x in line.split(" ")]
    offset = destinationRangeStart - sourceRangeStart
    sourceRangeEnd = sourceRangeStart + rangeLength
    return (sourceRangeStart,sourceRangeEnd,offset)

def readFile():
    global mappingList,seeds,sourceFile
    f = open(sourceFile,'r')
    lines = [x.strip() for x in f.readlines()]
    seedList = [int(x) for x in lines[0].split(":")[1].split(" ") if len(x) > 0]
    for x in range(0,len(seedList),2):
        seeds.append((seedList[x],seedList[x]+seedList[x+1]))
    # print(seedList)
    # print(sorted(seeds))
    seeds.sort()
    lines = lines[2:] + [""]
#List of mapping tuples for the current processing step
    stepList = []
    for line in lines:
        if len(line) == 0:
            mappingList.append(sorted(stepList))
        elif line.endswith("map:"):
            stepList = []
        else:
            stepList.append(getRangeTupleFromLine(line))

def transform(rangeStart,rangeEnd,offset):
    return (rangeStart+offset,rangeEnd+offset)

readFile()
workingDeque = deque(seeds)
for stepList in mappingList:
    newWorkingDeque = deque()
    for stepTuple in stepList:
        stepOffset = stepTuple[2]
        for _ in range(len(workingDeque)):
            workingTuple = workingDeque.popleft()
            #workingTuple overlaps with stepTuple
            if workingTuple[1] >= stepTuple[0] and workingTuple[0] <= stepTuple[1]:
                #total overlap
                if stepTuple[0] <= workingTuple[0] and stepTuple[1] >= workingTuple[1]:
                    newWorkingDeque.append(transform(workingTuple[0],workingTuple[1],stepOffset))
                #left overlap
                elif stepTuple[0] <= workingTuple[0] and stepTuple[1] <= workingTuple[1]:
                    newWorkingDeque.append(transform(workingTuple[0],stepTuple[1],stepOffset))
                    workingDeque.append((stepTuple[1],workingTuple[1]))
                #right overlap
                elif stepTuple[0] >= workingTuple[0] and stepTuple[1] >= workingTuple[1]:
                    newWorkingDeque.append(transform(stepTuple[0],workingTuple[1],stepOffset))
                    workingDeque.append((workingTuple[0],stepTuple[0]))
                else:
                    newWorkingDeque.append(transform(stepTuple[0],stepTuple[1],stepOffset))
                    workingDeque.append((workingTuple[0],stepTuple[0]))
                    workingDeque.append((stepTuple[1],workingTuple[1]))
            else:
                #no match found, send the tuple to the back
                workingDeque.append(workingTuple)
    workingDeque.extend(newWorkingDeque)

print(sorted(workingDeque))