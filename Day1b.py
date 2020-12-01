#!/usr/bin/env python

def CheckIfSum(item0, item1, lst, target):
    item2 = target - item0 - item1
    s = set(lst)
    s.discard(item0)
    s.discard(item1)
    if item2 in s:
        return item2 * item1 * item0
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
        for j in arr:
            output = CheckIfSum(i, j, arr, target)
            if output is not None:
                print(output)
                return 0

if __name__ == "__main__":
    main()
