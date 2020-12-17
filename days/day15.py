from collections import defaultdict


def convert_input(raw_input):
	return list(map(int, raw_input.split(',')))

def run_first(numbers):
	return get_simulation_value_at_index(numbers, 2020)

def run_second(numbers):
	return get_simulation_value_at_index(numbers, 30000000)

def get_simulation_value_at_index(starting_numbers, index):
	numbers_most_recent_steps = defaultdict(lambda: step - 1)

	number = starting_numbers[0]
	for step in range(1, index):
		new_number = step - numbers_most_recent_steps[number] - 1
		numbers_most_recent_steps[number] = step - 1
		if step < len(starting_numbers):
			number = starting_numbers[step]
		else:
			number = new_number
	return number
