import itertools
import math


def convert_input(raw_input):
	return list(map(int, raw_input.split()))

def run_first(puzzle_input):
	return find_product_of_summing_numbers(puzzle_input, 2, 2020)

def run_second(puzzle_input):
	return find_product_of_summing_numbers(puzzle_input, 3, 2020)

def find_product_of_summing_numbers(numbers, numbers_count, target_sum):
	for combination in itertools.combinations(numbers, numbers_count):
		if sum(combination) == target_sum:
			return math.prod(combination)
