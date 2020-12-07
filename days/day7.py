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
	bag_direct_outer_containers = defaultdict(set)
	for outer_bag in bag_direct_contents:
		for inner_bag in bag_direct_contents[outer_bag]:
			bag_direct_outer_containers[inner_bag].add(outer_bag)

	return len(get_bag_outer_containers_recursively('shiny gold', bag_direct_outer_containers))

def run_second(bag_direct_contents):
	return sum(get_bag_contents_with_counts_recursively('shiny gold', bag_direct_contents).values())

def get_bag_outer_containers_recursively(bag, bag_direct_outer_containers):
	outer_containers = set()
	for outer_bag in bag_direct_outer_containers[bag]:
		outer_containers.add(outer_bag)
		try:
			outer_containers.update(get_bag_outer_containers_recursively(outer_bag, bag_direct_outer_containers))
		except KeyError:
			pass
	return outer_containers

def get_bag_contents_with_counts_recursively(bag, bag_direct_contents):
	contents = Counter()
	for inner_bag, inner_bag_count in bag_direct_contents[bag].items():
		inner_bag_contents = get_bag_contents_with_counts_recursively(inner_bag, bag_direct_contents)
		for b in inner_bag_contents:
			contents[b] += inner_bag_contents[b] * inner_bag_count
		contents[inner_bag] += inner_bag_count
	return contents
