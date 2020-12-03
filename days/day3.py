import math


def convert_input(raw_input):
	return [[c == '#' for c in row] for row in raw_input.splitlines()]

def run_first(board):
	return get_trees_encountered(board, 3, 1)

def run_second(board):
	slopes = [
		(1, 1),
		(3, 1),
		(5, 1),
		(7, 1),
		(1, 2),
	]

	return math.prod(map(lambda slope: get_trees_encountered(board, slope[0], slope[1]), slopes))

def get_trees_encountered(board, speed_x, speed_y):
	x = 0
	y = 0
	trees_encountered = 0
	while True:
		x += speed_x
		x %= len(board[y])
		y += speed_y
		if y >= len(board):
			break
		trees_encountered += board[y][x]

	return trees_encountered
