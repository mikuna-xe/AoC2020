#!/usr/bin/env python
import re

def main():
    arr = []

    with open('input.txt', 'r') as f:
        contents = f.read()
    
    arr = contents.split('\n\n')
    batch = []
    valid_count = 0

    for entry in arr:
        batch.append(entry.split())
        passport = entry.split()
        valid = CheckPassport(passport)
        if valid:
            valid_count += 1

    #print(*batch, sep='\n')
    #print(arr)
    print("valid passports: {}".format(valid_count))

    return 0

def CheckPassport(passport):
    #criteria = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    fields = re.findall(r'byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:', ' '.join(passport))
    if len(fields) == 7:
        return True
    return False

if __name__ == "__main__":
    main()
