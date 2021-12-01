def convert_input(raw_input):
	seat_numbers = []

	for line in raw_input.splitlines():
		row = binary_string_to_int(line[:7], 'FB')
		column = binary_string_to_int(line[7:], 'LR')

		seat = row * 8 + column
		seat_numbers.append(seat)

	return seat_numbers

def run_first(seat_numbers):
	return max(seat_numbers)

def run_second(seat_numbers):
	seat_numbers.sort()
	for x, y in zip(seat_numbers, seat_numbers[1:]):
		if x + 1 != y:
			return x + 1

def binary_string_to_int(string, digits):
	return int(string.translate(str.maketrans(digits, '01')), len(digits))
