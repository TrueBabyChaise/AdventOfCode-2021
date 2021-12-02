input = open('input').read().splitlines()
inputList = [int(a) for a in input]

res = 0
for i in range(1, len(inputList)):
	if inputList[i] > inputList[i-1]:
		res +=1
print(res)