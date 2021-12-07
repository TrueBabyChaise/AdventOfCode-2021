inputVal = open('input').read().splitlines()
inputVal = [int(a) for a in inputVal[0].split(',')]

count = 0

for i in range(1000):
	total = sum([abs(a - i) for a in inputVal])
	print(total, i)
	if total < count:
		count = total
print(count)
