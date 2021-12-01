from abc import ABC, abstractmethod


class Day(ABC):
	@staticmethod
	@abstractmethod
	def convert_input(raw_input):
		pass

	@staticmethod
	@abstractmethod
	def run_first(puzzle_input):
		pass

	@staticmethod
	@abstractmethod
	def run_second(puzzle_input):
		pass
