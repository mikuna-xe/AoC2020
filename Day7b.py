#!/usr/bin/env python
import re

def main():
    arr = []
    with open('input2.txt', 'r') as f:
        arr = f.readlines()
    #print(arr)
    bag2find = "shiny gold"
    bag_dict = ParseContents(arr)
    print(SearchColour(bag2find, bag_dict))
    return 0

def SearchColour(target, bag_dict):
    if bag_dict[target] == {}:
        return 0
    
    #print("bag_dict[{}]: {}".format(target, bag_dict[target]))
    sum_bags = 0
    for sub_colour, count in bag_dict[target].items():
        #print("sub_colour, count: {}, {}".format(sub_colour, count))
        bags_in_bag = SearchColour(sub_colour, bag_dict)
        #print("bags in '{}' bag: {}".format(sub_colour, sub_colour, bags_in_bag))
        sum_bags += (count * bags_in_bag + count)
        #print("sub_colour, sum_bags: {}, {}".format(sub_colour, sum_bags))
    return sum_bags

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
