#!/usr/bin/python3

import math

def load_data(filename):
    with open(filename, 'r') as f:
        return f.read()

def part1(groups):
    return sum([len(set(group.replace('\n',''))) for group in groups])

def part2(groups):
    total = 0
    for group in groups:
        lines = group.replace('\n', ' ').split(' ')
        sets = [set([char for char in line]) for line in lines]
        common_chars = set.intersection(*sets)
        total += len(common_chars)
    return total

if __name__ == "__main__":
    data = load_data("data.txt")
    groups = [group for group in data.split('\n\n')]
    print(part1(groups))
    print(part2(groups))
