input = open('input').read().splitlines()
inputList = [[a.split()[0], int(a.split()[1])] for a in input]

horizontal = 0
depth = 0
aim = 0

for action, value in inputList:
	if action == 'forward':
		horizontal += value
		depth += aim * value
	if action == 'down':
		aim += value
	if action == 'up':
		aim -= value

print(horizontal * depth)