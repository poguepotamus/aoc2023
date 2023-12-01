from pathlib import Path

class Solver():
    """ Base class for puzzle solvers.

        A "Solver" file should be placed in each days' folder. It should contain a class "Solver" that inherits from this class.

        The child class should override the solveA() and solveB() methods. The Solver.report() method should be called that will call both methods, and print the values to the terminal for the user to view.

        Attributes:
            None
    """
    def read_puzzle_input(self, input_file:Path):
        """ Opens a puzzle input file and hands it to the method that solves puzzle input's as strings.

        This feeds the puzzle input file as a list of strings to self.solve().

        Arguments:
            inputFile(Path): Path to the puzzle input file
        """
        # Typically, we don't need to worry about closing our file, but I want to release it as soon as possible.
        input_data = None
        with open(input_file, 'r', encoding='utf-8') as inFile:
            input_data = inFile.read().splitlines()
        return input_data

    def solve_part_1(self, puzzle_input:list):
        """ Solves the puzzle input.

            This method should be overridden by the child class.

            Arguments:
                input(list): List of strings representing the puzzle input
        """
        raise NotImplementedError('This method should be overridden by the child class.')

    def solve_part_2(self, puzzle_input:list):
        """ Solves the puzzle input.

            This method should be overridden by the child class.

            Arguments:
                input(list): List of strings representing the puzzle input
        """
        raise NotImplementedError('This method should be overridden by the child class.')

    def report(self, test_input:Path, puzzle_input:Path=None, part_2_test_input:Path=None):
        """ Prints the solution to the console.

            Because some part 2's can have a different test input, I've allowed each of the inputs to be passed in separately.

            The puzzle input, and part 2 test input are optional. Those methods will only be run IF the corresponding argument is passed in.

            In addition. if the argument is passed in and a not implimented error is raised, the error will be caught and a message will be printed to the console.

            Arguments:
                inputFile(Path): Path to the puzzle input file
        """
        # Printing which input files we're using.
        print(f'\nTest input: `{test_input}`:')
        if puzzle_input:
            print(f'Puzzle input: `{puzzle_input}`:')
        if part_2_test_input:
            print(f'Part 2 test input: `{part_2_test_input}`:')

        # Running our solvers for part 1.
        print('\nPart 1:')
        print(f'	Test 1: {self.solve_part_1(self.read_puzzle_input(test_input))}')
        # If we have a puzzle input, run it through the solver as well.
        if puzzle_input:
            print(f'	Part 1: {self.solve_part_1(self.read_puzzle_input(puzzle_input))}')

        # Running our solvers for part 2.
        try:
            # If part 2 test input is not passed in, use the test input.
            test_input = part_2_test_input or test_input
            # If our part 2 isn't implimented, we'll catch the error and print a message to the console.
            test2solution = self.solve_part_2(self.read_puzzle_input(test_input))
            # Now we know part2 is implimented, we'll print the solution.
            print('\nPart 2:')
            print(f'	Test 2: {test2solution}')

            # Now, we can run the puzzle input through the solver if we have it.
            if puzzle_input:
                print(f'	Part 2: {self.solve_part_2(self.read_puzzle_input(puzzle_input))}')
        except NotImplementedError:
            print('    Part 2: Not implemented.')