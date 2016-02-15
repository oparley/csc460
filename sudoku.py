grid = [
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],

[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],

[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0],
]

def validRow(value, row):
	valid = True
	for i in range(0, 9):
		if grid[row][i] == value:
			valid = False
			break;
	return valid

def validColumn(value, column):
	valid = True
	for i in range(0, 9):
		if grid[i][column] == value:
			valid = False
			break;
	return valid

def validBlock(value, row, column):
	block_row = row // 3;
	block_column = column // 3;
	for x in range(block_row, block_row + 3):
		for y in range(block_column, block_column + 3):
			print(grid[x][y], x, y)
			if grid[x][y] == value:
				return False
	return True



print(validRow(9, 0))
print(validColumn(9, 0))

print(validBlock(6, 2, 5))