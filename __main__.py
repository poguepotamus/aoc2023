from pathlib import Path

from Solver import Solver

class DayX(Solver):
    """Day X"""

    def solve_part_1(self, puzzle_input:list):
        total = 0
        return total

    def solve_part_2(self, puzzle_input:list):
        return NotImplementedError('Part 2 not implemented yet.')

if __name__ == '__main__':
    DayX().report(
        Path(__file__).parent / 'testInput',
        Path(__file__).parent / 'input',
    )