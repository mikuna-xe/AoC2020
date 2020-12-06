#!/usr/bin/env python
import re

def main():
    arr = []
    with open('input.txt', 'r') as f:
        arr = f.read().strip().split()
    #print(arr)
    
    seat_id_list = []
    for i in range(len(arr)):
        row_num = RowSearch(arr[i][0:7])
        #print(row_num)
        col_num = ColumnSearch(arr[i][7:])
        #print(col_num)
        seat_id = row_num*8+col_num
        seat_id_list.append(seat_id)
        #print("{}: row {}, col {}, seatID {}".format(arr[i], row_num, col_num, seat_id))

    print("max seat id: {}".format(max(seat_id_list)))

    return 0

def RowSearch(boarding_pass):
    range_upper = 128
    #print("row search boarding_pass: {}".format(boarding_pass))
    return BinarySearch(range(range_upper), boarding_pass, 'F', 'B')

def ColumnSearch(boarding_pass):
    range_upper = 8
    #print("column search boarding_pass: {}".format(boarding_pass))
    return BinarySearch(range(range_upper), boarding_pass, 'L', 'R')
    
def BinarySearch(row_array, instructions, lower, upper):
    if len(row_array) == 1:
        return row_array[0]
    
    if instructions[0] == lower:
        subset = row_array[:len(row_array)//2]
        return BinarySearch(subset, instructions[1:], lower, upper)
    else:
        subset = row_array[len(row_array)//2:]
        return BinarySearch(subset, instructions[1:], lower, upper)



if __name__ == "__main__":
    main()
