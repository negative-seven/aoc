from collections import Counter
from functools import cache

from .day_template import Day


class Day6(Day):
    @staticmethod
    def convert_input(raw_input):
        return Counter(int(n) for n in raw_input.split(','))

    @classmethod
    def run_first(cls, puzzle_input):
        return cls.simulate_fish(puzzle_input, 80)

    @classmethod
    def run_second(cls, puzzle_input):
        return cls.simulate_fish(puzzle_input, 256)

    @classmethod
    def simulate_fish(cls, fish_timers, total_time):
        return sum(cls.simulate_one_fish(timer, total_time) * count for timer, count in fish_timers.items())

    @classmethod
    @cache
    def simulate_one_fish(cls, timer, time_left):
        if timer >= time_left:
            return 1
        else:
            return cls.simulate_one_fish(6, time_left - timer - 1) + cls.simulate_one_fish(8, time_left - timer - 1)
