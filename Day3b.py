#!/usr/bin/env python
import math
def main():
    arr = []
    start_pos = (0,0)
    x_step = [1,3,5,7,1]
    y_step = [1,1,1,1,2]

    with open('input.txt', 'r') as f:
        contents = f.readlines()
    
    for line in contents:
        code = list(line.strip())
        arr.append(code)

    #print(*arr, sep="\n")
    trees = []
    for i in range(len(x_step)):
        print("{},{}".format(x_step[i], y_step[i]))
        tree = CountTrees(start_pos, x_step[i], y_step[i], arr)
        print("Trees: {}".format(tree))
        trees.append(tree)
    print("multi trees: {}".format(math.prod(trees)))
    return 0

def CountTrees(origin, x_step, y_step, map):
    tree_count = 0
    max_x = len(map[0])
    max_y = len(map)
    pos_x = origin[0]
    pos_y = origin[1]

    #for i in range(max_y-1):
    while pos_y < max_y-1:
        #move x
        pos_x = pos_x + x_step
        if pos_x >= max_x:
            pos_x = pos_x - max_x
        #move y
        pos_y = pos_y + y_step

        if map[pos_y][pos_x] == '#':
            #map[pos_y][pos_x] = 'X'
            tree_count += 1
        #else:
            #map[pos_y][pos_x] = 'O'
        
    #print(*map, sep="\n")
    return tree_count

if __name__ == "__main__":
    main()
