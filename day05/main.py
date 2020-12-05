#!/usr/bin/python3

import math

def load_data(filename):
    with open(filename, 'r') as f:
        return [r.rstrip() for r in f.readlines()]

def decode_boarding_pass(bp):
    bp = bp.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0')
    row, seat = int(bp[0:7], 2), int(bp[7:10], 2)
    return (row, seat, row * 8 + seat)

if __name__ == "__main__":
    data = load_data("data.txt")

    # Part 1
    assert decode_boarding_pass('BFFFBBFRRR') == (70, 7, 567)
    assert decode_boarding_pass('FFFBBBFRRR') == (14, 7, 119)
    assert decode_boarding_pass('BBFFBBFRLL') == (102, 4, 820)
    print(max([decode_boarding_pass(bp)[2] for bp in data]))

    # Part 2
    seats_ids = [decode_boarding_pass(bp)[2] for bp in data]
    expected_ids = [n for n in range(min(seats_ids), max(seats_ids)+1)]
    for n in set(expected_ids) - set(seats_ids):
        print(n)
