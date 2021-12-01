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

	running_sums = [0]
	current_sum = 0
	for number in numbers:
		current_sum += number
		running_sums.append(current_sum)

	start_index = 0
	end_index = 0
	while True:
		current_sum = running_sums[end_index] - running_sums[start_index]
		if current_sum < target_sum:
			end_index += 1
		elif current_sum > target_sum:
			start_index += 1
		else:
			return numbers[start_index] + numbers[end_index - 1]
