#!/usr/bin/env python
import re

def main():
    arr = []
    pwd_fmt = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    ind_pos1 = 0
    ind_pos2 = 1
    ind_policy = 2
    ind_pwd = 3

    with open('input.txt', 'r') as f:
        contents = f.readlines()
    
    for line in contents:
        code = list(re.findall(pwd_fmt, line.strip())[0])
        code[ind_pos2] = int(code[ind_pos2])
        code[ind_pos1] = int(code[ind_pos1])
        arr.append(code)
    #print(arr)
    
    valid_ctr = 0

    for line in arr:
        if CheckPolicy(line[ind_pos1], line[ind_pos2], line[ind_policy], line[ind_pwd]):
            valid_ctr+=1

    print("valid passwords: {}".format(valid_ctr))
    return 0

def CheckPolicy(pos1, pos2, key_char, pwd):
    a = False
    b = False
    if list(pwd)[pos1-1] == key_char:
        a = True
    if list(pwd)[pos2-1] == key_char:
        b = True
    #print("count: {} | {}-{}".format(count, lower, upper))
    return a != b

if __name__ == "__main__":
    main()
