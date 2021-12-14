import copy
from collections import deque
import itertools

from .day_template import Day


class Day11(Day):
	@staticmethod
	def convert_input(raw_input):
		return [[int(n) for n in row] for row in raw_input.splitlines()]

	@staticmethod
	def run_first(puzzle_input):
		cells = copy.deepcopy(puzzle_input)
		return sum(Day11.run_step(cells) for _ in range(100))

	@staticmethod
	def run_second(puzzle_input):
		cells = copy.deepcopy(puzzle_input)
		cell_count = sum(len(row) for row in cells)
		for step in itertools.count(start=1):
			if Day11.run_step(cells) == cell_count:
				return step

	@staticmethod
	def run_step(cells):
		MOVE_VECTORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

		potential_flash_indices = set()
		for y, row in enumerate(cells):
			for x, _ in enumerate(row):
				cells[y][x] += 1
				if cells[y][x] >= 10:
					potential_flash_indices.add((x, y))

		flashes = 0
		flashed_indices = set()
		while potential_flash_indices:
			x, y = potential_flash_indices.pop()
			if cells[y][x] >= 10 and (x, y) not in flashed_indices:
				flashes += 1
				flashed_indices.add((x, y))
				for vector in MOVE_VECTORS:
					other_x = x + vector[0]
					other_y = y + vector[1]
					if 0 <= other_y < len(cells) and 0 <= other_x < len(cells[y]):
						cells[other_y][other_x] += 1
						potential_flash_indices.add((other_x, other_y))

		for x, y in flashed_indices:
			cells[y][x] = 0

		return flashes
