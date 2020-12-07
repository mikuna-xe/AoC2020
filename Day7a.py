#!/usr/bin/env python
import re

def main():
    arr = []
    with open('input2.txt', 'r') as f:
        arr = f.readlines()
    #print(arr)
    bag2find = "shiny gold"

    bag_dict = ParseContents(arr)

    sum_bags = 0
    for colour in bag_dict:
        if SearchColour(bag2find, colour, bag_dict):
            sum_bags += 1

    print("Bag options: {}".format(sum_bags-1))
    return 0

def SearchColour(target, colour, bag_dict):
    if colour == target:
        return True
    elif bag_dict[colour] == {}:
        return False
    
    contains_target = False
    #print("bag_dict[{}]: {}".format(colour, bag_dict[colour]))
    for sub_colour in bag_dict[colour]:
        contains_target = contains_target | SearchColour(target, sub_colour, bag_dict)
    return contains_target

def ParseContents(arry):
    re_bags = r"(\d+) (\w+ \w+) bag"
    output = [rule.strip() for rule in arry]
    outer_bags = dict()
    for rule in output:
        inner_bags = dict()
        [outer, inner] = rule.split(" bags contain ")
        inner_bag_list = re.findall(re_bags, inner)
        for bag in inner_bag_list:
            inner_bags[bag[1]] = int(bag[0])
        outer_bags[outer] = inner_bags
    #print(outer_bags)

    return outer_bags

if __name__ == "__main__":
    main()
