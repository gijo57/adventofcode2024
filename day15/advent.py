import numpy as np

with open('example.txt') as f:
    storage_map, moves = f.read(). split('\n\n')


def set_initial_positions(storage_map):
    search_map = np.array([[pos for pos in list(row)] for row in storage_map.split('\n')])
    robot_position = np.where(search_map == '@')
    box_positions = np.where(search_map == 'O')
    wall_positions = np.where(search_map == '#')
    return [int(robot_position[0][0]), int(robot_position[1][0])], [[int(x), int(y)] for (x, y) in zip(*box_positions)], [[int(x), int(y)] for (x, y) in zip(*wall_positions)]


def map_moves(moves):
    directions = {
        '^': [-1, 0],
        'v': [1, 0],
        '<': [0, -1],
        '>': [0, 1]
    }
    return [directions[x] for x in moves if x != '\n']


def find_next_robot_position(start_position, boxes_to_move, move):
    new_robot_position = [start_position[0]-(len(boxes_to_move)*move[0]), start_position[1]-(len(boxes_to_move)*move[1])] if sum(move) > 0 else [start_position[0]+(len(boxes_to_move)*move[0]), start_position[1]+(len(boxes_to_move)*move[1])]
    return new_robot_position


def move_boxes(boxes, move, next_position):
    to_move = 1
    moved_boxes = []
    for box in boxes:
        moved_boxes.append([next_position[0]-(move[0]*to_move), next_position[1]-(move[1]*to_move)])
        to_move += 1
    return moved_boxes

def check_direction(move, start_position, box_positions, wall_positions, boxes_to_move=[]):
    next_position = list(np.add(start_position, move))
    print('next', next_position, box_positions)
    if (next_position in box_positions):
        boxes_to_move.append(box_positions.pop(box_positions.index(next_position)))
        return check_direction(move, next_position, box_positions, wall_positions, boxes_to_move)
    elif (next_position in wall_positions):
        #TODO find_next_robot_position function -> check bounds
        print('tomove', boxes_to_move)
        new_robot_position = find_next_robot_position(start_position, boxes_to_move, move)
        moved_boxes = move_boxes(boxes_to_move, move, next_position)
        print(moved_boxes)
        box_positions.extend(moved_boxes)
        boxes_to_move.clear()
        return new_robot_position, box_positions
    else:
        return check_direction(move, next_position, box_positions, wall_positions, boxes_to_move)



robot_position, box_positions, wall_positions = set_initial_positions(storage_map)
moves_list = map_moves(moves)

while moves_list:
    print('-----------')
    print('robot', robot_position)
    move = moves_list.pop(0)
    print('move', move)
    robot_position, box_positions = check_direction(move, robot_position, box_positions, wall_positions)
