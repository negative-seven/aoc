import importlib
import sys


def main():
	day_number = sys.argv[1]
	run_solution(day_number)

def run_solution(day_number):
	solution_module = importlib.import_module(f'days.day{day_number}')
	with open(f'inputs/day{day_number}.txt', 'r') as input_file:
		raw_input = input_file.read()

	converted_input = solution_module.convert_input(raw_input)

	print('Answer for part one:')
	print(solution_module.run_first(converted_input))
	print()
	print('Answer for part two:')
	print(solution_module.run_second(converted_input))

main()
