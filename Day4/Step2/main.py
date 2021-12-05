input = open('input').read().splitlines()
numberList = [int(a) for a in input[0].split(",")]

if 14 in numberList:
	print("connard")

tmp = []
boardList = []
for i in range(2, len(input)):
	
	if (i - 1) % 6 == 0:
		boardList.append(tmp)
		tmp = []
	else:
		tmp.append(list(filter(None, input[i].replace('  ', ' ').split(' '))))

boardList.append(tmp)


def isBoardWinning(board, listNumber, height=5,width=5, boardIndex=0):

	for h in range(height):
		isDiff = False
		for w in range(width):
			if int(board[h][w]) not in listNumber:
				isDiff = True
				break
		if not isDiff:
				return True

	for w in range(width):
		isDiff = False
		for h in range(height):
			if int(board[h][w]) not in listNumber:
				isDiff = True
				break
		if not isDiff:
			return True

	if height != width:
		return False

	isDiff = True
	for i in range(height):
		if int(board[i][height - 1 - i]) not in listNumber:
			isDiff = True
			break
	if not isDiff:
		return True

	isDiff = True
	for i in range(height):
		if int(board[i][i]) not in listNumber:
			isDiff = True
			break
	if not isDiff:
		return True

	return False


winningNumber = None
winningBoard = None
isEnded = False

for i in range(len(numberList), 0, -1):
	if isEnded:
		break
	for board in boardList:
		if not isBoardWinning(board, numberList[:i]):
			winningNumber = numberList[i]
			winningBoard = board
			isEnded = True
			break
			

score = 0

for row in board:
	row = [int(a) for a in row]
	for number in row:
		if number not in numberList[:numberList.index(winningNumber) + 1]:
			score += int(number)
	
print(winningBoard)
print(winningNumber)
print(score)

print("Result:", score * winningNumber)