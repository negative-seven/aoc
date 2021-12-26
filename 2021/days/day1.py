from .day_template import Day


class Day1(Day):
    @staticmethod
    def convert_input(raw_input):
        return [int(n) for n in raw_input.split()]

    @classmethod
    def run_first(cls, puzzle_input):
        pairs = zip(puzzle_input[:-1], puzzle_input[1:])
        return sum(x < y for x, y in pairs)

    @classmethod
    def run_second(cls, puzzle_input):
        triplets = zip(puzzle_input, puzzle_input[1:], puzzle_input[2:])
        sums = [sum(triplet) for triplet in triplets]
        sum_pairs = zip(sums, sums[1:])
        return sum(x < y for x, y in sum_pairs)
