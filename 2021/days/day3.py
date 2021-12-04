from statistics import multimode
from operator import eq, ne

from .day_template import Day


class Day3(Day):
	@staticmethod
	def convert_input(raw_input):
		return raw_input.split()

	@staticmethod
	def run_first(puzzle_input):
		length = len(puzzle_input[0])
		gamma_rate_bitstring = ''.join(Day3._get_mode_digit(puzzle_input, index) for index in range(length))
		epsilon_rate_bistring = str.translate(gamma_rate_bitstring, str.maketrans({'0': '1', '1': '0'}))
		return int(gamma_rate_bitstring, 2) * int(epsilon_rate_bistring, 2)

	@staticmethod
	def run_second(puzzle_input):
		length = len(puzzle_input[0])
		result = 1
		for comparison in [eq, ne]:
			bitstrings = puzzle_input
			for index in range(length):
				bitstrings = [s for s in bitstrings if comparison(s[index], Day3._get_mode_digit(bitstrings, index))]
				if len(bitstrings) == 1:
					result *= int(bitstrings[0], 2)
					break
		return result

	@staticmethod
	def _get_mode_digit(bitstrings, index):
		return max(multimode(s[index] for s in bitstrings))
