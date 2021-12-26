import re

from .day_template import Day


class Day13(Day):
    @staticmethod
    def convert_input(raw_input):
        points_string, folds_string = raw_input.split('\n\n')
        points = {tuple(int(x) for x in line.split(',')) for line in points_string.splitlines()}
        folds = []
        for line in folds_string.splitlines():
            axis, coordinate_string = re.fullmatch(r'fold along ([xy])=(\d+)', line).groups()
            folds.append((axis, int(coordinate_string)))
        return {
            'points': points,
            'folds': folds,
        }

    @classmethod
    def run_first(cls, puzzle_input):
        return len(cls._fold_points(puzzle_input['points'], puzzle_input['folds'][0]))

    @classmethod
    def run_second(cls, puzzle_input):
        points = puzzle_input['points'].copy()
        for fold in puzzle_input['folds']:
            points = cls._fold_points(points, fold)

        output = ''
        width = max(p[0] for p in points) + 1
        height = max(p[1] for p in points) + 1
        for y in range(height):
            for x in range(width):
                output += '#' if (x, y) in points else ' '
            output += '\n'
        return output

    @classmethod
    def _fold_points(cls, points, fold):
        return {cls._mirror_point(point, *fold) for point in points}

    @staticmethod
    def _mirror_point(point, axis, coordinate):
        index = 'xy'.index(axis)
        if point[index] < coordinate:
            return point
        else:
            new_point = list(point)
            new_point[index] = coordinate * 2 - point[index]
            return tuple(new_point)
