input = open('input').read().splitlines()
pairList = [[[int(x) for x in a.split(" -> ")[0].split(',')], [int(x) for x in a.split(" -> ")[1].split(',')]] for a in input]


maxHeight = 0
maxWidth = 0
for pair in pairList:

	if pair[0][0] > maxWidth:
		maxWidth = pair[0][0]
	if pair[1][0] > maxWidth:
		maxWidth = pair[1][0]

	if pair[0][1] > maxHeight:
		maxHeight = pair[0][1]
	if pair[1][1] > maxHeight:
		maxHeight = pair[1][1]

print("Size", maxHeight, maxWidth)

recordArray = [[0 for a in range(maxWidth + 1)] for a in range(maxHeight + 1)]

for pairOne, pairTwo in pairList:
	if pairOne[0] == pairTwo[0]:
		maxHeight = max(pairOne[1], pairTwo[1]) + 1
		minHeight = min(pairOne[1], pairTwo[1])
		for i in range(minHeight, maxHeight):
			recordArray[i][pairOne[0]] += 1 if recordArray[i][pairOne[0]] < 2 else 0
	elif pairOne[1] == pairTwo[1]:
		maxWidth = max(pairOne[0], pairTwo[0]) + 1
		minWidth = min(pairOne[0], pairTwo[0])
		for i in range(minWidth, maxWidth):
			recordArray[pairOne[1]][i] += 1 if recordArray[pairOne[1]][i] < 2 else 0
	else:
		distance = abs(pairOne[0] - pairTwo[0]) + 1
		for i in range(distance):
			w = pairOne[0] + i if pairOne[0] < pairTwo[0] else pairOne[0] - i
			h = pairOne[1] + i if pairOne[1] < pairTwo[1] else pairOne[1] - i
			recordArray[h][w] += 1 if recordArray[h][w] < 2 else 0

count = 0

for rowIndex in range(len(recordArray)):
	for caseIndex in range(len(recordArray[rowIndex])):
		if recordArray[rowIndex][caseIndex] == 0:
			recordArray[rowIndex][caseIndex] = '.'
		
	print(*recordArray[rowIndex], sep='')
	if recordArray[rowIndex][caseIndex] != '.' and recordArray[rowIndex][caseIndex] > 2:
			recordArray[rowIndex][caseIndex] = 2
	count += recordArray[rowIndex].count(2)
print(count)
