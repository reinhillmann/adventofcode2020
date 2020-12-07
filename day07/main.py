#!/usr/bin/python3

import re

def load_data(filename):
    with open(filename, 'r') as f:
        return [l.rstrip() for l in f.readlines()]


def build_bag_dictionary(data):
    bag_dict = {}
    for line in data:
        (bag, contains) = line.split(' bags contain ')
        bag_dict[bag] = {}
        for contained_bag in contains.replace(" bags.", "").replace(" bags", "").replace(" bag.", "").replace(" bag", "").split(", "):
            if contained_bag == "no other":
                continue
            (quantity, color) = re.match(r"^(\d+) (.+)", contained_bag).groups()
            bag_dict[bag][color] = int(quantity)
    return bag_dict


def find_bags_containing_color(data, color):
    colors = []
    for d in data.keys():
        if color in data[d]:
            colors.append(d)
    return colors

def find_number_of_bags_in_color(data, color):
    total = 1
    for key in data[color].keys():
        total += data[color][key] * find_number_of_bags_in_color(data, key)
    return total

if __name__ == "__main__":
    data = load_data('data.txt')
    bag_dict = build_bag_dictionary(data)
    colors = find_bags_containing_color(bag_dict, "shiny gold")
    for color in colors:
        colors.extend(find_bags_containing_color(bag_dict, color))

    # part 1
    print(len(set(colors)))

    # part 2
    # - 1 because we don't count the shiny gold bag:
    print(find_number_of_bags_in_color(bag_dict, "shiny gold") - 1)
