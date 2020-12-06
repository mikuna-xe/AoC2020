#!/usr/bin/env python
import re

def main():
    arr = []

    with open('input.txt', 'r') as f:
        arr = f.read().split('\n\n')
    valid_count = 0

    for entry in arr:
        valid = CheckPassport(entry)
        if valid:
            valid_count += 1

    print("valid passports: {}".format(valid_count))

    return 0

def CheckPassport(passport):
    criteria = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    #fields = re.findall(r'byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:', ' '.join(passport))
    #if len(fields) != 7:
    #    return False

    passport = ParsePassport(passport)

    return (all(field in passport.keys() for field in criteria) and
        all(isValidField(field, passport[field]) for field in passport.keys())
        )

def isValidField(field, value):
    #print('field: {}, value: {}'.format(field, value))
    if field == "byr":
        return 1920 <= int(value) <= 2002
    elif field == "iyr":
        return 2010 <= int(value) <= 2020
    elif field == "eyr":
        return 2020 <= int(value) <= 2030
    elif field == "hgt":
        height, unit = re.search("(\d+)(\w+)", value).groups()
        return (
           unit == "cm" and 150 <= int(height) <= 193 or
           unit == "in" and 59 <= int(height) <= 76
        )
    elif field == "hcl":
        return bool(re.fullmatch("#[0-9a-f]{6}", value))
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return bool(re.fullmatch("\d{9}", value))
    elif field == "cid":
        return True
    else:
        return False

def ParsePassport(passport):
    passport = passport.strip().split()
    passport_dict = {}
    for field in passport:
        (field_key, field_value) = field.split(":")
        passport_dict[field_key] = field_value
    return passport_dict

if __name__ == "__main__":
    main()
