import re

class PasswordData:
	def __init__(self):
		self.first_value = None
		self.second_value = None
		self.character = None
		self.password = None

def convert_input(raw_input):
	passwords_data = []

	for raw_password_data in raw_input.splitlines():
		first_value, second_value, checked_letter, password = re.fullmatch(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', raw_password_data).groups()

		password_data = PasswordData()
		password_data.first_value = int(first_value)
		password_data.second_value = int(second_value)
		password_data.character = checked_letter
		password_data.password = password
		passwords_data.append(password_data)

	return passwords_data

def run_first(puzzle_input):
	valid_passwords_count = 0
	for data in puzzle_input:
		if data.first_value <= data.password.count(data.character) <= data.second_value:
			valid_passwords_count += 1
	return valid_passwords_count

def run_second(puzzle_input):
	valid_passwords_count = 0
	for data in puzzle_input:
		first_character = data.password[data.first_value - 1]
		second_character = data.password[data.second_value - 1]
		if first_character != second_character and data.character in set([first_character, second_character]):
			valid_passwords_count += 1
	return valid_passwords_count
