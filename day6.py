# timeDistance = [(41,244),(66,1047),(72,1228),(66,1040)]
#timeDistance = [(7,9),(15,40),(30,200)]
#timeDistance = [(71530,940200)]
timeDistance = [(41667266,244104712281040)]

for tD in timeDistance:
    time = tD[0]
    minDistance = tD[1]
    print(sum([1 for x in range(time+1) if time*x-x**2 > minDistance]))