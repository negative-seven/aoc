from collections import defaultdict, Counter
from typing import List, Callable

from .day_template import Day


class Day12(Day):
    @staticmethod
    def convert_input(raw_input):
        adjacent_caves = defaultdict(lambda: set())
        for row in raw_input.splitlines():
            a, b = row.split('-')
            adjacent_caves[a].add(b)
            adjacent_caves[b].add(a)
        return dict(adjacent_caves)

    @classmethod
    def run_first(cls, puzzle_input):
        return cls.count_paths(puzzle_input, lambda path, cave: cave.isupper() or cave not in path)

    @classmethod
    def run_second(cls, puzzle_input):
        def proceed_condition(path: List[str], cave: str):
            small_caves = Counter(c for c in path + [cave] if c.islower())
            if small_caves['start'] > 1:
                return False
            counts = [count for value, count in small_caves.most_common()]
            return len(counts) <= 1 or (counts[0] <= 2 and counts[1] <= 1)

        return cls.count_paths(puzzle_input, proceed_condition)

    @staticmethod
    def count_paths(adjacency_dict, proceed_condition: Callable[[List[str], str], bool]):
        paths = [['start']]
        completed_path_count = 0
        while paths:
            path = paths.pop()
            current_cave = path[-1]
            if current_cave == 'end':
                completed_path_count += 1
                continue
            for adjacent_cave in adjacency_dict[current_cave]:
                if proceed_condition(path, adjacent_cave):
                    paths.append(path + [adjacent_cave])

        return completed_path_count
