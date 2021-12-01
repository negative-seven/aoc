import itertools
import re
from enum import Enum


class InstructionType(Enum):
	SetMask = 0,
	SetMemory = 1,


def convert_input(raw_input):
	instructions = []
	for line in raw_input.splitlines():
		if match := re.fullmatch(r'mask = ([01X]{36})', line):
			instructions.append((InstructionType.SetMask, (match.group(1),)))
		elif match := re.fullmatch(r'mem\[(\d+)\] = (\d+)', line):
			instructions.append((InstructionType.SetMemory, (match.group(1), match.group(2))))
	return instructions

def run_first(instructions):
	or_mask_translation_table = str.maketrans('X01', '001')
	and_mask_translation_table = str.maketrans('X01', '101')
	memory = {}

	for instruction in instructions:
		instruction_type = instruction[0]
		arguments = instruction[1]
		if instruction_type == InstructionType.SetMask:
			or_mask = int(arguments[0].translate(or_mask_translation_table), 2)
			and_mask = int(arguments[0].translate(and_mask_translation_table), 2)
		elif instruction_type == InstructionType.SetMemory:
			memory[int(arguments[0])] = (int(arguments[1]) | or_mask) & and_mask

	return sum(memory.values())

def run_second(instructions):
	or_mask_translation_table = str.maketrans('X01', '001')
	memory = {}

	for instruction in instructions:
		instruction_type = instruction[0]
		arguments = instruction[1]

		if instruction_type == InstructionType.SetMask:
			or_mask = int(arguments[0].translate(or_mask_translation_table), 2)
			floating_bit_indices = [index for index, bit_mask in enumerate(arguments[0][::-1]) if bit_mask == 'X']
		elif instruction_type == InstructionType.SetMemory:
			base_address = int(arguments[0]) | or_mask
			for floating_bit_replacement in itertools.product([0, 1], repeat=len(floating_bit_indices)):
				address = base_address
				for index, bit in zip(floating_bit_indices, floating_bit_replacement):
					if bit:
						address |= 1 << index
					else:
						address &= ~(1 << index)

				memory[address] = int(arguments[1])

	return sum(memory.values())
