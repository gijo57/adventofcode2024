import numpy as np

with open('example.txt') as f:
    labmap = np.array([list(row) for row in f.read().split('\n')])
    infinite_loops = 0
    start_position = np.where(labmap == '^')


def run_simulation(map, start_position):
    labmap = np.copy(map)
    current_position = [start_position[0][0], start_position[1][0]]
    labmap[current_position[0], current_position[1]] = 'X'
    directions = ['U', 'R', 'D', 'L']
    visited_with_directions = []
    direction_index = 0
    is_infinite = False

    while True:
        if (current_position[0] < 0 or current_position[0] > len(labmap) or current_position[1] < 0 or current_position[1] > len(labmap[0])):
            break
        labmap[current_position[0], current_position[1]] = 'X'
        next_position = [current_position[0]-1, current_position[1]]
        next_tile = labmap[next_position[0], next_position[1]]
        visited_with_direction = (current_position, directions[direction_index])

        if (next_tile == '#'):
            if (visited_with_direction in visited_with_directions):
                is_infinite = True
                break
            visited_with_directions.append(visited_with_direction)
            labmap[current_position[0], current_position[1]] = 'G'
            labmap = np.rot90(labmap, 1)
            direction_index += 1
            
            if (direction_index > 3):
                direction_index = 0
            current_position = np.where(labmap == 'G')
            current_position = [current_position[0][0], current_position[1][0]]
            continue
        current_position = next_position
    return np.count_nonzero(labmap == 'X'), labmap, is_infinite, visited_with_directions


result1 = run_simulation(labmap, start_position)
part_1_visited = result1[3]

answer2 = 0
for i in range(len(part_1_visited)):
    visited = part_1_visited[i][0]
    print(visited)
    map_copy = np.copy(labmap)
    map_copy[visited[0]][visited[1]] = '#'

    if (run_simulation(map_copy, start_position)[2]):
        answer2 += 1

answer1 = result1[0]
print(answer1, answer2)