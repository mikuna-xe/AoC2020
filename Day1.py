#!/usr/bin/env python

def CheckIfSum(item, lst, target):
    to_find = target - item
    s = set(lst)
    s.discard(item)
    if to_find in s:
        return to_find * item
    else:
        return None

def main():
    arr = []
    with open('input.txt', 'r') as f:
        contents = f.read()
    input_list = contents.strip().split('\n')
    arr = list(map(int, input_list))

    target = 2020
    for i in arr:
        output = CheckIfSum(i, arr, target)
        if output is not None:
            print(output)
            return 0

if __name__ == "__main__":
    main()
