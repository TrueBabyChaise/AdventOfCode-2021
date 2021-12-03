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

oxygenList = newInputList.copy()


for bit in range(len(mostCommon)):
	red = 0
	oneCount = 0
	zeroCount = 0
	for h in range(len(oxygenList)):
		if oxygenList[h][bit] == 0:
			zeroCount += 1
		else:
			oneCount += 1
		if zeroCount > oneCount:
			mostCommon[bit] = 0
			leastCommon[bit] = 1
		else:
			mostCommon[bit] = 1
			leastCommon[bit] = 0
	for i in range(len(oxygenList)):
		if oxygenList[i - red][bit] != mostCommon[bit]:
			oxygenList.pop(i - red)
			red += 1



cO2List = newInputList.copy()

for bit in range(len(mostCommon)):
	if len(cO2List) == 1:
		break
	red = 0
	oneCount = 0
	zeroCount = 0
	for h in range(len(cO2List)):
		if cO2List[h][bit] == 0:
			zeroCount += 1
		else:
			oneCount += 1
		if zeroCount > oneCount:
			mostCommon[bit] = 0
			leastCommon[bit] = 1
		else:
			mostCommon[bit] = 1
			leastCommon[bit] = 0
	if bit == 9:
		print("Least Common bit : ", leastCommon[bit], bit)
	for i in range(len(cO2List)):
		if cO2List[i - red][bit] != leastCommon[bit]:
			cO2List.pop(i - red)
			red += 1


print(oxygenList, 1935)
print(cO2List, 3145)

print(3145 * 1935)