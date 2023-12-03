import re

RED = 12
GREEN = 13
BLUE = 14

with open('2.txt', 'r') as f:
    sum = 0
    for line in f:
        # parse game id and set info
        line = re.split(':|;', line.strip())
        game_id = int(line[0].split(' ')[1])
        cubesets = line[1:]
        max_red = 0
        max_green = 0
        max_blue = 0
        # count number of each color
        for cubeset in cubesets:
            cubeset = cubeset.split(',')
            for cube in cubeset:
                red_count = 0
                green_count = 0
                blue_count = 0
                if 'red' in cube:
                    red_count += int(cube.strip().split(' ')[0])
                    max_red = max(red_count, max_red)
                elif 'green' in cube:
                    green_count += int(cube.strip().split(' ')[0])
                    max_green = max(green_count, max_green)
                elif 'blue' in cube:
                    blue_count += int(cube.strip().split(' ')[0])
                    max_blue = max(blue_count, max_blue)
        sum += max_red*max_green*max_blue
    print(sum)
