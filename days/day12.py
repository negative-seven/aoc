def convert_input(raw_input):
	return list(map(lambda x:(x[0], int(x[1:])), raw_input.splitlines()))

def run_first(actions):
	position = 0
	direction = 1
	for command, value in actions:
		if command == 'N':
			position += -1j * value
		elif command == 'S':
			position += 1j * value
		elif command == 'E':
			position += 1 * value
		elif command == 'W':
			position += -1 * value
		elif command == 'L':
			direction *= (-1j) ** (value // 90)
		elif command == 'R':
			direction *= 1j ** (value // 90)
		elif command == 'F':
			position += direction * value
	return int(abs(position.real) + abs(position.imag))

def run_second(actions):
	position = 0 + 0j
	waypoint = 10 + -1j
	for command, value in actions:
		if command == 'N':
			waypoint += -1j * value
		elif command == 'S':
			waypoint += 1j * value
		elif command == 'E':
			waypoint += 1 * value
		elif command == 'W':
			waypoint += -1 * value
		elif command == 'L':
			waypoint *= (-1j) ** (value // 90)
		elif command == 'R':
			waypoint *= 1j ** (value // 90)
		elif command == 'F':
			position += waypoint * value
	return int(abs(position.real) + abs(position.imag))
