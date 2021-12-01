import importlib
import sys


def main():
	day_number = sys.argv[1]
	run_solution(day_number)

def run_solution(day_number):
	with open(f'inputs/day{day_number}.txt', 'r') as input_file:
		raw_input = input_file.read()

	solution_module = importlib.import_module(f'days.day{day_number}')
	solution = getattr(solution_module, f'Day{day_number}')

	converted_input = solution.convert_input(raw_input)

	print('Answer for part one:')
	print(solution.run_first(converted_input))
	print()
	print('Answer for part two:')
	print(solution.run_second(converted_input))


if __name__ == '__main__':
	main()
