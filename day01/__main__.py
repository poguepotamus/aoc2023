from pathlib import Path
from Solver import Solver
from re import sub

class Solver(Solver):

	numbers = {
		'one': '1', 'two': '2', 'three': '3',
		'four': '4', 'five': '5', 'six': '6',
		'seven': '7', 'eight': '8', 'nine': '9',
	}

	def solve_a(self, input:list):
		total = 0
		for line in input:
			numeric_line = sub(r'[^\d]', '', line)
			total += int(numeric_line[0] + numeric_line[-1])
		return total

	def solve_b(self, input: list):
		total = 0
		new_input = []
		# Iterating through each of our lines.
		for line in input:
			new_line = ''
			# From left to right, replace each word with it's number.
			for start in range(len(line)):
				line_segment = line[start:]
				for word, number in self.numbers.items():
					if line_segment.startswith(word) or line_segment.startswith(number):
						new_line += number
						break
			# Add new line to our new input.
			new_input.append(new_line)

		return self.solve_a(new_input)

if __name__ == '__main__':
	Solver().report(
		Path(__file__).parent / 'testInput.txt',
		Path(__file__).parent / 'input.txt',
		Path(__file__).parent / 'testInput2.txt'
	)