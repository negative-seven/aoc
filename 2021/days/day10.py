import enum
from statistics import median_low

from .day_template import Day


class BracketErrorType(enum.Enum):
	LINE_CORRUPTED = enum.auto(),
	LINE_INCOMPLETE = enum.auto(),

class Day10(Day):
	@staticmethod
	def convert_input(raw_input):
		return raw_input.splitlines()

	@staticmethod
	def run_first(puzzle_input):
		BRACKET_SCORES = {
			')': 3,
			']': 57,
			'}': 1197,
			'>': 25137,
		}

		score = 0
		for error_type, error_data in Day10.get_errors(puzzle_input):
			if error_type == BracketErrorType.LINE_CORRUPTED:
				score += BRACKET_SCORES[error_data]

		return score

	@staticmethod
	def run_second(puzzle_input):
		BRACKET_SCORES = {
			')': 1,
			']': 2,
			'}': 3,
			'>': 4,
		}

		scores = []
		for error_type, error_data in Day10.get_errors(puzzle_input):
			if error_type == BracketErrorType.LINE_INCOMPLETE:
				scores.append(sum(BRACKET_SCORES[b] * (5 ** i) for i, b in enumerate(error_data)))

		return median_low(scores)

	@staticmethod
	def get_errors(lines):
		OPEN_BRACKETS = set('([{<')
		MATCHING_CLOSE_BRACKETS = {
			'(': ')',
			'[': ']',
			'{': '}',
			'<': '>',
		}

		for line in lines:
			syntax_error = False
			current_layers = []
			for bracket in line:
				if bracket in OPEN_BRACKETS:
					current_layers.append(bracket)
				else:
					corresponding_bracket = current_layers.pop()
					if bracket != MATCHING_CLOSE_BRACKETS[corresponding_bracket]:
						yield BracketErrorType.LINE_CORRUPTED, bracket
						syntax_error = True
				if syntax_error:
					break
			if not syntax_error and current_layers:
				yield BracketErrorType.LINE_INCOMPLETE, [MATCHING_CLOSE_BRACKETS[b] for b in current_layers]
