from .day_template import Day


class Day2(Day):
	@staticmethod
	def convert_input(raw_input):
		iterator = iter(raw_input.split())
		pairs = zip(iterator, iterator)
		return [(x, int(y)) for x, y in pairs]

	@classmethod
	def run_first(cls, puzzle_input):
		position = 0
		depth = 0
		for command, distance in puzzle_input:
			if command == 'forward':
				position += distance
			elif command == 'down':
				depth += distance
			elif command == 'up':
				depth -= distance
		return position * depth

	@classmethod
	def run_second(cls, puzzle_input):
		position = 0
		depth = 0
		aim = 0
		for command, distance in puzzle_input:
			if command == 'forward':
				position += distance
				depth += aim * distance
			elif command == 'down':
				aim += distance
			elif command == 'up':
				aim -= distance
		return position * depth
