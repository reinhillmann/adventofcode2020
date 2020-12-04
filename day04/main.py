#!/usr/bin/python3

import re

def load_data(filename) -> [str]:
    with open(filename, 'r') as f:
        return f.read()

def validate_number_range(n, min, max) -> bool:
    if not n.isnumeric():
        return False
    return min <= int(n) <= max

def validate_height(h, mincm, maxcm, minin, maxin):
    if h.endswith('cm'):
        return validate_number_range(h[:-2], mincm, maxcm)
    if h.endswith('in'):
        return validate_number_range(h[:-2], minin, maxin)
    return False

def validate_match_pattern(val, pattern):
    return bool(re.match(pattern, val))

def validate_eye_color(ecl, valid_colors):
    return ecl in valid_colors

def validate_passport(passport, deep_validation, expected_key_set) -> bool:
    if expected_key_set - set(passport):
        # not all keys are present, passport is invalid
        return False
    valid = True
    if deep_validation:
        valid &= validate_number_range(passport['byr'], 1920, 2002)
        valid &= validate_number_range(passport['iyr'], 2010, 2020)
        valid &= validate_number_range(passport['eyr'], 2020, 2030)
        valid &= validate_height(passport['hgt'], 150, 193, 59, 76)
        valid &= validate_match_pattern(passport['hcl'], r"^#[a-f0-9]{6}$")
        valid &= validate_eye_color(
            passport['ecl'], ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        valid &= validate_match_pattern(passport['pid'], r"^[0-9]{9}$")
    return valid

def count_valid_passports(data, expected_key_set, deep_validation=False) -> int:
    # splits the data into a list of passport strings
    passports = [p.replace('\n', ' ') for p in data.split('\n\n')]
    # creates a list of passport dictionaries
    passport_dicts = [{k.split(':')[0]: k.split(':')[1] for k in p.split(' ')} for p in passports]
    # returns the number of passports that are valid. Deep validation is for part2.
    return sum(
        [1 for p in passport_dicts if validate_passport(p, deep_validation, expected_key_set)])

if __name__ == '__main__':
    test_data = load_data('test.txt')
    actual_data = load_data('actual.txt')
    invalid_data = load_data('invalid.txt')
    valid_data = load_data('valid.txt')

    expected_key_set = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])  # omit cid

    # Part 1
    assert count_valid_passports(test_data, expected_key_set) == 2
    print(count_valid_passports(actual_data, expected_key_set))

    # Part 2
    assert count_valid_passports(invalid_data, expected_key_set, True) == 0
    assert count_valid_passports(valid_data, expected_key_set, True) == 4
    print(count_valid_passports(actual_data, expected_key_set, True))
