import re
from collections import Counter, defaultdict


def convert_input(raw_input):
	bag_direct_contents = dict()
	for line in raw_input.splitlines():
		outer_bag, raw_inner_bags = line.split(' bags contain ', 1)
		inner_bags = {bag: int(count) for count, bag in re.findall(r'(\d+) ([a-z]+ [a-z]+) bags?[,\.]', raw_inner_bags)}
		bag_direct_contents[outer_bag] = inner_bags

	return bag_direct_contents

def run_first(bag_direct_contents):
	bag_contents = generate_bag_contents(bag_direct_contents)
	return sum('shiny gold' in inner_bags for inner_bags in bag_contents.values())

def run_second(bag_direct_contents):
	bag_contents = generate_bag_contents(bag_direct_contents)
	return sum(bag_contents['shiny gold'].values())

def generate_bag_contents(bag_direct_contents):
	bag_contents = defaultdict(Counter)

	def get_one_bag_contents_recursively(bag):
		if bag not in bag_contents:
			for inner_bag, inner_bag_count in bag_direct_contents[bag].items():
				inner_bag_contents = get_one_bag_contents_recursively(inner_bag)
				for b in inner_bag_contents:
					bag_contents[bag][b] += inner_bag_contents[b] * inner_bag_count
				bag_contents[bag][inner_bag] += inner_bag_count

		return bag_contents[bag]


	for bag in bag_direct_contents:
		get_one_bag_contents_recursively(bag)

	return bag_contents
