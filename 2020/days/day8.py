import copy
from enum import Enum


class Interpreter:
	def __init__(self, instructions):
		self.instructions = instructions
		self.program_counter_values = set()
		self.program_counter = 0
		self.accumulator = 0

	def step(self):
		if self.program_counter in self.program_counter_values:
			return InterpreterResult.LoopDetected
		self.program_counter_values.add(self.program_counter)

		instruction = self.get_next_instruction()
		if instruction is None:
			return InterpreterResult.Halt

		if instruction.opcode == 'acc':
			self.accumulator += instruction.operand
		elif instruction.opcode == 'jmp':
			self.program_counter += instruction.operand - 1

		self.program_counter += 1

		return InterpreterResult.Success

	def get_next_instruction(self):
		try:
			return self.instructions[self.program_counter]
		except IndexError:
			return None

	def run_until_loop_or_end(self):
		while True:
			result = self.step()
			if result != InterpreterResult.Success:
				return result


class InterpreterResult(Enum):
	Success = 0
	Halt = 1
	LoopDetected = 2


class Instruction:
	def __init__(self, opcode, operand):
		self.opcode = opcode
		self.operand = operand


def convert_input(raw_input):
	instructions = []
	for line in raw_input.splitlines():
		opcode, operand = line.split(' ', 1)
		instructions.append(Instruction(opcode, int(operand)))

	return instructions

def run_first(instructions):
	interpreter = Interpreter(instructions)
	interpreter.run_until_loop_or_end()
	return interpreter.accumulator

def run_second(instructions):
	SWAPPED_INSTRUCTIONS = ['nop', 'jmp']

	main_interpreter = Interpreter(instructions)

	while True:
		instruction = main_interpreter.get_next_instruction()
		if instruction.opcode in SWAPPED_INSTRUCTIONS:
			interpreter_copy = copy.deepcopy(main_interpreter)
			new_opcode = SWAPPED_INSTRUCTIONS[not SWAPPED_INSTRUCTIONS.index(instruction.opcode)]
			interpreter_copy.instructions[interpreter_copy.program_counter].opcode = 'nop' if instruction.opcode == 'jmp' else 'jmp'
			if interpreter_copy.run_until_loop_or_end() == InterpreterResult.Halt:
				return interpreter_copy.accumulator

		main_interpreter.step()
