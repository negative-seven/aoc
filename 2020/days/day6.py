def convert_input(raw_input):
	return [list(map(set, group.splitlines())) for group in raw_input.split('\n\n')]

def run_first(group_answers):
	return sum(map(lambda g: len(set.union(*g)), group_answers))

def run_second(group_answers):
	return sum(map(lambda g: len(set.intersection(*g)), group_answers))
