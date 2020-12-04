import re


REQUIRED_ENTRIES = [
	('byr', lambda v: 1920 <= int(v) <= 2002),
	('iyr', lambda v: 2010 <= int(v) <= 2020),
	('eyr', lambda v: 2020 <= int(v) <= 2030),
	('hgt', lambda v: (v.endswith('in') and 59 <= int(v[:-2]) <= 76) or (v.endswith('cm') and 150 <= int(v[:-2]) <= 193)),
	('hcl', lambda v: re.fullmatch(r'#[0-9a-f]{6}', v)),
	('ecl', lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
	('pid', lambda v: re.fullmatch(r'\d{9}', v)),
]

def convert_input(raw_input):
	passports = []
	for raw_passport_data in raw_input.split('\n\n'):
		passport_data = dict(re.findall('([^\s:]+):([^\s:]+)', raw_passport_data))
		passports.append(passport_data)

	return passports

def run_first(passports):
	required_keys = [e[0] for e in REQUIRED_ENTRIES]
	return sum(
		all(
			key in passport.keys()
		for key in required_keys)
	for passport in passports)

def run_second(passports):
	return sum(
		all(
			entry[0] in passport.keys() and entry[1](passport[entry[0]])
		for entry in REQUIRED_ENTRIES)
	for passport in passports)
