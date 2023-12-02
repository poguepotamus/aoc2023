from pathlib import Path
from functools import reduce

from Solver import Solver


class Day02(Solver):
    """Day 2"""

    test_bag = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    def solve_part_1(self, puzzle_input:list):
        possible_games = []
        # Iterating through our games (each line)
        for game_num, bag in enumerate(puzzle_input, 1):
            # Removing our game iterator from the line. We handle that in code.
            game_possible = True
            bag = bag.split(': ')[1]

            game_summary = self.summarize_game(bag)

            for color, numbers in game_summary.items():
                # If we don't have record of that color in our test bag, then our game isn't possible
                # If our minimum number is greater than the number in our test bag, then our game isn't possible
                if color not in self.test_bag or max(numbers) > self.test_bag[color]:
                    game_possible = False
                    break

            possible_games.append(game_num if game_possible else 0)
        return sum(possible_games)

    def solve_part_2(self, puzzle_input:list):
        total = 0
        # Iterating through our games (each line)
        for bag in puzzle_input:
            # Removing our game iterator from the line. We handle that in code.
            bag = bag.split(': ')[1]

            game_summary = self.summarize_game(bag)

            # Finding the lowest number for each color in the bag
            game_summary = {color: max(numbers) for color, numbers in game_summary.items()}

            # Then finding the power of the lowest number for each color
            total += reduce(lambda x, y: x * y, game_summary.values())

        return total

    def iter_pull(self, pull:str) -> (str, int):
        """Parses a pull into a dictionary of color: number"""
        for color_cluster in pull.split(', '):
            number, color = color_cluster.split(' ')
            yield color, int(number)

    def iter_game(self, game:str) -> dict:
        """Parses a game into a dictionary of color: number.

            Returns a generator of dictionaries for each pull in a game.
        """
        for pull in game.split('; '):
            pull_dict = {}
            for color, number in self.iter_pull(pull):
                pull_dict[color] = number
            yield pull_dict

    def summarize_game(self, game:str) -> dict:
        """Parses a game into a dictionary of color: [numbers]."""
        game_dict = {}

        # Iterating through each pulls in the game
        for pull in self.iter_game(game):

            for color, number in pull.items():
                # If our color doesn't exist in our game dictionary, we add it
                if color not in game_dict:
                    game_dict[color] = []

                # Then, we append our number to the appropriate color list
                game_dict[color].append(int(number))

        return game_dict


if __name__ == '__main__':
    Day02().report(
        Path(__file__).parent / 'testInput',
        Path(__file__).parent / 'input',
    )
