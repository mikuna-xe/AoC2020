#!/usr/bin/env python

def main():
    arr = []
    start_pos = (0,0)
    x_step = 3
    y_step = 1

    with open('input.txt', 'r') as f:
        contents = f.readlines()
    
    for line in contents:
        code = list(line.strip())
        arr.append(code)

    #print(*arr, sep="\n")

    print("Trees: {}".format(CountTrees(start_pos, x_step, y_step, arr)))
    
    return 0

def CountTrees(origin, x_step, y_step, map):
    tree_count = 0
    max_x = len(map[0])
    max_y = len(map)
    pos_x = origin[0]
    pos_y = origin[1]

    for i in range(max_y-1):
        #move x
        pos_x = pos_x + x_step
        if pos_x >= max_x:
            pos_x = pos_x - max_x
        #move y
        pos_y = pos_y + y_step

        if map[pos_y][pos_x] == '#':
            map[pos_y][pos_x] = 'X'
            tree_count += 1
        else:
            map[pos_y][pos_x] = 'O'
        
    #print(*map, sep="\n")
    return tree_count

if __name__ == "__main__":
    main()
