#!/usr/bin/python3

import numpy

def load_data(filename) -> [str]:
    with open(filename, "r") as f:
        return f.readlines()

def count_trees(landscape, slope):
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
        col %= (cols - 1)
    return trees

if __name__ == "__main__":
    slope = (3, 1)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    test_data = load_data("test.txt")
    actual_data = load_data("actual.txt")

    assert count_trees(test_data, slope) == 7
    print(count_trees(actual_data, slope))

    assert numpy.prod([count_trees(test_data, s) for s in slopes]) == 336
    print(numpy.prod([count_trees(actual_data, s) for s in slopes]))
