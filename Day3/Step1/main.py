input = open('input').read().splitlines()
inputList = [a for a in input]
newInputList = []

for bits in inputList:
	tmp = []
	for bit in bits:
		tmp.append(int(bit))
	newInputList.append(tmp)

mostCommon = []
leastCommon = []

for i in range(len(newInputList[0])):
	oneCount = 0
	zeroCount = 0
	for h in range(len(newInputList)):
		if newInputList[h][i] == 0:
			zeroCount += 1
		else:
			oneCount += 1
	if zeroCount > oneCount:
		mostCommon.append(0)
		leastCommon.append(1)
	else:
		mostCommon.append(1)
		leastCommon.append(0)
	
print(*mostCommon)
print(*leastCommon)