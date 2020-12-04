#!/usr/bin/env python
import re

def main():
    arr = []
    pwd_fmt = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    ind_lower = 0
    ind_upper = 1
    ind_policy = 2
    ind_pwd = 3

    with open('input.txt', 'r') as f:
        contents = f.readlines()
    
    for line in contents:
        code = list(re.findall(pwd_fmt, line.strip())[0])
        code[ind_upper] = int(code[ind_upper])
        code[ind_lower] = int(code[ind_lower])
        arr.append(code)
    #print(arr)
    
    valid_ctr = 0

    for line in arr:
        if CheckPolicy(line[ind_lower], line[ind_upper], line[ind_policy], line[ind_pwd]):
            valid_ctr+=1

    print("valid passwords: {}".format(valid_ctr))
    return 0

def CheckPolicy(lower, upper, key_char, pwd):
    count = pwd.count(key_char)
    #print("count: {} | {}-{}".format(count, lower, upper))
    if lower <= count <= upper:
        return True
    return False

if __name__ == "__main__":
    main()
