#!/usr/bin/env python

def main():
    arr = []
    with open('input.txt', 'r') as f:
        arr = f.read().split('\n\n')
    #print(arr)

    sum_count = 0
    for group in arr:
        sum_count += len(GetUniqueAnswers(group))

    print("sum of counts: {}".format(sum_count))
    return 0

def GetUniqueAnswers(group):
    split_group = []
    group = group.strip().split()
    for i in group:
        split_group.extend(list(i))
    #print(split_group)
    unique = set(split_group)
    #print(unique)
    return unique

if __name__ == "__main__":
    main()
