import re

from .day_template import Day


class Day8(Day):
	DIGIT_ENCODINGS = {
		frozenset('abcefg'): 0,
		frozenset('cf'): 1,
		frozenset('acdeg'): 2,
		frozenset('acdfg'): 3,
		frozenset('bcdf'): 4,
		frozenset('abdfg'): 5,
		frozenset('abdefg'): 6,
		frozenset('acf'): 7,
		frozenset('abcdefg'): 8,
		frozenset('abcdfg'): 9,
	}

	@staticmethod
	def convert_input(raw_input):
		return [tuple(tuple(s.split()) for s in line.split('|')) for line in raw_input.splitlines()]

	@staticmethod
	def run_first(puzzle_input):
		digits = ''.join(str(n) for n in Day8.decode_numbers(puzzle_input))
		return len(re.findall(r'[1478]', digits))

	@staticmethod
	def run_second(puzzle_input):
		return sum(Day8.decode_numbers(puzzle_input))

	@staticmethod
	def decode_numbers(pattern_output_pairs):
		numbers = []

		real_hashes = Day8.get_segment_hashes(Day8.DIGIT_ENCODINGS)
		for patterns, output in pattern_output_pairs:
			pattern_hashes = Day8.get_segment_hashes(patterns)
			mapping = str.maketrans({character: real_hashes[character_hash] for character_hash, character in pattern_hashes.items()})

			mapped_output = [frozenset(x.translate(mapping)) for x in output]
			number = int(''.join(str(Day8.DIGIT_ENCODINGS[x]) for x in mapped_output))
			numbers.append(number)
		return numbers

	@staticmethod
	def get_segment_hashes(encodings):
		# returns a different value for each segment, which can be used to identify it
		return {sum(len(x) ** 2 for x in encodings if c in x): c for c in 'abcdefg'}
