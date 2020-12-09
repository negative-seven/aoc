import itertools


def convert_input(raw_input):
	return list(map(int, raw_input.splitlines()))

def run_first(numbers):
	preamble_length = 25

	for index in range(preamble_length, len(numbers) - 1):
		number = numbers[index]
		if not any(sum(pair) == number for pair in itertools.combinations(numbers[index - preamble_length : index], 2)):
			return number

def run_second(numbers):
	target_sum = run_first(numbers)

	for start_index in range(len(numbers)):
		for end_index in range(start_index + 2, len(numbers) + 1):
			if sum(numbers[start_index : end_index]) == target_sum:
				return numbers[start_index] + numbers[end_index - 1]
