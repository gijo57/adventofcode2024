import re
import math
import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

with open('input.txt') as f:
    robots = [robot for robot in f.read().split('\n')]
    space_width, space_height, seconds = 101, 103, 100
    end_positions = []
    quadrant_limit_width = space_width // 2
    quadrant_limit_height = space_height // 2
    space_map = np.full((space_height, space_width), ' ')


def move_robot(position, velocity, seconds):
    final_x = (position[0] + velocity[0] * seconds) % space_width
    final_y = (position[1] + velocity[1] * seconds) % space_height
    return (final_x, final_y)

def find_robot_quadrant(end_position):
    x, y = end_position[0], end_position[1]
    if (x < quadrant_limit_width):
        if (y < quadrant_limit_height):
            return 1
        elif (y > quadrant_limit_height):
            return 3

    if (x > quadrant_limit_width):
        if (y < quadrant_limit_height):
            return 2
        elif (y > quadrant_limit_height):
            return 4


robots_per_quadrant = [0, 0, 0, 0]
for robot in robots:
    vals = re.findall(r'-*\d+', robot)
    position, velocity = [int(vals[0]), int(vals[1])], [int(vals[2]), int(vals[3])]
    space_map[position[1]][position[0]] = 'x'

    end_position = move_robot(position, velocity, seconds)
    end_positions.append(end_position)
    quadrant = find_robot_quadrant(end_position)

    if (quadrant):
        robots_per_quadrant[quadrant-1] += 1


outfile = open('output.txt', 'w')
seconds = 1
while seconds < 10000:
    for robot in robots:
        vals = re.findall(r'-*\d+', robot)
        position, velocity = [int(vals[0]), int(vals[1])], [int(vals[2]), int(vals[3])]
        if (seconds > 1):
            old_pos = [(position[0] + velocity[0] * (seconds-1)) % space_width, (position[1] + velocity[1] * (seconds-1)) % space_height]
        else:
            old_pos = position
        space_map[old_pos[1]][old_pos[0]] = ' '
        new_pos = [(position[0] + velocity[0] * seconds) % space_width, (position[1] + velocity[1] * seconds) % space_height]
        space_map[new_pos[1]][new_pos[0]] = 'x'
    print(seconds, file=outfile, end='\n')
    print(space_map, file=outfile, end='\n')
    seconds += 1


answer1 = math.prod(robots_per_quadrant)
print(answer1)