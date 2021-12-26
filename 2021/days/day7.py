from statistics import median_low

from .day_template import Day


class Day7(Day):
	@staticmethod
	def convert_input(raw_input):
		return [int(n) for n in raw_input.split(',')]

	@classmethod
	def run_first(cls, puzzle_input):
		target_position = median_low(puzzle_input)
		return sum(abs(x - target_position) for x in puzzle_input)

	@classmethod
	def run_second(cls, puzzle_input):
		lower_bound = min(puzzle_input)
		upper_bound = max(puzzle_input)

		while lower_bound < upper_bound - 1:
			center = (lower_bound + upper_bound) // 2
			center_gradient = sum(position - center - (center < position) for position in puzzle_input)
			if center_gradient > 0:
				lower_bound = center
			else:
				upper_bound = center

		cost = 0
		for position in puzzle_input:
			distance = abs(position - lower_bound)
			cost += distance * (distance + 1) // 2 # 1+2+3+...+n = n*(n+1)/2
		return cost
