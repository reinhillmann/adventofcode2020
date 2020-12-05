#!/usr/bin/python3

import math

def load_data(filename):
    with open(filename, 'r') as f:
        return [r.rstrip() for r in f.readlines()]

def binary_part(data, min_val, max_val):
    if len(data) == 0:
        return min_val
    half = math.ceil((max_val - min_val) / 2)
    if data[0] in ['B', 'R']:
        return binary_part(data[1:], min_val + half, max_val)
    if data[0] in ['F', 'L']:
        return binary_part(data[1:], min_val, max_val - half)

def decode_boarding_pass(boarding_pass):
    row = binary_part(boarding_pass[0:7], 0, 127)
    seat = binary_part(boarding_pass[7:10], 0, 7)
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
    print(set(expected_ids) - set(seats_ids))
