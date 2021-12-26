from collections import Counter
import numpy as np
import re

from .day_template import Day


class Day5(Day):
    @staticmethod
    def convert_input(raw_input):
        return [[int(n) for n in re.findall(r'\d+', line)] for line in raw_input.splitlines()]

    @classmethod
    def run_first(cls, puzzle_input):
        return cls.count_overlaps(puzzle_input, False)

    @classmethod
    def run_second(cls, puzzle_input):
        return cls.count_overlaps(puzzle_input, True)

    @staticmethod
    def count_overlaps(line_data, include_diagonals: bool):
        point_counts = Counter()
        for x0, y0, x1, y1 in line_data:
            step_x = np.sign(x1 - x0)
            step_y = np.sign(y1 - y0)
            if not include_diagonals and step_x != 0 and step_y != 0:
                continue

            step_count = max(abs(x1 - x0), abs(y1 - y0)) + 1  # inclusive on both ends
            for step_index in range(step_count):
                x = x0 + step_index * step_x
                y = y0 + step_index * step_y
                point_counts[(x, y)] += 1

        return sum(1 for c in point_counts.values() if c > 1)
