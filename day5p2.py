from collections import deque

seeds = []
mappingList = []
sourceFile = "day5.txt"

def getRangeTupleFromLine(line):
    arr = [int(x) for x in line.strip().split(" ") if len(x) > 0]
    return (arr[1],arr[1]+arr[2],arr[0])

def getRangeFromTuple(rangeTuple):
    return range(rangeTuple[0],rangeTuple[1])

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
            mappingList.append(sorted(stepList))
        elif line.endswith("map:"):
            stepList = []
        else:
            stepList.append(getRangeTupleFromLine(line))

def findDiscontinuities(thisList):
    for y in range(len(thisList)):
        stepList = thisList[y]
        for x in range(len(stepList)-1):
            if stepList[x][1] < stepList[x+1][0]:
                print(y,stepList[x],stepList[x+1])

def resolveContinuitites(head,thisDeque : deque):
    if len(thisDeque) == 0:
        thisDeque.append(head)
        return thisDeque
    newHead = thisDeque.popleft()
    if len(thisDeque) == 0:
        if head[0] <= newHead[0] and head[1] >= newHead[0]:
            thisDeque.append((min(head[0],newHead[0]),max(head[1],newHead[1])))
        else:
            thisDeque.append(head)
            thisDeque.append(newHead)
        return thisDeque           
    else:
        if head[0] <= newHead[0] and head[1] >= newHead[0]:
            return resolveContinuitites((min(head[0],newHead[0]),max(head[1],newHead[1])),thisDeque)
        else:
            thisDeque = resolveContinuitites(newHead,thisDeque)
            thisDeque.appendleft(head)
            return thisDeque





if __name__ == '__main__':
    lowestLocation = None
    readFile()
    #findDiscontinuities(mappingList)
    outputRanges = []
    for x in range(0,len(seeds),2): 
        inputRanges = deque()
        outputRanges = deque()
        inputRanges.append((seeds[x],seeds[x]+seeds[x+1]))
        print(f"seed: {inputRanges}")
        for stepList in mappingList:
            print("stepList:",stepList)
            outputRanges = deque()
            print(f"Input Ranges: {inputRanges}")
            for inputTuple in inputRanges:
                foundTransformer = False
                diffs = list()
                intersections = list()
                for transformTuple in stepList:
                    if inputTuple[0] < transformTuple[1] and inputTuple[1] > transformTuple[0]:
                        foundTransformer = True
                        intersectionMin = max(inputTuple[0],transformTuple[0])
                        intersectionMax = min(inputTuple[1],transformTuple[1])
                        intersection = (
                            intersectionMin,
                            intersectionMax,
                            (intersectionMin-transformTuple[0])+transformTuple[2],
                            (intersectionMax-transformTuple[0])+transformTuple[2]
                        )
                        # intersections.append((
                        #     (intersection[0]-transformTuple[0])+transformTuple[2],
                        #     (intersection[1]-transformTuple[0])+transformTuple[2]
                        # ))
                        intersections.append(intersection)
                
                #TODO: Build logic to resolve conflicts between differences and intersections
                for x in range(len(diffs)):
                    diff = diffs[x]
                    for inter in intersections:
                        if diff[1] >= inter[0] and diff[0] <= inter[1]:
                            #We have an intersection between the diff and the intersection, and we need to correct.

                            if diff[0] == inter[0] and diff[1] == inter[1]:
                                diff = ()
                                diffs[x] = diff
                                break
                            if diff[0] < inter[0]:
                                if diff[1] <= inter[1]:
                                    diff = (diff[0],inter[0])
                                    diffs[x] = diff
                                else:
                                    #intersection fully contained by diff
                                    print("Why is this happening")
                            else:
                                if diff[1] <= inter[1]:
                                    diff = ()
                                    diffs[x] = diff
                                    break
                                else:
                                    diff = (inter(1),diff[1])
                                    diffs[x] = diff
                for diff in diffs:
                    outputRanges.append(diff)
                for inter in intersections:
                    outputRanges.append(inter[2:])
                                    
                
                if foundTransformer == False:
                    outputRanges.append(inputTuple)
            outputRanges = deque(sorted(outputRanges))
            #outputRanges = deque([x for x in sorted(outputRanges) if x[0] < x[1]])
            #outputRanges = resolveContinuitites(outputRanges.popleft(),outputRanges)
            print("outputRanges:",outputRanges,len(outputRanges))
            inputRanges = outputRanges
        
        if len(outputRanges) > 0:
            lowestOutput = min(x[0] for x in outputRanges)
            if lowestLocation is None:
                lowestLocation = lowestOutput
            else:
                lowestLocation = min(lowestLocation,lowestOutput)
    print("lowestLocation: {lowestLocation}")
        

