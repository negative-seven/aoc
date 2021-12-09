from collections import Counter
from functools import reduce
from operator import mul

from .day_template import Day


class Day9(Day):
	@staticmethod
	def convert_input(raw_input):
		return [[int(cell) for cell in row] for row in raw_input.splitlines()]

	@staticmethod
	def run_first(puzzle_input):
		low_points = {Day9.get_flow_target(puzzle_input, x, y) for y in range(len(puzzle_input)) for x in range(len(puzzle_input[y]))}
		low_points.remove(None)
		return sum(puzzle_input[point[1]][point[0]] + 1 for point in low_points)

	@staticmethod
	def run_second(puzzle_input):
		basins = Counter()
		for y in range(len(puzzle_input)):
			for x in range(len(puzzle_input[y])):
				basins[Day9.get_flow_target(puzzle_input, x, y)] += 1
		basins.pop(None, None)
		return reduce(mul, [v for k, v in basins.most_common(3)], 1)

	@staticmethod
	def get_flow_target(heightmap, x, y):
		MOVE_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

		height = heightmap[y][x]
		if height == 9:
			return None

		for vector in MOVE_VECTORS:
			if 0 <= x + vector[0] < len(heightmap[0]) and 0 <= y + vector[1] < len(heightmap):
				adjacent_height = heightmap[y + vector[1]][x + vector[0]]
				if adjacent_height < height:
					return Day9.get_flow_target(heightmap, x + vector[0], y + vector[1])
		return x, y
