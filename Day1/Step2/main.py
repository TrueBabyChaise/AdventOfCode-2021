input = open('input').read().splitlines()
inputList = [int(a) for a in input]

newList = list()
for i in range(0, len(inputList) - 2):
	newList.append(inputList[i] + inputList[1 + i] + inputList[2 + i])

res = 0
for i in range(1, len(newList)):
	if newList[i] > newList[i-1]:
		res +=1
print(res)