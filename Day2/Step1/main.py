input = open('input').read().splitlines()
inputList = [[a.split()[0], int(a.split()[1])] for a in input]

horizontal = 0
depth = 0

for action, value in inputList:
	if action == 'forward':
		horizontal += value
	if action == 'down':
		depth += value
	if action == 'up':
		depth -= value

print(horizontal * depth)