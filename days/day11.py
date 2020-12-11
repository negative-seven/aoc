import copy


def convert_input(raw_input):
	return [list(map(lambda x: False if x == 'L' else None, row)) for row in raw_input.splitlines()]

def run_first(initial_seats_state):
	def calculate_neighbor_counts(seats_state):
		neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

		neighbor_counts = [[0 for _ in row] for row in seats_state]
		for y, row in enumerate(seats_state):
			for x, tile in enumerate(row):
				if tile:
					for offset_x, offset_y in neighbor_offsets:
						neighbor_x = x + offset_x
						neighbor_y = y + offset_y
						if neighbor_y < 0 or neighbor_x < 0 or neighbor_y >= len(seats_state) or neighbor_x >= len(seats_state[y]):
							continue
						neighbor_counts[neighbor_y][neighbor_x] += 1
		return neighbor_counts

	return run_simulation_and_count_occupied(initial_seats_state, 4, calculate_neighbor_counts)

def run_second(initial_seats_state):
	def calculate_neighbor_counts(seats_state):
		neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

		neighbor_counts = [[0 for _ in row] for row in seats_state]
		for y, row in enumerate(seats_state):
			for x, tile in enumerate(row):
				if tile:
					for offset_x, offset_y in neighbor_offsets:
						distance = 1
						while True:
							neighbor_x = x + offset_x * distance
							neighbor_y = y + offset_y * distance
							if neighbor_y < 0 or neighbor_x < 0 or neighbor_y >= len(seats_state) or neighbor_x >= len(seats_state[y]):
								break
							neighbor = seats_state[neighbor_y][neighbor_x]
							if neighbor is not None:
								neighbor_counts[neighbor_y][neighbor_x] += 1
								break
							distance += 1
		return neighbor_counts

	return run_simulation_and_count_occupied(initial_seats_state, 5, calculate_neighbor_counts)

def run_simulation_and_count_occupied(seats_state, occupied_threshold, neighbor_update_function):
	while True:
		neighbor_counts = neighbor_update_function(seats_state)

		new_seats_state = [[None for _ in row] for row in seats_state]
		state_changed = False
		for y, row in enumerate(seats_state):
			for x, tile in enumerate(row):
				if tile is None:
					new_seats_state[y][x] = None
				else:
					if tile and neighbor_counts[y][x] >= occupied_threshold:
						tile = False
						state_changed = True
					elif not tile and neighbor_counts[y][x] == 0:
						tile = True
						state_changed = True
					new_seats_state[y][x] = tile

		seats_state = copy.deepcopy(new_seats_state)
		if not state_changed:
			break

	return sum(map(bool, sum(seats_state, [])))
