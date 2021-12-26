import numpy as np

from .day_template import Day


class BingoBoard:
    BOARD_SIZE = 5

    def __init__(self, numbers):
        self.numbers = np.array(numbers)
        self.marked = np.zeros((BingoBoard.BOARD_SIZE, BingoBoard.BOARD_SIZE), dtype=bool)
        self.last_rolled_number = None

    def mark_number(self, number) -> None:
        self.marked[self.numbers == number] = True
        self.last_rolled_number = number

    def has_bingo(self) -> bool:
        for axis in range(2):
            if np.any(np.all(self.marked, axis=axis)):
                return True
        return False

    def get_score(self):
        return self.numbers.flatten()[~self.marked.flatten()].sum() * self.last_rolled_number


class Day4(Day):
    @staticmethod
    def convert_input(raw_input):
        sections = raw_input.split('\n\n')
        rolls = [int(n) for n in sections[0].split(',')]
        boards = [[[int(n) for n in row.split()] for row in board.splitlines()] for board in sections[1:]]
        return {
            'rolled_numbers': rolls,
            'board_numbers': boards,
        }

    @classmethod
    def run_first(cls, puzzle_input):
        boards = [BingoBoard(b) for b in puzzle_input['board_numbers']]
        for rolled_number in puzzle_input['rolled_numbers']:
            for board in boards:
                board.mark_number(rolled_number)
                if board.has_bingo():
                    return board.get_score()

    @classmethod
    def run_second(cls, puzzle_input):
        boards = [BingoBoard(b) for b in puzzle_input['board_numbers']]
        for rolled_number in puzzle_input['rolled_numbers']:
            for board in boards:
                board.mark_number(rolled_number)

            if len(boards) == 1 and boards[0].has_bingo():
                return boards[0].get_score()

            boards = [b for b in boards if not b.has_bingo()]
