#!/usr/bin/python3
import re

def load_data(filename):
    with open(filename, 'r') as f:
        return [int(l.rstrip()) for l in f.readlines()]


def find_first_not_sum(data, preamble):
    for i in range(preamble, len(data)):
        target = data[i]
        found = False
        for j in range(i-preamble, i-1):
            for k in range(i-preamble+1, i):
                if data[j] + data[k] == target:
                    found = True
                    continue
        if not found:
            return target

def find_contiguous_sum(data, target):
    break_out = False
    for i in range(0, len(data)):
        if break_out:
            break_out = False
            continue
        total = 0
        for j in range(i, len(data)):
            total += data[j]
            if total == target:
                return min(data[i:j+1]) + max(data[i:j+1])
            if total > target:
                break_out = True
                continue
    return None


if __name__ == "__main__":
    data = load_data('data.txt')

    preamble = 25
    part1_answer = find_first_not_sum(data, preamble)
    print(part1_answer) # 731031916

    part2_answer = find_contiguous_sum(data, part1_answer)
    print(part2_answer) # 93396727