inputVal = open('input').read().splitlines()
inputVal = [int(a) for a in inputVal[0].split(',')]

listVal = [0 for i in range(7)]
newCountDown = [0 for i in range(9)]

for val in inputVal:
	listVal[val] += 1

def getCount():
	count = 0
	print(*listVal)
	print(*newCountDown)
	for a in listVal:
		count += a
	for a in newCountDown:
		count += a
	return count


for time in range(80):
	tmp = listVal[0]
	tmpCountDown = newCountDown[0]
	for i in range(len(listVal) - 1):
		listVal[i] = listVal[i+1]
	for i in range(len(newCountDown) -1):
		newCountDown[i] = newCountDown[i+1]
	newCountDown[8] = tmp + tmpCountDown
	listVal[6] = tmp + tmpCountDown

print(getCount())
