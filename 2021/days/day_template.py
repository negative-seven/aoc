from abc import ABC, abstractmethod


class Day(ABC):
	@staticmethod
	@abstractmethod
	def convert_input(raw_input):
		pass

	@classmethod
	@abstractmethod
	def run_first(cls, puzzle_input):
		pass

	@classmethod
	@abstractmethod
	def run_second(cls, puzzle_input):
		pass
