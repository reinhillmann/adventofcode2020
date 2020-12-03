#!/usr/bin/python3

import numpy

def load_data(filename) -> [str]:
    with open(filename, "r") as f:
        data = f.readlines()
        return [r.rstrip() for r in data]

def count_trees(landscape, slope) -> int:
    cols = len(landscape[0])
    rows = len(landscape)
    row = 0
    col = 0
    trees = 0
    while row < rows:
        char = landscape[row][col]
        if char == '#':
            trees += 1
        row += slope[1]
        col += slope[0]
        col %= cols
    return trees

if __name__ == "__main__":
    test_data = load_data("test.txt")
    actual_data = load_data("actual.txt")

    # Part 1
    slope = (3, 1)
    assert count_trees(test_data, slope) == 7
    print(count_trees(actual_data, slope))

    # Part 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    assert numpy.prod([count_trees(test_data, s) for s in slopes]) == 336
    print(numpy.prod([count_trees(actual_data, s) for s in slopes]))
