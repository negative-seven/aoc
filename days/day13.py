import math


def convert_input(raw_input):
	time, raw_buses = raw_input.splitlines()
	time = int(time)
	buses = []
	for bus in raw_buses.split(','):
		try:
			buses.append(int(bus))
		except ValueError:
			buses.append(bus)
	return time, buses

def run_first(puzzle_input):
	time = puzzle_input[0]
	buses = list(filter(lambda x: x != 'x', puzzle_input[1]))
	return math.prod(min(map(lambda x: (x, x - time % x), buses), key=lambda x: x[1]))

def run_second(puzzle_input):
	buses = list(map(lambda x: ((x[1] - x[0]) % x[1], x[1]),filter(lambda x: x[1] != 'x', enumerate(puzzle_input[1]))))
	while len(buses) > 1:
		buses.sort(key=lambda x: -x[1])
		bus0 = buses[-2]
		bus1 = buses[-1]

		remainder0 = bus0[0]
		divisor0 = bus0[1]
		remainder1 = bus1[0]
		divisor1 = bus1[1]

		shared_divisor = math.lcm(divisor0, divisor1)
		shared_remainder = remainder0
		while shared_remainder % divisor1 != remainder1:
			shared_remainder += divisor0
		buses = buses[:-2]
		buses.append((shared_remainder, shared_divisor))
	return buses[0][0]
