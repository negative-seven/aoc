from collections import Counter


def convert_input(raw_input):
	values = list(map(int, raw_input.splitlines()))
	return values + [0, max(values) + 3]

def run_first(values):
	values.sort()
	differences_count = Counter(get_differences(values))
	return differences_count[1] * differences_count[3]

# this solution assumes there were no differences of two in part 1 of the puzzle
def run_second(values):
	differences = get_differences(values)

	ones_in_a_row_to_arrangements = [1, 1, 2] # recursive relation, f(n) = f(n-1) + f(n-2) + f(n-3)
	ones_in_a_row = 0
	arrangements = 1
	for difference in differences:
		if difference == 1:
			ones_in_a_row += 1
		elif difference == 3:
			while len(ones_in_a_row_to_arrangements) - 1 < ones_in_a_row:
				ones_in_a_row_to_arrangements.append(sum(ones_in_a_row_to_arrangements[-3:]))
			arrangements *= ones_in_a_row_to_arrangements[ones_in_a_row]
			ones_in_a_row = 0
	return arrangements

def get_differences(values):
	values.sort()
	return list(map(lambda p: p[1] - p[0], zip(values, values[1:])))
