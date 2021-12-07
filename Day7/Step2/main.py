import math

inputVal = open('input').read().splitlines()
inputVal = [int(a) for a in inputVal[0].split(',')]

count =  math.inf

def getMoveCost(start, end):
	count = 0
	distance = abs(start - end)
	for i in range(distance + 1):
		count += i
	return count

print(getMoveCost(2, 5))

distance = 0



for i in range(1000):
	total = sum([getMoveCost(a, i) for a in inputVal])
	if total < count:
		count = total
		distance = i

for a in inputVal:
	print(a, " to", distance ,":", getMoveCost(a, distance))
print(count)