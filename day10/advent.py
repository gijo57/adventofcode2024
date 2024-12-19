import numpy as np
import heapq

with open('input.txt') as f:
    trail_map = np.array([[x for x in list(row.strip())] for row in f.readlines()])
    start_coords = [x for x in np.where(trail_map == '0')]
    starts = list(zip(start_coords[0], start_coords[1]))
    turn_left = np.array([[0, 1], [-1, 0]])
    turn_right = np.array([[0, -1], [1, 0]])
    direction = [1, 0]
    limit = len(trail_map)-1


def get_neighbors(current):
    neighbors = []
    potential_neighbors =  [[sum(x) for x in zip(current, direction)], [sum(x) for x in zip(current, np.dot(direction, turn_left))], [sum(x) for x in zip(current, np.dot(direction, turn_right))], [sum(x) for x in zip(current, np.dot(np.dot(direction, turn_right), turn_right))]]
    for neighbor in potential_neighbors:
        if (neighbor[0] < 0 or neighbor[0] > limit or neighbor[1] < 0 or neighbor[1] > limit):
            continue
        if (trail_map[neighbor[0]][neighbor[1]] == '.'):
            continue
        current_height = int(trail_map[current[0]][current[1]])
        neighbor_height = int(trail_map[neighbor[0]][neighbor[1]])
        if (neighbor_height - current_height == 1):
            neighbors.append(neighbor)
    return neighbors


def find_path(start):
    nodes = []
    visited = []
    trail_heads = 0
    trail_heads2 = 0
    nodes.append(start)

    while nodes:
        node = heapq.heappop(nodes)
        if (int(trail_map[node[0]][node[1]]) == 9):
            if (node not in visited):
                trail_heads += 1
            trail_heads2 += 1
            visited.append(node)
            continue
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            heapq.heappush(nodes, neighbor)
        visited.append(node)
    return trail_heads, trail_heads2


answer1, answer2 = 0, 0
for start in starts:
    trail_heads, trail_heads2 = find_path(start)
    answer1 += trail_heads
    answer2 += trail_heads2

print(answer1, answer2)