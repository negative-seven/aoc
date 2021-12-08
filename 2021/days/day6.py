from collections import Counter
from functools import cache

from .day_template import Day


class Day6(Day):
	@staticmethod
	def convert_input(raw_input):
		return Counter(int(n) for n in raw_input.split(','))

	@staticmethod
	def run_first(puzzle_input):
		return Day6.simulate_fish(puzzle_input, 80)

	@staticmethod
	def run_second(puzzle_input):
		return Day6.simulate_fish(puzzle_input, 256)

	@staticmethod
	def simulate_fish(fish_timers, total_time):
		return sum(Day6.simulate_one_fish(timer, total_time) * count for timer, count in fish_timers.items())

	@staticmethod
	@cache
	def simulate_one_fish(timer, time_left):
		if timer >= time_left:
			return 1
		else:
			return Day6.simulate_one_fish(6, time_left - timer - 1) + Day6.simulate_one_fish(8, time_left - timer - 1)
