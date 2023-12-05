from pathlib import Path

from Solver import Solver
from Engine import Engine

class DayX(Solver):
    """Day X"""

    def solve_part_1(self, puzzle_input:list):
        total = 0
        engine = Engine(puzzle_input)
        engine.find_adjacent(2, 0)

        return total

    def solve_part_2(self, puzzle_input:list):
        return NotImplementedError('Part 2 not implemented yet.')

if __name__ == '__main__':
    DayX().report(
        Path(__file__).parent / 'testInput',
        Path(__file__).parent / 'input',
    )